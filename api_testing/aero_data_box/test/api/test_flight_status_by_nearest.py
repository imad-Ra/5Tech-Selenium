import unittest
import logging
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.flight_api import APIFlightApi
from api_testing.aero_data_box.infra.api.logging_basicConfig import LoggingSetup

class TestAPIFlightStatusByNearest(unittest.TestCase):

    def setUp(self):
        self.config = ConfigProvider.load_from_file()
        self.api_request = APIFlightApi(APIWrapper())

    def test_flight_status_by_nearest(self):
        """
        Tests the API endpoint for getting flight information by nearest time (in future or past).
        """
        logging.info("______________")
        logging.info("Starting the 'Flight status by nearest' test")

        response = self.api_request.get_flight_departure_nearest()
        flight_status_nearest = response.json()

        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(flight_status_nearest[0]["number"], self.config["flight-numbers"]["1"])

        logging.info("Test ended successfully")

if __name__ == '__main__':
    unittest.main()