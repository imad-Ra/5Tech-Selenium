import unittest
import logging
from datetime import datetime
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.flight_api import APIFlightApi

class TestAPIFIDSSchedulesAirportDeparturesTimeRange(unittest.TestCase):

    def setUp(self):
        # Arrange
        self.config = ConfigProvider.load_from_file()
        self.api_request = APIFlightApi(APIWrapper())
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def test_fids_Schedules_airport_departures_time_range(self):
        """
        Tests the API endpoint for retrieving FIDS getting updated flights schedule per specific airports by time range.
        """
        logging.info("Starting the 'FIDS Schedules airport departures time range' test")

        # Act
        response = self.api_request.get_fids_schedules_airport_departures_relative_time()

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(200, response.status_code)

        # Test response structure
        self.assertIn('departures', response.data)
        self.assertIsInstance(response.data['departures'], list)

        logging.info("Test ended successfully")

    if __name__ == '__main__':
        unittest.main()