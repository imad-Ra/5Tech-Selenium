import unittest
import logging
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.aircraft_api import APIAircraftApi
from api_testing.aero_data_box.infra.api.logging_basicConfig import LoggingSetup

class TestAPIAllAircraftByRegistrationDetails(unittest.TestCase):

    def setUp(self):
        self.config = ConfigProvider.load_from_file()
        self.api_request = APIAircraftApi(APIWrapper())

    def test_all_aircraft_by_registration_details(self):
        """
        Tests the API endpoint for retrieving all aircraft by registration details.
        """
        logging.info("______________")
        logging.info("Starting the 'All aircrafts by registration details' test")

        response = self.api_request.get_all_aircraft_by_registration_details()
        all_aircraft_by_registration = response.json()

        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(all_aircraft_by_registration["reg"], self.config["aircraft_registration"]["0"])

        logging.info("Test ended successfully")

if __name__ == '__main__':
    unittest.main()