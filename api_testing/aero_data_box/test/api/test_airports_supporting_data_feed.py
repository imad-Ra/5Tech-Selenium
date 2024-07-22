import unittest
import logging
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.health_chek_and_status_api import APIHealthCheckAndStatus
from api_testing.aero_data_box.infra.api.logging_basicConfig import LoggingSetup

class TestAPIFlightStatus(unittest.TestCase):

    def setUp(self):
        self.config = ConfigProvider.load_from_file()
        self.api_request = APIHealthCheckAndStatus(APIWrapper())

    def test_airports_supporting_data_feed(self):
        """
        Tests the API endpoint for retrieving airports supporting data feed(flight schedule).
        """
        logging.info("______________")
        logging.info("Starting the 'Airports supporting data feed' test")

        response = self.api_request.get_airports_supporting_data_feed()
        flight_status_nearest = response.json()

        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(flight_status_nearest["count"], self.config["airports_support_data"]["0"])

        logging.info("Test ended successfully")

if __name__ == '__main__':
    unittest.main()