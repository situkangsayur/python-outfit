import yaml
import logging.config
import logging
from .io import load_yaml 

modules = ['development', 'production']

class Logger(object):
    mode = 'development'
    info = logging.getLogger(mode).info
    debug = logging.getLogger(mode).debug
    error = logging.getLogger(mode).error

    @staticmethod
    def load_config_from_yaml_file(self, source_location):
        log_config = load_yaml(source_location)
        logging.config.dictConfig(log_config)
        
        loggers = [name for name in logging.root.manager.loggerDict]
        return loggers

        
    @staticmethod
    def load_config_from_consulkv(self, source_location = None, consul_con = None):

        from ..hashicorp.consul_config import ConsulCon

        consul_con = ConsulCon() if consul_con == None else consul_con

        config = consul_con.get_kv()

        logging.config.dictConfig(log_config)

        loggers = [name for name in logging.root.manager.loggerDict]
        return loggers
 

    @staticmethod
    def load_config_from_dict(self, config_dict):
        logging.config.dictConfig(log_config)

        loggers = [name for name in logging.root.manager.loggerDict]
        return loggers

    @staticmethod
    def load_config_from_json_file(self, source_location):

        import json
        with open(source_location, 'rt') as f:
            log_config = json.loads(f.read())
        logging.config.dictConfig(log_config)

        loggers = [name for name in logging.root.manager.loggerDict]
        return loggers


    @staticmethod
    def setup_log(self, mode = 'development', source_type = None, 
                  source_location = None, consul_con = None, config_dict = None):
        mode_enum = {
            'yaml_file' : lambda x, y, z: self.load_config_from_file(xy),
            'consulkv' : lambda x, y, z : self.load_config_from_consulkv(x, y),
            'dictionary' : lambda x, y, z : self.load_config_from_dict(z),
            'json_file' : lambda x, y, z : self.load_config_from_json_file(x)
        }

        logger = mode_enum[source_type](source_location, consul_con, config_dict)

        if mode not in logger:
            raise Exception('modules for mode '+ mode +' is not found!!')
        else:
            self.mode = mode
 
