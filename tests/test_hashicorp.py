import unittest
import yaml
import os
from unittest import mock

class TestHashicorp(unittest.TestCase):

    def setUp(self):
       
        curr_dir = os.path.dirname(__file__)
        file_path = 'assets/config.yaml'
        content = None
        # get the yaml file
        with open(os.path.join(curr_dir,file_path), 'r') as stream:
            try:
                content = yaml.load(stream)
            except yaml.YAMLError as err:
                print('error load yaml file ' + str(err))
            print(content)

    def test_get_config_dict(self):
        self.assertTrue(False)

    def test_consul_init(self):
        pass

    def test_consul_get_kv(self):
        pass

    def test_vault_init(self):
        pass

    def test_vault_get_kv(self):
        pass


if __name__=='__main__':
    unittest.main()
