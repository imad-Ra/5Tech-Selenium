import unittest
from api_testing.aero_data_box.logic.api.flight_alert_push_api import APIFlightAlertPUSH
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider

class TestPostCreateWebHookSubscription(unittest.TestCase):

    def setUp(self):
        # Arrange
        self.config = ConfigProvider.load_from_file()
        self.api_request = APIFlightAlertPUSH(APIWrapper())

    def test_post_create_web_hook_subscription(self):
        payload = {"url": "https://webhook.site/687a0369-61ab-4be8-97d4-feef4d326fa2"}

        # Act
        # Call the method under test
        response = self.api_request.post_create_web_hook_subscription(payload)

        # Assert
        self.assertTrue(response.ok, f"Request failed with status code {response.status_code}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["subscriber"]["id"], self.config["subscriber"]["id"])

if __name__ == "__main__":
    unittest.main()
