import unittest
import logging
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.airport_api import APIAirportApi

class TestAPIAirportByCode(unittest.TestCase):

    def setUp(self):
        # Arrange
        self.config = ConfigProvider.load_from_file()
        self.api_request = APIAirportApi(APIWrapper())
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def test_airport_by_code(self):
        """
        Tests the API endpoint for retrieving airport information by IATA code.
        """
        logging.info("Starting the 'Airport by code' test")

        # Act
        response = self.api_request.get_airport_by_code()

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(200, response.status_code)
        self.assertEqual(self.config["airports-codes"]["1"], response.data["iata"])

        logging.info("Test ended successfully")

if __name__ == '__main__':
    unittest.main()