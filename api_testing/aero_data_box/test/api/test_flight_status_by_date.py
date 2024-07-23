import unittest
import logging
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.flight_api import APIFlightApi
from api_testing.aero_data_box.infra.api.logging_basicConfig import LoggingSetup


class TestAPIFlightStatus(unittest.TestCase):

    def setUp(self):
        #Arrange
        self.config = ConfigProvider.load_from_file()
        self.api_request = APIFlightApi(APIWrapper())

    def test_flight_status_by_date(self):
        """
        Tests the API endpoint for getting flight status by specified  date
        """
        logging.info("______________")
        logging.info("Starting the 'Flight status by date' test")

        #Act
        response = self.api_request.get_flight_status_by_date()

        #Assert
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.config["aircraft-models"]["0"], response.data[0]["aircraft"]["model"])

        logging.info("Test ended successfully")


if __name__ == '__main__':
    unittest.main()
