import json
import unittest

from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.flight_api import APIFlightApi


class TestAPIFIDSSchedulesAirportDeparturesTimeRange(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.config = ConfigProvider.load_from_file()
        print(f"Config loaded!")
        self.api_request = APIFlightApi(APIWrapper())

    def test_fids_Schedules_airport_departures_time_range(self):
        """
        Tests the shuffling of the deck by calling the API and validating the response.
        """
        response = self.api_request.get_fids_schedules_airport_departures_time_range()
        fids_time_range = response.json()
        print(fids_time_range)


        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(fids_time_range["departures"][0]["departure"]["scheduledTime"]["utc"], "2024-04-05 01:00Z")
