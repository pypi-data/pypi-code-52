# -*- coding: utf-8 -*-
import sys
import tensorflow as tf
import tensorflow_datasets as tfds
from skydl.datasets.super_tf_dataset_builder import SuperDatasetBuilder
from skydl.models.train_phase_enum import TrainPhaseEnum
from skydl.models.tf_keras_modelv2 import TfKerasModelV2
from py_common_util.common.annotations import print_exec_time


class MnistTfKerasModelV2(TfKerasModelV2):
    """
    实现卷积神经网络CNN对MNIST数字分类
    """
    def adjust_parse_args_value(self):
        super().adjust_parse_args_value()
        self.parser_args.data_path = sys.path[0] + '/../../datasets'
        self.parser_args.use_cuda = True
        self.parser_args.init_from_saver = False
        self.parser_args.fit_initial_epoch = 0
        self.parser_args.train_phase = TrainPhaseEnum.Train.value
        self.parser_args.model_version = '20191125003'
        self.parser_args.epochs = 1
        self.parser_args.batch_size = 128
        self.parser_args.log_interval = 1000

    @print_exec_time
    def load_data(self, *args, **kwargs):
        super().load_data(*args, **kwargs)
        def map_fn_feature_label(feature, label):
            feature = feature / 255
            feature = tf.squeeze(feature)
            return feature, label
        dateset_name = "mnist"
        train_data = SuperDatasetBuilder.load_batched_datasets(dateset_name,
                                                                map_fn_feature_label=map_fn_feature_label,
                                                                split=[tfds.Split.TRAIN],
                                                                batch_size=self.parser_args.batch_size,
                                                                epochs=self.parser_args.epochs)
        test_data = SuperDatasetBuilder.load_batched_datasets(dateset_name,
                                                               map_fn_feature_label=map_fn_feature_label,
                                                               split=[tfds.Split.TEST],
                                                               batch_size=SuperDatasetBuilder.get_num_examples(
                                                                   dateset_name, tfds.Split.TEST))
        return train_data, test_data, SuperDatasetBuilder.get_info(dateset_name)

    def fit(self, *args, **kwargs):
        if not self.is_training_phase():
            return self
        # TODO restore mode from lastest checkpoint
        # 参考：https://github.com/tensorflow/tensorflow/issues/27909
        if self.parser_args.init_from_saver:
            checkpoint = tf.train.get_checkpoint_state(self.get_model_checkpoint_dir(), latest_filename=self.latest_model_filename)
            if checkpoint and checkpoint.saved_model_path:
                # saver.restore(sess, checkpoint.saved_model_path)
                self.log.info("Restored and Init Session Variables from Saver......")
            else:
                self.log.info(
                    "*** Error Occurred in " + self.parser_args.train_phase + " phase(1), Can not find the model file: "
                    + self.get_model_checkpoint_dir() + "/" + self.latest_model_filename)
                self.log.info("And you can ignore this error, then the trainning will go on......")

        # load dataset
        train_dataset, test_dataset, _ = self.load_data()
        self.model.fit(train_dataset, epochs=self.parser_args.epochs, callbacks=self._fit_callbacks())
        self.model.summary()

        # test mode
        self.evaluate(evaluate_dataset=test_dataset)
        return self

    def evaluate(self, *args, **kwargs):
        evaluate_dataset = kwargs.get("evaluate_dataset")
        if evaluate_dataset:
            _, evaluate_dataset, _ = self.load_data()

        # test mode
        test_loss, test_acc = self.model.evaluate(evaluate_dataset)
        self.model.summary()
        print('\nTest accuracy:', test_acc)
        return self

    def serving(self, *args, **kwargs):
        # restore weights from latest checkpoint
        latest_checkpoint = tf.train.latest_checkpoint(self.get_model_checkpoint_dir())
        if latest_checkpoint:
            self.model.load_weights(latest_checkpoint)
        saved_serving_path = self.parser_args.saved_model_path + "/serving/models/" + self.model.name() + "/" + self.parser_args.model_version
        _, evaluate_dataset, _ = self.load_data()

        # prediction mode
        for batched_examples in tfds.as_numpy(evaluate_dataset.take(1)):
            test_batched_features, test_batched_labels = batched_examples
        # predictions = self.model.predict(test_batched_features)
        # print("serving predict, real:", np.argmax(predictions[0]), test_batched_labels[0])

        # save model for tf serving
        if not self.model.inputs:
            self.model._set_inputs(test_batched_features)
        tf.saved_model.save(self.model, saved_serving_path)
        return self