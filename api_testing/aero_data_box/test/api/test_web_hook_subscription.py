import unittest
import logging
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.flight_alert_push_api import APIFlightAlertPUSH
from api_testing.aero_data_box.infra.api.logging_basicConfig import LoggingSetup

class TestAPIGetWebHookSubscriptions(unittest.TestCase):

    def setUp(self):
        self.config = ConfigProvider.load_from_file()
        self.api_request = APIFlightAlertPUSH(APIWrapper())

    def test_web_hook_subscription(self):
        """
        Testing the API of getting information about existing web-hook subscription
        """
        logging.info("______________")
        logging.info("Starting the 'Get webhook subscription' test")

        response = self.api_request.get_web_hook_subscription()
        response_data = response.json()

        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data["subscriber"]["id"], self.config["subscriber"]["id"])

        logging.info("Test ended successfully")

if __name__ == '__main__':
    unittest.main()