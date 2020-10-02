import unittest
import yaml
import os
import json
from consul import Consul
from hvac.api.secrets_engines import kv_v1 
from unittest import mock 
from unittest.mock import MagicMock, patch
from outfit import ConsulCon
from outfit import VaultCon
from outfit.hashicorp.hashicorp_base import ConnBase
from outfit import Outfit
from outfit import Logger
from outfit import merge_dict
from .assets.sample_respon_secret import secret_kv

class TestHashicorp(unittest.TestCase):

    def setUp(self):
       
        curr_dir = os.path.dirname(__file__)
        file_path = 'assets/config.yaml'
        # get the yaml file
        with open(os.path.join(curr_dir,file_path), 'r') as stream:
            try:
                self.normal_content = yaml.safe_load(stream)
            except yaml.YAMLError as err:
                Logger.error('error load yaml file ' + str(err))

        self.vault_data_key = {
            'db' : {
                'password' : '-'
            }
        }
        self.kv_sample = {
            'appmode' : 'development',
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
        Outfit.setup(path = 'tests/assets/config.yaml')
        os.environ['host_vault']= 'localhost'
        os.environ['port_vault']= '12345'
        os.environ['scheme_vault']= 'http' 
        os.environ['token_vault']= 'qwerty123'
        os.environ['path_vault']= 'application'

        os.environ['host_consul']= 'localhost'
        os.environ['port_consul']= '12345'
        os.environ['scheme_consul']= 'http' 
        os.environ['token_consul']= 'qwerty123'
        os.environ['path_consul']= 'application'

        os.environ['LOG_MODE']= 'development'
        os.environ['LOG_LOCATION']= './tests/assets/logging.yaml'
        os.environ['LOG_TYPE']= 'yaml_file' 
        os.environ['DEFAULT_TYPE']= 'yaml_file'
        os.environ['DEFAULT_LOCATION']= './tests/assets/logging.yaml' 


    def test_consul_init(self):
        con = ConsulCon()
        self.assertNotEqual(con.cons, None, 'the con is None')
    
    def test_get_config_dict(self):
        con = ConnBase()
        result = con.get_configs_dict(self.normal_content['consul'], list('path'))
        self.assertEqual(result['host'], 'localhost', 'the value of sample consul config is not equal')

    def test_consul_get_kv(self):
        con = ConsulCon()
        con.get_kv = MagicMock(return_value = self.kv_sample)
        result = con.get_kv()
        self.assertEqual(result['db']['host'], 'localhost', 'the db host value is not equal')

    @patch.object(kv_v1.KvV1,'read_secret' )
    def test_vault_init(self,mock_kv):
        #mock_vault_con.return_value = {'data' : secret_kv}
        mock_kv.return_value = {'data' : secret_kv}
        con = VaultCon()
        result = con.get_secret_kv()
        self.assertEqual(result['big_query']['client_id'], '1234567', 'the vault result is not match')
    
    @patch.object(kv_v1.KvV1,'read_secret' )
    def test_construct_data_vault(self, mock_kv):
        mock_kv.return_value = {'data' : secret_kv}
        con = VaultCon()
        result = con.get_secret_kv()

        self.assertEqual(result['big_query']['client_id'], '1234567', 'the vault result is not match')

    @patch.object(kv_v1.KvV1, 'read_secret')
    @patch.object(Consul.KV, 'get')
    def test_env_var(self, mock_consul_kv, mock_vault_kv):
        mock_consul_kv.return_value = [None, { 'Value' : json.dumps(self.kv_sample).encode()}]
        mock_vault_kv.return_value = {'data' : secret_kv}

        Outfit.setup('tests/assets/config-env.yaml')
        vault = VaultCon()
        consul = ConsulCon()

        result_vault = vault.get_secret_kv()
        result_consul = consul.get_kv()

        result = merge_dict(result_vault, result_consul)

        self.assertEqual(result['big_query']['client_id'], '1234567', ' client id from vault not match')
        self.assertEqual(result['appmode'], 'development', ' appmode from consul not match')

        

if __name__=='__main__':
    unittest.main()
