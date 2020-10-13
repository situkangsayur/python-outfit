import unittest
import os
import glob
import json
import yaml
from unittest.mock import patch, mock_open, builtins
from outfit import Outfit 
from outfit import Logger
from outfit import merge_dict
from consul import Consul
from outfit.hashicorp.consul_config import ConsulCon
from outfit.utils.io import convert_yaml
from .assets.logging_b import logging_b
from .assets.logging import logging

class TestLogger(unittest.TestCase):

    def setUp(self):
        if not os.path.exists('tests/test_logs'):
            os.mkdir('tests/test_logs')

        curr_dir = os.path.dirname(__file__)
        file_path = 'assets/logging.yaml'
        # get the yaml file
        with open(os.path.join(curr_dir,file_path), 'r') as stream:
            try:
                self.normal_content = yaml.safe_load(stream)
            except yaml.YAMLError as err:
                Logger.error('error load yaml file ' + str(err))


            
    def test_setup_log_json(self):
        self.delete_all_log_files()
        Outfit.setup('./tests/assets/config-log-json.yaml')
        Logger.info('test_info')
        with open('tests/test_logs/info.log', 'r') as finfo:
            temp_info = finfo.readlines()
            last_line = temp_info[len(temp_info) - 1]
            self.assertTrue('test_info' in last_line)

        Logger.debug('test_debug')
        with open('tests/test_logs/debug.log', 'r') as fdebug:
            temp_debug = fdebug.readlines()
            last_line = temp_debug[len(temp_debug) - 1]
            self.assertTrue('test_debug' in last_line)

        Logger.error('test_error')
        with open('tests/test_logs/errors.log', 'r') as ferrors:
            temp_errors = ferrors.readlines()
            last_line = temp_errors[len(temp_errors) - 1]
            self.assertTrue('test_error' in last_line)

        Logger.critical('test_critical')
        with open('tests/test_logs/errors.log', 'r') as fcritical:
            temp_critical = fcritical.readlines()
            last_line = temp_critical[len(temp_critical) - 1]
            self.assertTrue('test_critical' in last_line)


    def test_setup_log_yaml(self):
        self.delete_all_log_files()
        Outfit.setup('./tests/assets/config.yaml')
        Logger.info('test_info')
        with open('tests/test_logs/info.log', 'r') as finfo:
            temp_info = finfo.readlines()
            last_line = temp_info[len(temp_info) - 1]
            self.assertTrue('test_info' in last_line)

        Logger.debug('test_debug')
        with open('tests/test_logs/debug.log', 'r') as fdebug:
            temp_debug = fdebug.readlines()
            last_line = temp_debug[len(temp_debug) - 1]
            self.assertTrue('test_debug' in last_line)

        Logger.error('test_error')
        with open('tests/test_logs/errors.log', 'r') as ferrors:
            temp_errors = ferrors.readlines()
            last_line = temp_errors[len(temp_errors) - 1]
            self.assertTrue('test_error' in last_line)

        Logger.critical('test_critical')
        with open('tests/test_logs/errors.log', 'r') as fcritical:
            temp_critical = fcritical.readlines()
            last_line = temp_critical[len(temp_critical) - 1]
            self.assertTrue('test_critical' in last_line)
    
    def test_setup_log_py(self):
        self.delete_all_log_files()
        Outfit.setup('./tests/assets/config-log-py.yaml')
        Logger.info('test_info')
        with open('tests/test_logs/info.log', 'r') as finfo:
            temp_info = finfo.readlines()
            last_line = temp_info[len(temp_info) - 1]
            self.assertTrue('test_info' in last_line)

        Logger.debug('test_debug')
        with open('tests/test_logs/debug.log', 'r') as fdebug:
            temp_debug = fdebug.readlines()
            last_line = temp_debug[len(temp_debug) - 1]
            self.assertTrue('test_debug' in last_line)

        Logger.error('test_error')
        with open('tests/test_logs/errors.log', 'r') as ferrors:
            temp_errors = ferrors.readlines()
            last_line = temp_errors[len(temp_errors) - 1]
            self.assertTrue('test_error' in last_line)

        Logger.critical('test_critical')
        with open('tests/test_logs/errors.log', 'r') as fcritical:
            temp_critical = fcritical.readlines()
            last_line = temp_critical[len(temp_critical) - 1]
            self.assertTrue('test_critical' in last_line)
    
    @patch.object(ConsulCon, 'get_kv')
    def test_setup_log_consulkv(self, mock_kv):
        self.delete_all_log_files()
        
        from outfit.utils.io import load_yaml
        mock_kv.return_value =  logging

        #result = convert_yaml(self.normal_content)

        Outfit.setup('./tests/assets/config-log-kv.yaml')
       
        m = minfo = mock_open(read_data='INFO:test_utilslogger.py(50)> test_info')
        mdebug = mock_open(read_data = 'ERROR:test_utilslogger.py(62)> test_debug')
        merror = mock_open(read_data = 'ERROR:test_utilslogger.py(62)> test_error')
        mcritical = mock_open(read_data = 'ERROR:test_utilslogger.py(62)> test_critical')
        m.side_effect = [minfo.return_value, mdebug.return_value, merror.return_value, mcritical.return_value]

        with patch('builtins.open', m):
            
            Logger.info('test_info')
            with open('tests/test_logs/info.log', 'r') as finfo:
                temp_info = finfo.read()
                last_line = temp_info[len(temp_info) - 1]
                self.assertTrue('test_info' in temp_info)

            Logger.debug('test_debug')
            with open('tests/test_logs/debug.log', 'r') as fdebug:
                temp_debug = fdebug.readlines()
                last_line = temp_debug[len(temp_debug) - 1]
                self.assertTrue('test_debug' in last_line)

            Logger.error('test_error')
            with open('tests/test_logs/errors.log', 'r') as ferrors:
                temp_errors = ferrors.readlines()
                last_line = temp_errors[len(temp_errors) - 1]
                self.assertTrue('test_error' in last_line)

            Logger.critical('test_critical')
            with open('tests/test_logs/errors.log', 'r') as fcritical:
                temp_critical = fcritical.readlines()
                last_line = temp_critical[len(temp_critical) - 1]
                self.assertTrue('test_critical' in last_line)

    @patch.object(ConsulCon, 'get_kv')
    def test_setup_log_consulkv_failed(self, mock_kv):
        self.delete_all_log_files()
        
        from outfit.utils.io import load_yaml
        mock_kv.return_value =  logging

        Outfit.setup('./tests/assets/config-log-kv.yaml')
        
        Logger.info('test_info')
        with open('tests/test_logs/info.log', 'r') as finfo:
            temp_info = finfo.readlines()
            print(temp_info)
            print(len(temp_info))
            last_line = temp_info[len(temp_info) - 1]
            self.assertTrue('test_info' in last_line)

        Logger.debug('test_debug')
        with open('tests/test_logs/debug.log', 'r') as fdebug:
            temp_debug = fdebug.readlines()
            last_line = temp_debug[len(temp_debug) - 1]
            self.assertTrue('test_debug' in last_line)

        Logger.error('test_error')
        with open('tests/test_logs/errors.log', 'r') as ferrors:
            temp_errors = ferrors.readlines()
            last_line = temp_errors[len(temp_errors) - 1]
            self.assertTrue('test_error' in last_line)

        Logger.critical('test_critical')
        with open('tests/test_logs/errors.log', 'r') as fcritical:
            temp_critical = fcritical.readlines()
            last_line = temp_critical[len(temp_critical) - 1]
            self.assertTrue('test_critical' in last_line)

    def delete_all_log_files(self):
        filelist = glob.glob(os.path.join('tests/test_logs', '*'))
        for f in filelist:
            os.remove(f) 


if __name__ == '__main__':
    unittest.main()
