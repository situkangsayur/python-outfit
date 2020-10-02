import unittest

import flask
from healthcheck import HealthCheck
from outfit.utils.db_status import MongoLib
from outfit.utils.healtchcheck import HealthcheckList
from outfit.utils.logger import Logger


class BasicHealthCheckTest(unittest.TestCase):

    def setUp(self):
        self.path = '/healthcheck'
        self.path2 = '/healthcheck_200'
        self.app = flask.Flask(__name__)
        self.app2 = flask.Flask(__name__)

        self.hc = HealthCheck()
        self.hc2 = HealthCheck()

        self.client = self.app.test_client()
        self.client2 = self.app2.test_client()
        dbmongo = None
        service_enum = {
            'mongoengine': {
                'connection': dbmongo,
                'lib_list': [MongoLib.MONGOENGINE]
            }
        }
        
        self.hc = HealthcheckList.setup(healthcheck = self.hc, service_list = service_enum)

        self.app.add_url_rule(self.path, view_func=lambda: self.hc.run())
        self.app2.add_url_rule(self.path2, view_func=lambda: self.hc2.run())



    def test_basic_check_success(self):
        response = self.client2.get(self.path2)
        self.assertEqual(200, response.status_code)


    def test_basic_check(self):
        response = self.client.get(self.path2)
        Logger.info(response)
        self.assertEqual(404, response.status_code)

    def test_failing_check(self):
        def fail_check():
            return False, "FAIL"

        self.hc2.add_check(fail_check)
        response = self.client2.get(self.path2)
        self.assertEqual(500, response.status_code)

        respon = flask.json.loads(response.data)
        self.assertEqual("failure", respon["status"])

if __name__ == '__main__':
    unittest.main()

