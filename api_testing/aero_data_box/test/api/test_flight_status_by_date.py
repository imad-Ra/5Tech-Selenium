import unittest
import logging
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.flight_api import APIFlightApi
from api_testing.aero_data_box.infra.api.logging_basicConfig import LoggingSetup

class TestAPIFlightStatus(unittest.TestCase):

    def setUp(self):
        self.config = ConfigProvider.load_from_file()
        self.api_request = APIFlightApi(APIWrapper())

    def test_flight_status_by_date(self):
        """
        Tests the API endpoint for getting flight status by specified  date
        """
        logging.info("______________")
        logging.info("Starting the 'Flight status by date' test")

        querystring = self.config["querystring"]["3"]

        response = self.api_request.get_flight_status_by_date(querystring)
        flight_status_date = response.json()

        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(flight_status_date[0]["aircraft"]["model"], self.config["aircraft-models"]["0"])

        logging.info("Test ended successfully")

if __name__ == '__main__':
    unittest.main()