import os
import tensorflow as tf
import numpy as np

curr_dir = os.path.dirname(os.path.realpath(__file__))

from qiznlp.common.modules.common_layers import mask_nonpad_from_embedding, add_timing_signal_1d, label_smoothing, softmax_cross_entropy
from qiznlp.common.modules.embedding import embedding
from qiznlp.common.modules.encoder import transformer_encoder, mean_pool, multi_head_attention_base_pool
import qiznlp.common.utils as utils

conf = utils.dict2obj({
    "vocab_size": 14180,
    'label_size': 16,
    "embed_size": 300,
    'hidden_size': 300,
    'num_heads': 6,
    'num_encoder_layers': 6,
    'dropout_rate': 0.2,
    'lr': 1e-3,
    'pretrain_emb': None,
    # 'pretrain_emb': np.load(f'{curr_dir}/pretrain_word_emb300.npy'),
})


class Model(object):
    def __init__(self, build_graph=True, **kwargs):

        self.conf = conf
        if build_graph:
            # build placeholder
            self.build_placeholder()
            # build model
            self.model_name = kwargs.get('model_name', 'trans_meanpool')
            {
                'trans_meanpool': self.build_model,
                'trans_mhattnpool': self.build_model1,
                # add new here
            }[self.model_name]()
            print(f'model_name: {self.model_name} build graph ok!')

    def build_placeholder(self):
        # placeholder
        # 原则上模型输入输出不变，不需换新model
        self.s1 = tf.placeholder(tf.int32, [None, None], name='s1')
        self.target = tf.placeholder(tf.int32, [None], name="target")
        self.dropout_rate = tf.placeholder(tf.float32, name="dropout_rate")

    def build_model(self):
        s1_embed, _ = embedding(tf.expand_dims(self.s1, -1), conf.vocab_size, conf.embed_size, pretrain_embedding=conf.pretrain_emb)

        """ encoder """
        # encoder_input  # [batch,length,embed]
        encoder_input = s1_embed
        encoder_valid_mask = mask_nonpad_from_embedding(encoder_input)  # [batch,length] 1 for nonpad; 0 for pad
        encoder_input = add_timing_signal_1d(encoder_input)  # add position embedding
        encoder_input = tf.layers.dropout(encoder_input, self.dropout_rate)  # dropout

        encoder_output = transformer_encoder(encoder_input, encoder_valid_mask,
                                             hidden_size=conf.hidden_size,
                                             filter_size=conf.hidden_size * 4,
                                             num_heads=conf.num_heads,
                                             num_encoder_layers=conf.num_encoder_layers,
                                             dropout=self.dropout_rate,
                                             attention_dropout=self.dropout_rate,
                                             relu_dropout=self.dropout_rate,
                                             )

        mean_pool_output = mean_pool(encoder_output, encoder_valid_mask)

        self.logits = tf.layers.dense(mean_pool_output, conf.label_size, use_bias=True, name='logits')  # [batch,cls]
        self.one_hot_target = tf.one_hot(self.target, conf.label_size)
        smooth_one_hot_target = label_smoothing(self.one_hot_target)
        self.loss = softmax_cross_entropy(self.logits, smooth_one_hot_target)
        self.y_prob = tf.nn.softmax(self.logits)
        self.y_prob = tf.identity(self.y_prob, name='y_prob')

        with tf.name_scope("accuracy"):
            self.correct = tf.equal(
                tf.argmax(self.logits, -1, output_type=tf.int32),
                self.target)
            self.accuracy = tf.reduce_mean(tf.cast(self.correct, tf.float32))

        self.global_step = tf.train.get_or_create_global_step()
        self.optimizer = tf.train.AdamOptimizer(learning_rate=conf.lr)
        self.train_op = self.optimizer.minimize(self.loss, global_step=self.global_step)

    def build_model1(self):
        # pretrained_word_embeddings = np.load(f'{curr_dir}/pretrain_emb_300.npy')
        pretrained_word_embeddings = None
        s1_embed, _ = embedding(tf.expand_dims(self.s1, -1), conf.vocab_size, conf.embed_size, pretrain_embedding=pretrained_word_embeddings)

        """ encoder """
        # encoder_input  # [batch,length,embed]
        encoder_input = s1_embed
        encoder_valid_mask = mask_nonpad_from_embedding(encoder_input)  # [batch,length] 1 for nonpad; 0 for pad
        encoder_input = add_timing_signal_1d(encoder_input)  # add position embedding
        encoder_input = tf.layers.dropout(encoder_input, self.dropout_rate)  # dropout

        encoder_output = transformer_encoder(encoder_input, encoder_valid_mask,
                                             hidden_size=conf.hidden_size,
                                             filter_size=conf.hidden_size * 4,
                                             num_heads=conf.num_heads,
                                             num_encoder_layers=conf.num_encoder_layers,
                                             dropout=self.dropout_rate,
                                             attention_dropout=self.dropout_rate,
                                             relu_dropout=self.dropout_rate,
                                             )

        # attention # e.g. HAN
        attn_output = multi_head_attention_base_pool(encoder_output, encoder_valid_mask,
                                                     conf.embed_size,
                                                     conf.embed_size,
                                                     6,
                                                     name='sent_pool',
                                                     reuse=tf.AUTO_REUSE,
                                                     dropout=self.dropout_rate,
                                                     attn_v=None)

        self.logits = tf.layers.dense(attn_output, conf.label_size, use_bias=True, name='logits')  # [batch,cls]
        self.one_hot_target = tf.one_hot(self.target, conf.label_size)
        smooth_one_hot_target = label_smoothing(self.one_hot_target)
        self.loss = softmax_cross_entropy(self.logits, smooth_one_hot_target)
        self.y_prob = tf.nn.softmax(self.logits)
        self.y_prob = tf.identity(self.y_prob, name='y_prob')

        with tf.name_scope("accuracy"):
            self.correct = tf.equal(
                tf.argmax(self.logits, -1, output_type=tf.int32),
                self.target)
            self.accuracy = tf.reduce_mean(tf.cast(self.correct, tf.float32))

        self.global_step = tf.train.get_or_create_global_step()
        self.optimizer = tf.train.AdamOptimizer(learning_rate=conf.lr)
        self.train_op = self.optimizer.minimize(self.loss, global_step=self.global_step)

    @classmethod
    def sent2ids(cls, sent, word2id, max_word_len=None):
        # sent 已分好词 ' '隔开
        # 形成batch时才动态补齐长度
        words = sent.split(' ')
        token_ids = [word2id.get(word, word2id['<unk>']) for word in words]
        if max_word_len:
            token_ids = token_ids[:max_word_len]
        return token_ids  # [len]

    @classmethod
    def label2id(cls, label, label2id):
        label_id = label2id.get(label, label2id['<unk>'])
        return label_id

    def create_feed_dict_from_data(self, data, ids, mode='train'):
        # data:数据已经转为id, data不同字段保存该段字段全量数据
        batch_s1 = [data['s1'][i] for i in ids]
        if len(set([len(e) for e in batch_s1])) != 1:  # 长度不等
            batch_s1 = utils.pad_sequences(batch_s1, padding='post')
        feed_dict = {
            self.s1: batch_s1,
            self.target: [data['target'][i] for i in ids],
        }
        if mode == 'train': feed_dict['num'] = len(batch_s1)
        feed_dict[self.dropout_rate] = conf.dropout_rate if mode == 'train' else 0.
        return feed_dict

    def create_feed_dict_from_features(self, features, mode='train'):
        # feature:tfrecord数据的example, 每个features的不同字段包括该字段一个batch数据
        feed_dict = {
            self.s1: features['s1'],
            self.target: features['target'],
        }
        if mode == 'train': feed_dict['num'] = len(features['s1'])
        feed_dict[self.dropout_rate] = conf.dropout_rate if mode == 'train' else 0.
        return feed_dict

    def create_feed_dict_from_raw(self, batch_s1, batch_y, token2id_dct, mode='infer'):
        word2id = token2id_dct['word2id']
        label2id = token2id_dct['label2id']

        feed_s1 = [self.sent2ids(s1, word2id) for s1 in batch_s1]
        if len(set([len(e) for e in feed_s1])) != 1:  # 长度不等
            feed_s1 = utils.pad_sequences(feed_s1, padding='post')

        feed_dict = {
            self.s1: np.array(feed_s1),
        }
        feed_dict[self.dropout_rate] = conf.dropout_rate if mode == 'train' else 0.

        if mode == 'infer':
            return feed_dict

        if mode in ['train', 'dev']:
            feed_target = [self.label2id(y, label2id) for y in batch_y]
            feed_dict[self.target] = feed_target
            return feed_dict
        raise ValueError(f'mode type {mode} not support')

    @classmethod
    def generate_data(cls, file, token2id_dct):
        word2id = token2id_dct['word2id']
        label2id = token2id_dct['label2id']
        data = {
            's1': [],
            'target': []
        }
        with open(file, 'r', encoding='U8') as f:
            for i, line in enumerate(f):
                item = line.strip().split('\t')
                s1 = item[0]
                y = item[1]
                s1_ids = cls.sent2ids(s1, word2id, max_word_len=50)
                y_id = cls.label2id(y, label2id)
                data['s1'].append(s1_ids)
                data['target'].append(y_id)
        data['num_data'] = len(data['s1'])
        return data

    @classmethod
    def generate_tfrecord(cls, file, token2id_dct, tfrecord_file):
        from qiznlp.common.tfrecord_utils import items2tfrecord
        word2id = token2id_dct['word2id']
        label2id = token2id_dct['label2id']

        def items_gen():
            with open(file, 'r', encoding='U8') as f:
                for i, line in enumerate(f):
                    item = line.strip().split('\t')
                    if len(item) != 2:
                        print(repr(line))
                        continue
                    try:
                        s1 = item[0]
                        y = item[1]
                        s1_ids = cls.sent2ids(s1, word2id, max_word_len=50)
                        y_id = cls.label2id(y, label2id)
                        if i < 5:  # check
                            print(f'check {i}:')
                            print(f'{s1} -> {s1_ids}')
                            print(f'{y} -> {y_id}')
                        d = {
                            's1': s1_ids,
                            'target': y_id,
                        }
                        yield d
                    except:
                        continue

        count = items2tfrecord(items_gen(), tfrecord_file)
        return count

    @classmethod
    def load_tfrecord(cls, tfrecord_file, batch_size=128, index=None, shard=None):
        from qiznlp.common.tfrecord_utils import tfrecord2dataset, exist_tfrecord_file
        if not exist_tfrecord_file(tfrecord_file):
            return None, None
        feat_dct = {
            's1': tf.VarLenFeature(tf.int64),
            'target': tf.FixedLenFeature([], tf.int64),
        }
        dataset, count = tfrecord2dataset(tfrecord_file, feat_dct, batch_size=batch_size, auto_pad=True, index=index, shard=shard)
        return dataset, count

    def get_signature_export_model(self):
        inputs_dct = {
            's1': self.s1,
            'dropout_rate': self.dropout_rate,
        }
        outputs_dct = {
            'y_prob': self.y_prob,
        }
        return inputs_dct, outputs_dct

    @classmethod
    def get_signature_load_pbmodel(cls):
        inputs_lst = ['s1', 'dropout_rate']
        outputs_lst = ['y_prob']
        return inputs_lst, outputs_lst

    @classmethod
    def from_pbmodel(cls, pbmodel_dir, sess):
        meta_graph_def = tf.saved_model.loader.load(sess, [tf.saved_model.tag_constants.SERVING], pbmodel_dir)  # 从pb模型载入graph和variable,绑定到sess
        signature = meta_graph_def.signature_def  # 取出signature_def
        default_key = tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY  # or 'chitchat_predict' 签名
        inputs_lst, output_lst = cls.get_signature_load_pbmodel()  # 类方法
        pb_dict = {}
        for k in inputs_lst:
            pb_dict[k] = sess.graph.get_tensor_by_name(signature[default_key].inputs[k].name)  # 从signature中获取输入输出的tensor_name,并从graph中取出
        for k in output_lst:
            pb_dict[k] = sess.graph.get_tensor_by_name(signature[default_key].outputs[k].name)
        model = cls(build_graph=False)  # 里面不再构造图
        for k, v in pb_dict.items():
            setattr(model, k, v)  # 绑定必要的输入输出到实例
        return model

    @classmethod
    def from_ckpt_meta(cls, ckpt_name, sess, graph):
        with graph.as_default():
            saver = tf.train.import_meta_graph(ckpt_name + '.meta', clear_devices=True)
            sess.run(tf.global_variables_initializer())

        model = cls(build_graph=False)  # 里面不再构造图
        # 绑定必要的输入输出到实例
        model.s1 = graph.get_tensor_by_name('s1:0')
        model.dropout_rate = graph.get_tensor_by_name('dropout_rate:0')
        # self.target = self.graph.get_tensor_by_name('target:0')
        model.y_prob = graph.get_tensor_by_name('y_prob:0')

        saver.restore(sess, ckpt_name)
        print(f':: restore success! {ckpt_name}')
        return model, saver
