import unittest
import logging
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.aircraft_api import APIAircraftApi
from api_testing.aero_data_box.infra.api.logging_basicConfig import LoggingSetup

class TestAPISingleAircraftByRegistrationDetails(unittest.TestCase):

    def setUp(self):
        #Act
        self.config = ConfigProvider.load_from_file()
        self.api_request = APIAircraftApi(APIWrapper())

    def test_single_aircraft_by_registration_details(self):
        """
        Tests the API endpoint for retrieving single aircraft by registration details.
        """
        logging.info("______________")
        logging.info("Starting the 'Single aircraft by registration details' test")
        #Act
        response = self.api_request.get_single_aircraft_by_registration_details()

        #Assert
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.config["aircraft_registration"]["0"] , response.data["reg"])


        logging.info("Test ended successfully")

if __name__ == '__main__':
    unittest.main()