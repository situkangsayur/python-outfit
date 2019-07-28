import unittest
import yaml
import os
import consul
from unittest import mock
from unittest.mock import MagicMock
from pycloud.hashicorp.consul_config import ConsulCon
from pycloud.hashicorp.hashicorp_base import ConnBase


class TestHashicorp(unittest.TestCase):

    def setUp(self):
       
        curr_dir = os.path.dirname(__file__)
        file_path = 'assets/config.yaml'
        self.normal_content = None
        # get the yaml file
        with open(os.path.join(curr_dir,file_path), 'r') as stream:
            try:
                self.normal_content = yaml.load(stream)
            except yaml.YAMLError as err:
                print('error load yaml file ' + str(err))

        self.kv_sample = {
            'db' : {
                'username' : 'root',
                'host' : 'localhost',
                'port' : 1234
            },
            'elasticsearch' : {
                'host' : 'localhost',
                'port' : 9200
            }
        }

    def test_consul_init(self):
        con = ConsulCon(self.normal_content)
        self.assertNotEqual(con.cons, None, 'the con is None')
    
    def test_get_config_dict(self):
        con = ConnBase()
        result = con.get_configs_dict(self.normal_content['consul'], list('path'))
        self.assertEqual(result['host'], 'localhost', 'the value of sample consul config is not equal')

    def test_consul_get_kv(self):
        con = ConsulCon(self.normal_content)
        con.get_kv = MagicMock(return_value = self.kv_sample)
        result = con.get_kv()
        self.assertEqual(result['db']['host'], 'localhost', 'the db host value is not equal')

    def test_vault_init(self):
        pass

    def test_vault_get_kv(self):
        pass


if __name__=='__main__':
    unittest.main()
