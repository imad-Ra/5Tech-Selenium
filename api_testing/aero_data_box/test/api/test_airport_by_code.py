import logging

import unittest
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.airport_api import APIAirportApi
from api_testing.aero_data_box.infra.api.logging_basicConfig import LoggingSetup

class TestAPIAirportByCode(unittest.TestCase):

    def setUp(self):
        self.config = ConfigProvider.load_from_file()
        self.api_request = APIAirportApi(APIWrapper())

    def test_airport_by_code(self):
        """
        Tests the API endpoint for retrieving airport information by IATA code.
        """

        logging.info("______________")
        logging.info("Starting the 'Airport by code' test")

        response = self.api_request.get_airport_by_code()
        airport_by_code = response.json()

        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(airport_by_code["iata"], self.config["airports-codes"]["1"])

        logging.info("Test ended successfully")

if __name__ == '__main__':
    unittest.main()