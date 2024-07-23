import unittest
import logging
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.flight_alert_push_api import APIFlightAlertPUSH

class TestPatchRefreshWebHookSubscription(unittest.TestCase):

    def setUp(self):
        #Arrange
        self.config = ConfigProvider.load_from_file()
        self.api_request = APIFlightAlertPUSH(APIWrapper())

    def test_patch_refresh_web_hook_subscription(self):
        """
        Tests the API endpoint for patching and refreshing webhook subscription.

        Note: This test may return a 400 status code with a specific message if the subscription cannot be extended yet.
        Expected error response:
        {
            "message": "Extending this subscription beyond 2024-09-21 07:07:15 UTC is not allowed yet. Please try again later."
        }
        If this error occurs, the test will pass but log a warning. The test should be re-run at a later time when extension is allowed.
        """
        logging.info("______________")
        logging.info("Starting the 'Patch refresh webhook subscription' test")

        #Act
        response = self.api_request.patch_refresh_web_hook_subscription()

        #Assert
        if response.status_code == 400:
            self.assertIn("message", response.data)
            expected_message = "Extending this subscription beyond"
            self.assertTrue(response.data["message"].startswith(expected_message),
                            f"Unexpected error message: {response.data['message']}")
            logging.warning(f"Subscription extension not allowed yet. Message: {response.data['message']}")
        else:
            self.assertTrue(response.ok)
            self.assertEqual(200, response.status_code)
            self.assertEqual(self.config["subscriptions_id"]["0"], response.data["id"])

        logging.info("Test ended successfully")

if __name__ == '__main__':
    unittest.main()