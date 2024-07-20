import json
import unittest

from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.flight_api import APIFlightApi


class TestAPIFlightDepartureDates(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.config = ConfigProvider.load_from_file()
        print(f"Config loaded!")
        self.api_request = APIFlightApi(APIWrapper())

    def test_flight_departure_dates(self):
        """
        Tests the shuffling of the deck by calling the API and validating the response.
        """
        response = self.api_request.get_flight_departure_dates()
        # flight_departure_date = response.json()
        # print(flight_departure_date)


        # For a 204 response, we expect no content
        self.assertEqual(response.text, '')
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 204)

        # Don't try to parse JSON for a 204 response
        if response.status_code != 204:
            try:
                flight_departure_date = response.json()
                print(flight_departure_date)
            except json.JSONDecodeError:
                self.fail("Expected JSON content for non-204 response")
        else:
            print("No content in response (as expected for 204)")

