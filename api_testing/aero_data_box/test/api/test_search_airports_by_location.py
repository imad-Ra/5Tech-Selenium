import unittest
import logging
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.airport_api import APIAirportApi
from api_testing.aero_data_box.infra.api.logging_basicConfig import LoggingSetup

class TestAPIAirportByLocation(unittest.TestCase):

    def setUp(self):
        #Arrange
        self.config = ConfigProvider.load_from_file()
        self.api_request = APIAirportApi(APIWrapper())

    def test_airport_by_location(self):
        """
        Tests the API endpoint for retrieving airports by the radius of certain location.
        """
        logging.info("______________")
        logging.info("Starting the 'Airport by location' test")

        params = self.config["querystring"]["1"]

        #Act
        response = self.api_request.get_search_airports_by_location(params)

        #Arrange
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(int(self.config["results"]["7"]), response.data["count"])

        logging.info("Test ended successfully")

if __name__ == '__main__':
    unittest.main()