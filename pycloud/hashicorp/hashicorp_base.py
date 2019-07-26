from abc import ABC

class ConnBase(ABC):

    def get_configs_dict(source, exception_key):
            """Constructing consul/vault properties from bootstrap.py return list of configs

            it will checking if the property is in exception_key list

            Keyword arguments:
            source -- The dict of vault/consul property from config file .py
            """

            params = {}

            # iterate source items
            for k,v in source.items():
                if '$' == v[0]:

                    # checking if the string of value is in environment variables
                    temp = os.environ[v[1:]] if v[1:] in os.environ else None

                    # checking if the string of value is in exception keys
                    if v[1:] not in exception_key:
                        # set the real value to params[k]
                        # if temp value is digit then convert to integer
                        params[k] = int(temp) if temp.isdigit() else temp
                    else:
                        # if the string of value is in exception keys
                        # assing the temp value (real value) to exception_dict for index v[1:]
                        self.exception_dict[v[1:]] =int(temp) if temp.isdigit() else temp
                else:
                    param[k] = v

            return params
