import unittest
import logging
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.flight_api import APIFlightApi


class TestAPIFlightDepartureDates(unittest.TestCase):

    def setUp(self):
        # Arrange
        self.config = ConfigProvider.load_from_file()
        self.api_request = APIFlightApi(APIWrapper())
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def test_flight_departure_dates(self):
        """
        Tests the API endpoint for getting flight departure dates
        """
        logging.info("______________")
        logging.info("Starting the 'Flight departure dates' test")

        # Act
        response = self.api_request.get_flight_departure_dates()

        # Assert
        self.assertIsNotNone(response, "Response should not be None")

        # Check if the response object has a 'data' attribute
        if hasattr(response, 'data'):  # hasattr() checks if an object has a given attribute
            # Log an informational message if data exists
            logging.info("Response contains data")
        else:
            # Log an informational message if no data is found
            logging.info("No data in response")

        logging.info("Test ended successfully")


if __name__ == '__main__':
    unittest.main()
