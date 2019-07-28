import unittest
import yaml
import os
import consul
from hvac.v1 import Client
from hvac.api.secrets_engines.kv import Kv
from hvac.adapters import Adapter
from hvac.api.secrets_engines import kv_v1 
from unittest import mock
from unittest.mock import MagicMock, patch
from pycloud.hashicorp.consul_config import ConsulCon
from pycloud.hashicorp.vault_config import VaultCon
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

        self.vault_cons_params = self.normal_content['vault']
        self.vault_data_key = {
            'password' : 'secrets123'
        }
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
    
    #@patch.object(Kv,'kv')
    @patch.object(kv_v1.KvV1,'read_secret' )
    @patch.object(VaultCon, '_construct_data_vault')
    def test_vault_init(self,mock_kv, mock_vault_con):
        #with patch.object(VaultCon, '_construct_data_vault', return_value= self.kv_sample) as mock_VauleCon:
        mock_vault_con.return_value = {'data' : {'password' : 'secrets123'}}
        mock_kv.return_value = {'password' : 'secrets123'}
        con = VaultCon(self.normal_content)
        result = con.get_secret_kv()
        self.assertEqual(result['password'], 'secrets123', 'the vault client is None')

    def test_vault_get_kv(self):
        pass

        

if __name__=='__main__':
    unittest.main()
