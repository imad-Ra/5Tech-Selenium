import unittest
import logging
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.airport_api import APIAirportApi
from api_testing.aero_data_box.infra.api.logging_basicConfig import LoggingSetup

class TestAPIAirportByLocation(unittest.TestCase):

    def setUp(self):
        self.config = ConfigProvider.load_from_file()
        self.api_request = APIAirportApi(APIWrapper())

    def test_airport_by_location(self):
        """
        Tests the API endpoint for retrieving airports by the radius of certain location.
        """
        logging.info("______________")
        logging.info("Starting the 'Airport by location' test")

        querystring1 = self.config["querystring"]["1"]

        response = self.api_request.get_search_airports_by_location(querystring1)
        airport_by_location = response.json()

        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(airport_by_location["count"], int(self.config["results"]["7"]))

        logging.info("Test ended successfully")

if __name__ == '__main__':
    unittest.main()