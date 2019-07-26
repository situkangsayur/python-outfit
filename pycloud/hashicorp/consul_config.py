#import conf.bootstrap as config
#import conf.datakey as datakey
from .hashicorp_base import ConnBase
import consul
import os
import json

class ConsulCon(ConnBase):
    """Class to construct the dict properties for the app from Consul and Vault
    """

    exception_key = ['host_vault','scheme_vault', 'port_vault', 'path_vault']
    exception_dict = {}

    def __init__(self):
        """Constructor inisiating all properties
        """
        consul_params = {}
        
        # construct the consul and vault params
        consul_params = get_configs_dict(config.consul)

        # construct the consul
        self.cons = consul.Consul(**consul_params)
   
    def get_kv(self):
        """run config constructor return dict all configs
        """
        temp = self.cons.kv.get(self.exception_dict['path_consul'])[1]['Value']
        result = json.loads(temp.decode('utf-8')) if temp else ''
        return result

