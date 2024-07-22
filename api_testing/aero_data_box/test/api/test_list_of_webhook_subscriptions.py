import json
import unittest

from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.flight_alert_push_api import APIFlightAlertPUSH


class TestAPIListOfWebHookSubscriptions(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.config = ConfigProvider.load_from_file()
        print(f"Config loaded!")
        self.api_request = APIFlightAlertPUSH(APIWrapper())

    def test_list_of_webhook_subscriptions(self):
        """
        Tests the API of getting the list of existing active web-hook subscription
        """
        response = self.api_request.get_list_of_webhook_subscriptions()
        response_data = response.json()
        print(response_data)



        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        # Check if response is a list
        self.assertIsInstance(response_data, list)
        # Check if first item has 'id' key
        self.assertIn('id', response_data[0])


