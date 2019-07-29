import logging
from .utils.logger import Logger
from .utils.io import load_yaml

class CloudConn(object):
    
    path = None 
    content = None
    
    def __init__(self):
        pass
    @staticmethod
    def setup(path):
        CloudConn.content = load_yaml(path)
        print(CloudConn.content)
        log_config = CloudConn.content['logconfig'] if 'logconfig' in CloudConn.content else None

        if log_config != None:
            mode = log_config['mode'] if 'mode' in log_config else 'root'
            source_type = log_config['source_type'] if 'source_type' in log_config else None
            source_location = log_config['source_location'] if 'source_location' in log_config else None
            if source_type == 'yaml_file':
                Logger.setup_log(mode = mode, source_type = yaml, source_location = source_location)
        else:
            Logger.mode = 'root'
