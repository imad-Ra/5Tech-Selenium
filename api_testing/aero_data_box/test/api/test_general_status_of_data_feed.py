import unittest
import logging
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.health_chek_and_status_api import APIHealthCheckAndStatus
from api_testing.aero_data_box.infra.api.logging_basicConfig import LoggingSetup

class TestAPIFlightStatus(unittest.TestCase):

    def setUp(self):
        # Arrange
        self.config = ConfigProvider.load_from_file()
        self.api_request = APIHealthCheckAndStatus(APIWrapper())

    def test_general_status_of_data_feed(self):
        """
        Tests the API endpoint for retrieving general status of data feed.
        """
        logging.info("______________")
        logging.info("Starting the 'General status of data feed' test")

        # Act
        response = self.api_request.get_general_status_of_data_feed()

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.config["service"]["0"], response.data["service"])

        logging.info("Test ended successfully")

if __name__ == '__main__':
    unittest.main()