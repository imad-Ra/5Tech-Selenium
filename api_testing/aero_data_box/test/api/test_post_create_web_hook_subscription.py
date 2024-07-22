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
        Tests creating a web hook subscription by calling the API and validating the response.
        """
        payload = {"url": "https://webhook.site/687a0369-61ab-4be8-97d4-feef4d326fa2"}

        response = self.api_request.post_create_web_hook_subscription(payload)
        response_data = response.json()
        print(response_data)

        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response_data, dict)  # Changed from list to dict
        self.assertEqual(response_data["subscriber"]["id"], self.config["subscriber"]["id"])

