import unittest
import logging
import json
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.flight_api import APIFlightApi
from api_testing.aero_data_box.infra.api.logging_basicConfig import LoggingSetup

class TestAPIFlightDepartureDates(unittest.TestCase):

    def setUp(self):
        self.config = ConfigProvider.load_from_file()
        self.api_request = APIFlightApi(APIWrapper())

    def test_flight_departure_dates(self):
        """
        Tests the API endpoint for getting flight departure dates
        """
        logging.info("______________")
        logging.info("Starting the 'Flight departure dates' test")

        response = self.api_request.get_flight_departure_dates()

        self.assertEqual(response.text, '')
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 204)

        if response.status_code != 204:
            try:
                flight_departure_date = response.json()
            except json.JSONDecodeError:
                self.fail("Expected JSON content for non-204 response")
        else:
            logging.info("No content in response (as expected for 204)")

        logging.info("Test ended successfully")

if __name__ == '__main__':
    unittest.main()