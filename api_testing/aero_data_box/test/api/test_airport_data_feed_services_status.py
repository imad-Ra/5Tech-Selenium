import unittest
import logging
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.health_chek_and_status_api import APIHealthCheckAndStatus

class TestAPIFlightStatus(unittest.TestCase):

    def setUp(self):
        # Arrange
        self.config = ConfigProvider.load_from_file()
        self.api_request = APIHealthCheckAndStatus(APIWrapper())
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def test_airports_supporting_data_feed(self):
        """
        Tests the API endpoint for retrieving airports supporting data feed(flight schedule).
        """
        logging.info("______________")
        logging.info("Starting the 'Airports supporting data feed' test")

        # Act
        response = self.api_request.get_airports_supporting_data_feed()

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], self.config["airports_support_data"]["0"])

        logging.info("Test ended successfully")

if __name__ == '__main__':
    unittest.main()