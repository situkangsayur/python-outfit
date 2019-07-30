import unittest

import flask
from healthcheck import HealthCheck
from pycloud.utils.db_status import MongoLib
from pycloud.utils.healtchcheck import HealthcheckList
from pycloud.utils.logger import Logger


class BasicHealthCheckTest(unittest.TestCase):

    def setUp(self):
        self.path = '/healtcheck'
        self.app = flask.Flask(__name__)
        self.hc = HealthCheck()
        self.client = self.app.test_client()
        dbmongo = None
        service_enum = {
            'mongoengine': {
                'connection': dbmongo,
                'lib_list': [MongoLib.MONGOENGINE]
            }
        }
        
        self.hc = HealthcheckList.setup(healthcheck = self.hc, service_list = service_enum)
        self.app.add_url_rule(self.path, view_func=lambda: self.hc.run())


    def test_basic_check(self):
        response = self.client.get(self.path)
        Logger.info(response)
        self.assertEqual(200, response.status_code)

    def test_failing_check(self):
        def fail_check():
            return False, "FAIL"

        self.hc.add_check(fail_check)
        response = self.client.get(self.path)
        self.assertEqual(500, response.status_code)

        respon = flask.json.loads(response.data)
        self.assertEqual("failure", respon["status"])


if __name__ == '__main__':
    unittest.main()

