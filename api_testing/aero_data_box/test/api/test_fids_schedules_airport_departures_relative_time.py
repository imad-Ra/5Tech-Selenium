import unittest
import logging
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.flight_api import APIFlightApi
from api_testing.aero_data_box.infra.api.logging_basicConfig import LoggingSetup

class TestAPIFIDSSchedulesAirportDeparturesTimeRange(unittest.TestCase):

    def setUp(self):
        self.config = ConfigProvider.load_from_file()
        self.api_request = APIFlightApi(APIWrapper())

    def test_fids_Schedules_airport_departures_time_range(self):
        """
        Tests the API endpoint for retrieving FIDS getting updated flights schedule per specific airports by time range relative to current time.
        """
        logging.info("______________")
        logging.info("Starting the 'FIDS Schedules airport departures time range' test")

        querystring = self.config["querystring"]["5"]
        response = self.api_request.get_fids_schedules_airport_departures_relative_time(querystring)
        fids_relative_time = response.json()

        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(fids_relative_time["departures"][0]["departure"]["scheduledTime"]["utc"],
                         self.config["time"]["current_utc_time_for_relative"])

        logging.info("Test ended successfully")
        logging.info("Note: This test checks time and needs to be updated daily. In an ideal environment, the time should be continuously updated in the database.")

if __name__ == '__main__':
    unittest.main()