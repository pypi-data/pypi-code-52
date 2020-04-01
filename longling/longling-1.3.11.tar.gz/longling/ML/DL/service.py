# coding: utf-8
# 2020/1/7 @ tongshiwei


class ServiceModule(object):
    def __init__(self, cfg=None, **kwargs):
        cfg = self.config(cfg, **kwargs)
        self.mod = self.get_module(cfg)

        self.bp_loss_f = None
        self.loss_function = None

    @staticmethod
    def get_configuration_cls():
        raise NotImplementedError

    @staticmethod
    def get_module_cls():
        raise NotImplementedError

    @classmethod
    def config(cls, cfg=None, **kwargs):
        """
        配置初始化

        Parameters
        ----------
        cfg: Configuration, str or None
            默认为 None，不为None时，将使用cfg指定的参数配置
            或路径指定的参数配置作为模型参数
        kwargs
            参数配置可选参数
        """
        configuration_cls = cls.get_configuration_cls()

        cfg = configuration_cls(
            **kwargs
        ) if cfg is None else cfg
        if not isinstance(cfg, configuration_cls):
            cfg = configuration_cls.load_cfg(cfg, **kwargs)
        cfg.dump(override=True)
        return cfg

    @classmethod
    def get_module(cls, cfg):
        """
        根据配置，生成模型模块

        Parameters
        ----------
        cfg: Configuration
            模型配置参数
        Returns
        -------
        mod: Module
            模型模块
        """
        module_cls = cls.get_module_cls()

        mod = module_cls(cfg)
        mod.logger.info(str(mod))
        filename = mod.cfg.cfg_path
        mod.logger.info("parameters saved to %s" % filename)
        return mod


class CliServiceModule(ServiceModule):

    @staticmethod
    def get_configuration_cls():
        raise NotImplementedError

    @staticmethod
    def get_module_cls():
        raise NotImplementedError

    @staticmethod
    def get_configuration_parser_cls():
        raise NotImplementedError

    @classmethod
    def cli_commands(cls):
        raise NotImplementedError

    @classmethod
    def get_parser(cls):
        configuration_parser_cls = cls.get_configuration_parser_cls()
        configuration_cls = cls.get_configuration_cls()

        cfg_parser = configuration_parser_cls(
            configuration_cls,
            commands=cls.cli_commands()
        )
        return cfg_parser

    @classmethod
    def run(cls, parse_args=None):
        cfg_parser = cls.get_parser()
        cfg_kwargs = cfg_parser(parse_args)

        if "subcommand" not in cfg_kwargs:
            cfg_parser.print_help()
            return
        subcommand = cfg_kwargs["subcommand"]
        del cfg_kwargs["subcommand"]

        eval("%s.%s" % (cls.__name__, subcommand))(**cfg_kwargs)
