import yaml
import logging.config
import logging

modules = ['development', 'production']

class Logger(object):
    mode = 'development'
    info = logging.getLogger(mode).info
    debug = logging.getLogger(mode).debug
    error = logging.getLogger(mode).error

    @staticmethod
    def load_config_from_yaml_file(self, mode, dir):
        with open(dir, 'rt') as f:
            log_config = yaml.safe_load(f.read())
        logging.config.dictConfig(log_config)
        
        loggers = [name for name in logging.root.manager.loggerDict]
        return loggers

        
    @staticmethod
    def load_config_from_consulkv(self, mode, source_location = None, consul_con = None):

        from ..hashicorp.consul_config import ConsulCon

        consul_con = ConsulCon() if consul_con == None else consul_con

        config = consul_con.get_kv()

        logging.config.dictConfig(log_config)

        loggers = [name for name in logging.root.manager.loggerDict]
        return loggers
 

    @staticmethod
    def load_config_from_dict(self, mode, config_dict):
        logging.config.dictConfig(log_config)

        loggers = [name for name in logging.root.manager.loggerDict]
        return loggers

    @staticmethod
    def load_config_from_json_file(self, mode, dir):

        import json
        with open(dir, 'rt') as f:
            log_config = json.loads(f.read())
        logging.config.dictConfig(log_config)

        loggers = [name for name in logging.root.manager.loggerDict]
        return loggers


    @staticmethod
    def setup_log(self, mode = None, source_type = None, 
                  source_location = None, consul_con = None, config_dict = None):
        mode_enum = {
            'yaml_file' : lambda x, y : self.load_config_from_file(x, y),
            'consulkv' : lambda x, y : self.load_config_from_consulkv(x, y),
            'dictionary' : lambda x, y : self.load_config_from_dict(x, y),
            'json_file' : lambda x, y : self.load_config_from_json_file(x, y)
        }

        logger = mode_enum[mode](mode, source_location, consul_con)

        if mode not in logger:
            raise Exception('modules for mode '+ mode +' is not found!!')
        else:
            self.mode = mode
 
