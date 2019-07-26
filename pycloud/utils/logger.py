import yaml
import logging.config
import logging

modules = ['development', 'production']

def setup_logging(mode):
    log_path = 'conf/logging.yaml'
    with open(log_path, 'rt') as f:
        log_config = yaml.safe_load(f.read())
    logging.config.dictConfig(log_config)
   
    if mode not in modules:
        raise Exception('modules for mode '+ mode +' is not found!!')
    else:
        Logger.mode = mode 

class Logger(object):
    mode = 'development'
    info = logging.getLogger(mode).info
    debug = logging.getLogger(mode).debug
    error = logging.getLogger(mode).error

