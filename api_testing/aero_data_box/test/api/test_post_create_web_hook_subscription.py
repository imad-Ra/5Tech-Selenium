import unittest

from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.flight_alert_push_api import APIFlightAlertPUSH


class TestPostCreateWebHookSubscription(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.config = ConfigProvider.load_from_file()
        print(f"Config loaded!")
        self.api_request = APIFlightAlertPUSH(APIWrapper())

    def test_post_create_web_hook_subscription(self):
        """
        Tests the shuffling of the deck by calling the API and validating the response.
        """
        response = self.api_request.post_create_web_hook_subscription()
        flight_status_date = response.json()
        print(flight_status_date)

        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(flight_status_date[0]["aircraft"]["model"], self.config["aircraft-models"]["0"])
