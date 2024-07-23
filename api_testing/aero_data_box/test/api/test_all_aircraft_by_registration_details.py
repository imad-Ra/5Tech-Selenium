import unittest
import logging
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.aircraft_api import APIAircraftApi

class TestAPIAllAircraftByRegistrationDetails(unittest.TestCase):

    def setUp(self):
        #Arrange
        self.config = ConfigProvider.load_from_file()
        self.api_request = APIAircraftApi(APIWrapper())
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def test_all_aircraft_by_registration_details(self):
        """
        Tests the API endpoint for retrieving all aircraft by registration details.
        """
        logging.info("Starting the 'All aircrafts by registration details' test")
        #Act
        response = self.api_request.get_all_aircraft_by_registration_details()

        #Assert
        self.assertTrue(response.ok)
        self.assertEqual(200, response.status_code)
        self.assertEqual(self.config["aircraft_registration"]["0"], response.data["reg"])

        logging.info("Test ended successfully")

if __name__ == '__main__':
    unittest.main()