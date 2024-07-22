import unittest
import logging
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.airport_api import APIAirportApi
from api_testing.aero_data_box.infra.api.logging_basicConfig import LoggingSetup

class TestAPIAirportByIpAddressGeoLocation(unittest.TestCase):

    def setUp(self):
        self.config = ConfigProvider.load_from_file()
        self.api_request = APIAirportApi(APIWrapper())

    def test_airports_by_ip_address(self):
        """
        Tests the API endpoint for retrieving airports by costumer's IP address geolocation.
        """
        logging.info("______________")
        logging.info("Starting the 'Airports by IP address' test")

        querystring2 = self.config["querystring"]["2"]

        response = self.api_request.get_search_airports_by_ip_address_geolocation(querystring2)
        airport_by_ip_address_geolocation = response.json()

        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(airport_by_ip_address_geolocation["count"], int(self.config["results"]["2"]))

        logging.info("Test ended successfully")

if __name__ == '__main__':
    unittest.main()