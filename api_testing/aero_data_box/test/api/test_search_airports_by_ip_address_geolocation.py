import unittest
import logging
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.airport_api import APIAirportApi


class TestAPISearchAirportsByIPAddressGeolocation(unittest.TestCase):

    def setUp(self):
        #Arrange
        self.config = ConfigProvider.load_from_file()
        self.api_request = APIAirportApi(APIWrapper())
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def test_search_airports_by_ip_address_geolocation(self):
        """
        Tests the API endpoint for retrieving airports by customer's IP address geolocation.
        """
        logging.info("Starting the 'Airports by IP address' test")


        params = self.config["querystring"]["2"]

        #Act
        response = self.api_request.get_search_airports_by_ip_address_geolocation(params)

        print(response)
        print(response.data)

        #Assert
        self.assertTrue(response.ok)
        self.assertEqual(200, response.status_code)
        self.assertIn('items', response.data)
        self.assertEqual(int(self.config["results"]["2"]),response.data["count"])


        logging.info("Test ended successfully")


if __name__ == '__main__':
    unittest.main()
