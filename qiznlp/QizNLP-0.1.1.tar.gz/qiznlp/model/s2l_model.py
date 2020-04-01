import os
import tensorflow as tf
import numpy as np

curr_dir = os.path.dirname(os.path.realpath(__file__))

from qiznlp.common.modules.common_layers import mask_nonpad_from_embedding
from qiznlp.common.modules.embedding import embedding
from qiznlp.common.modules.birnn import Bi_RNN
from qiznlp.common.modules.idcnn import IDCNN
import qiznlp.common.utils as utils

conf = utils.dict2obj({
    "vocab_size": 1847,
    "embed_size": 300,
    'label_size': 30,
    'birnn_hidden_size': 300,
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
            self.model_name = kwargs.get('model_name', 'birnn')
            {
                'birnn': self.build_model,
                'idcnn': self.build_model1,
                # add new here
            }[self.model_name]()
            print(f'model_name: {self.model_name} build graph ok!')

    def build_placeholder(self):
        # placeholder
        # 原则上模型输入输出不变，不需换新model
        self.s1 = tf.placeholder(tf.int32, [None, None], name='s1')
        self.ner_label = tf.placeholder(tf.int32, [None, None], name='ner_label')
        self.dropout_rate = tf.placeholder(tf.float32, name="dropout_rate")

    def build_model(self):
        # embedding
        # [batch,len,embed]
        s1_embed, _ = embedding(tf.expand_dims(self.s1, -1), conf.vocab_size, conf.embed_size, name='embedding', pretrain_embedding=conf.pretrain_emb)
        s1_mask = mask_nonpad_from_embedding(s1_embed)  # [batch,len] 1 for nonpad; 0 for pad
        s1_seqlen = tf.cast(tf.reduce_sum(s1_mask, axis=-1), tf.int32)  # [batch]

        # encoder
        encoder_input = s1_embed
        encoder_input = tf.layers.dropout(encoder_input, rate=self.dropout_rate)  # dropout

        with tf.variable_scope('rnn_1'):
            self.bilstm_encoder1 = Bi_RNN(cell_name='LSTMCell', hidden_size=conf.birnn_hidden_size, dropout_rate=self.dropout_rate)
            encoder_output, _ = self.bilstm_encoder1(encoder_input, s1_seqlen)  # [batch,len,2hid]
        with tf.variable_scope('rnn_2'):
            self.bilstm_encoder2 = Bi_RNN(cell_name='LSTMCell', hidden_size=conf.birnn_hidden_size, dropout_rate=self.dropout_rate)
            encoder_output, _ = self.bilstm_encoder2(encoder_output, s1_seqlen)  # [batch,len,2hid]

        # logits
        cls_logits = tf.layers.dense(encoder_output, conf.label_size, activation=None, use_bias=True, name='cls_logits')  # [batch,length,label]

        # crf
        log_likelihood, transition_params = tf.contrib.crf.crf_log_likelihood(cls_logits, self.ner_label, tf.to_int32(s1_seqlen))
        crf_loss = tf.reduce_mean(-log_likelihood)

        # loss
        self.loss = crf_loss

        # crf decode
        ner_pred, ner_prob = tf.contrib.crf.crf_decode(cls_logits, transition_params, tf.to_int32(s1_seqlen))

        self.ner_prob = tf.identity(ner_prob, name='ner_prob')  # [batch]
        self.ner_pred = tf.identity(ner_pred, name='ner_pred')  # [batch,len]

        with tf.name_scope("accuracy"):
            ner_acc = tf.cast(tf.equal(self.ner_pred, self.ner_label), tf.float32) * s1_mask  # [batch,length]
            ner_acc = tf.reduce_sum(ner_acc, axis=-1)  # [batch]
            ner_acc = ner_acc / tf.cast(s1_seqlen, tf.float32)  # [batch]
            self.accuracy = tf.reduce_mean(ner_acc, axis=0)  # scalar

        self.global_step = tf.train.get_or_create_global_step()
        self.optimizer = tf.train.AdamOptimizer(learning_rate=conf.lr)
        self.train_op = self.optimizer.minimize(self.loss, global_step=self.global_step)

    def build_model1(self):
        # embedding
        # [batch,len,embed]
        # pretrained_word_embeddings = np.load(f'{curr_dir}/pretrain_emb_300.npy')
        pretrained_word_embeddings = None
        s1_embed, _ = embedding(tf.expand_dims(self.s1, -1), conf.vocab_size, conf.embed_size, name='embedding', pretrain_embedding=pretrained_word_embeddings)
        s1_mask = mask_nonpad_from_embedding(s1_embed)  # [batch,len] 1 for nonpad; 0 for pad
        s1_seqlen = tf.cast(tf.reduce_sum(s1_mask, axis=-1), tf.int32)  # [batch]

        # encoder
        encoder_input = s1_embed
        encoder_input = tf.layers.dropout(encoder_input, self.dropout_rate)  # dropout

        idcnn_net = IDCNN()
        encoder_output = idcnn_net(encoder_input)
        encoder_output = tf.layers.dropout(encoder_output, self.dropout_rate)  # dropout

        # logits
        cls_logits = tf.layers.dense(encoder_output, conf.label_size, activation=None, use_bias=True, name='cls_logits')  # [batch,length,label]

        # crf
        log_likelihood, transition_params = tf.contrib.crf.crf_log_likelihood(cls_logits, self.ner_label, tf.to_int32(s1_seqlen))
        crf_loss = tf.reduce_mean(-log_likelihood)

        # loss
        self.loss = crf_loss

        # crf decode
        ner_pred, ner_prob = tf.contrib.crf.crf_decode(cls_logits, transition_params, tf.to_int32(s1_seqlen))

        self.ner_prob = tf.identity(ner_prob, name='ner_prob')  # [batch]
        self.ner_pred = tf.identity(ner_pred, name='ner_pred')  # [batch,len]

        with tf.name_scope("accuracy"):
            ner_acc = tf.cast(tf.equal(self.ner_pred, self.ner_label), tf.float32) * s1_mask  # [batch,len]
            ner_acc = tf.reduce_sum(ner_acc, axis=-1)  # [batch]
            ner_acc = ner_acc / tf.cast(s1_seqlen, tf.float32)  # [batch]
            self.accuracy = tf.reduce_mean(ner_acc, axis=0)  # scalar

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
        # token_ids = utils.pad_sequences([token_ids], padding='post', maxlen=max_word_len)[0]
        return token_ids  # [len]

    @classmethod
    def bmeo2ids(cls, ner_labels, bmeo2id, max_word_len=None):
        # ner_labels 已分好词 ' '隔开
        # 形成batch时才动态补齐长度
        labels = ner_labels.split(' ')
        token_ids = [bmeo2id.get(label, bmeo2id['<unk>']) for label in labels]
        if max_word_len:
            token_ids = token_ids[:max_word_len]
        # token_ids = utils.pad_sequences([token_ids], padding='post', maxlen=max_word_len)[0]
        return token_ids  # [len]

    def create_feed_dict_from_data(self, data, ids, mode='train'):
        # data:数据已经转为id, data不同字段保存该段字段全量数据
        batch_s1 = [data['s1'][i] for i in ids]
        batch_ner_label = [data['ner_label'][i] for i in ids]
        if len(set([len(e) for e in batch_s1])) != 1:  # 长度不等
            batch_s1 = utils.pad_sequences(batch_s1, padding='post')
        if len(set([len(e) for e in batch_ner_label])) != 1:  # 长度不等
            batch_ner_label = utils.pad_sequences(batch_ner_label, padding='post')
        feed_dict = {
            self.s1: batch_s1,
            self.ner_label: batch_ner_label,
        }
        if mode == 'train': feed_dict['num'] = len(batch_s1)
        feed_dict[self.dropout_rate] = conf.dropout_rate if mode == 'train' else 0.
        return feed_dict

    def create_feed_dict_from_features(self, features, mode='train'):
        # feature:tfrecord数据的example, 每个features的不同字段包括该字段一个batch数据
        feed_dict = {
            self.s1: features['s1'],
            self.ner_label: features['ner_label'],
        }
        if mode == 'train': feed_dict['num'] = len(features['s1'])
        feed_dict[self.dropout_rate] = conf.dropout_rate if mode == 'train' else 0.
        return feed_dict

    def create_feed_dict_from_raw(self, batch_s1, batch_ner_label, token2id_dct, mode='infer'):
        char2id = token2id_dct['char2id']
        bmeo2id = token2id_dct['bmeo2id']

        feed_s1 = [self.sent2ids(s1, char2id) for s1 in batch_s1]
        if len(set([len(e) for e in feed_s1])) != 1:  # 长度不等
            feed_s1 = utils.pad_sequences(feed_s1, padding='post')

        feed_dict = {
            self.s1: np.array(feed_s1),
        }
        feed_dict[self.dropout_rate] = conf.dropout_rate if mode == 'train' else 0.

        if mode == 'infer':
            return feed_dict

        if mode in ['train', 'dev']:
            feed_ner_label = [self.bmeo2ids(label, bmeo2id) for label in batch_ner_label]
            if len(set([len(e) for e in feed_ner_label])) != 1:  # 长度不等
                feed_ner_label = utils.pad_sequences(feed_ner_label, padding='post')

            feed_dict[self.ner_label] = feed_ner_label
            return feed_dict

        raise ValueError(f'mode type {mode} not support')

    @classmethod
    def generate_data(cls, file, token2id_dct):
        char2id = token2id_dct['char2id']
        bmeo2id = token2id_dct['bmeo2id']
        data = {
            's1': [],
            'ner_label': []
        }
        with open(file, 'r', encoding='U8') as f:
            for i, line in enumerate(f):
                item = line.strip().split('\t')
                s1 = item[0]
                bmeo = item[1]
                s1_ids = cls.sent2ids(s1, char2id, max_word_len=100)
                bmeo_ids = cls.bmeo2ids(bmeo, bmeo2id, max_word_len=100)
                if i < 5:  # check
                    print(f'check {i}:')
                    print(f'{s1} -> {s1_ids}')
                    print(f'{bmeo} -> {bmeo_ids}')
                data['s1'].append(s1_ids)
                data['ner_label'].append(bmeo_ids)
        data['num_data'] = len(data['s1'])
        return data

    @classmethod
    def generate_tfrecord(cls, file, token2id_dct, tfrecord_file):
        from qiznlp.common.tfrecord_utils import items2tfrecord
        char2id = token2id_dct['char2id']
        bmeo2id = token2id_dct['bmeo2id']

        def items_gen():
            with open(file, 'r', encoding='U8') as f:
                for i, line in enumerate(f):
                    item = line.strip().split('\t')
                    if len(item) != 2:
                        print(repr(line))
                        continue
                    try:
                        s1 = item[0]
                        bmeo = item[1]
                        s1_ids = cls.sent2ids(s1, char2id, max_word_len=100)
                        bmeo_ids = cls.bmeo2ids(bmeo, bmeo2id, max_word_len=100)
                        if i < 5:  # check
                            print(f'check {i}:')
                            print(f'{s1} -> {s1_ids}')
                            print(f'{bmeo} -> {bmeo_ids}')
                        d = {
                            's1': s1_ids,
                            'ner_label': bmeo_ids,
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
            'ner_label': tf.VarLenFeature(tf.int64),
        }
        dataset, count = tfrecord2dataset(tfrecord_file, feat_dct, batch_size=batch_size, auto_pad=True, index=index, shard=shard)
        return dataset, count

    def get_signature_export_model(self):
        inputs_dct = {
            's1': self.s1,
            'dropout_rate': self.dropout_rate,
        }
        outputs_dct = {
            'ner_pred': self.ner_pred,
            'ner_prob': self.ner_prob,
        }
        return inputs_dct, outputs_dct

    @classmethod
    def get_signature_load_pbmodel(cls):
        inputs_lst = ['s1', 'dropout_rate']
        outputs_lst = ['ner_pred', 'ner_prob']
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
        model.ner_prob = graph.get_tensor_by_name('ner_prob:0')
        model.ner_pred = graph.get_tensor_by_name('ner_pred:0')

        saver.restore(sess, ckpt_name)
        print(f':: restore success! {ckpt_name}')
        return model, saver
