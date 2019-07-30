import unittest
import os
import glob
import json
from unittest.mock import patch
from outfit import CloudConn
from outfit import Logger
from consul import Consul

class TestLogger(unittest.TestCase):
    
    def delete_all_log_files(self):
        filelist = glob.glob(os.path.join('tests/logs', '*'))
        for f in filelist:
            os.remove(f) 

    def test_setup_log_json(self):
        self.delete_all_log_files()
        CloudConn.setup('./tests/assets/config-log-json.yaml')
        Logger.info('test_info')
        with open('tests/logs/info.log', 'r') as finfo:
            temp_info = finfo.readlines()
            last_line = temp_info[len(temp_info) - 1]
            self.assertTrue('test_info' in last_line)

        Logger.debug('test_debug')
        with open('tests/logs/debug.log', 'r') as fdebug:
            temp_debug = fdebug.readlines()
            last_line = temp_debug[len(temp_debug) - 1]
            self.assertTrue('test_debug' in last_line)

        Logger.error('test_error')
        with open('tests/logs/errors.log', 'r') as ferrors:
            temp_errors = ferrors.readlines()
            last_line = temp_errors[len(temp_errors) - 1]
            self.assertTrue('test_error' in last_line)

        Logger.critical('test_critical')
        with open('tests/logs/errors.log', 'r') as fcritical:
            temp_critical = fcritical.readlines()
            last_line = temp_critical[len(temp_critical) - 1]
            self.assertTrue('test_critical' in last_line)


    def test_setup_log_yaml(self):
        self.delete_all_log_files()
        CloudConn.setup('./tests/assets/config.yaml')
        Logger.info('test_info')
        with open('tests/logs/info.log', 'r') as finfo:
            temp_info = finfo.readlines()
            last_line = temp_info[len(temp_info) - 1]
            self.assertTrue('test_info' in last_line)

        Logger.debug('test_debug')
        with open('tests/logs/debug.log', 'r') as fdebug:
            temp_debug = fdebug.readlines()
            last_line = temp_debug[len(temp_debug) - 1]
            self.assertTrue('test_debug' in last_line)

        Logger.error('test_error')
        with open('tests/logs/errors.log', 'r') as ferrors:
            temp_errors = ferrors.readlines()
            last_line = temp_errors[len(temp_errors) - 1]
            self.assertTrue('test_error' in last_line)

        Logger.critical('test_critical')
        with open('tests/logs/errors.log', 'r') as fcritical:
            temp_critical = fcritical.readlines()
            last_line = temp_critical[len(temp_critical) - 1]
            self.assertTrue('test_critical' in last_line)
    
    def test_setup_log_py(self):
        self.delete_all_log_files()
        CloudConn.setup('./tests/assets/config-log-py.yaml')
        Logger.info('test_info')
        with open('tests/logs/info.log', 'r') as finfo:
            temp_info = finfo.readlines()
            last_line = temp_info[len(temp_info) - 1]
            self.assertTrue('test_info' in last_line)

        Logger.debug('test_debug')
        with open('tests/logs/debug.log', 'r') as fdebug:
            temp_debug = fdebug.readlines()
            last_line = temp_debug[len(temp_debug) - 1]
            self.assertTrue('test_debug' in last_line)

        Logger.error('test_error')
        with open('tests/logs/errors.log', 'r') as ferrors:
            temp_errors = ferrors.readlines()
            last_line = temp_errors[len(temp_errors) - 1]
            self.assertTrue('test_error' in last_line)

        Logger.critical('test_critical')
        with open('tests/logs/errors.log', 'r') as fcritical:
            temp_critical = fcritical.readlines()
            last_line = temp_critical[len(temp_critical) - 1]
            self.assertTrue('test_critical' in last_line)

    @patch.object(Consul.KV, 'get')
    def test_setup_log_consulkv(self, mock_kv):
        self.delete_all_log_files()
        
        from outfit.utils.io import load_yaml

        mock_kv.return_value = [None, {'Value' : json.dumps(load_yaml('tests/assets/logging.yaml')).encode()}]
        CloudConn.setup('./tests/assets/config-log-kv.yaml')
        
        Logger.info('test_info')
        with open('tests/logs/info.log', 'r') as finfo:
            temp_info = finfo.readlines()
            last_line = temp_info[len(temp_info) - 1]
            self.assertTrue('test_info' in last_line)

        Logger.debug('test_debug')
        with open('tests/logs/debug.log', 'r') as fdebug:
            temp_debug = fdebug.readlines()
            last_line = temp_debug[len(temp_debug) - 1]
            self.assertTrue('test_debug' in last_line)

        Logger.error('test_error')
        with open('tests/logs/errors.log', 'r') as ferrors:
            temp_errors = ferrors.readlines()
            last_line = temp_errors[len(temp_errors) - 1]
            self.assertTrue('test_error' in last_line)

        Logger.critical('test_critical')
        with open('tests/logs/errors.log', 'r') as fcritical:
            temp_critical = fcritical.readlines()
            last_line = temp_critical[len(temp_critical) - 1]
            self.assertTrue('test_critical' in last_line)

if __name__ == '__main__':
    unittest.main()
