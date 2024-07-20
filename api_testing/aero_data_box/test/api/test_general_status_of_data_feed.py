import unittest

from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider
from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.logic.api.health_chek_and_status_api import APIHealthCheckAndStatus


class TestAPIFlightStatus(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.config = ConfigProvider.load_from_file()
        print(f"Config loaded!")
        self.api_request = APIHealthCheckAndStatus(APIWrapper())

    def test_airports_supporting_data_feed(self):
        """
        Tests the shuffling of the deck by calling the API and validating the response.
        """
        response = self.api_request.get_general_status_of_data_feed()
        flight_status_nearest = response.json()
        print(flight_status_nearest)

        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(flight_status_nearest["service"], self.config["service"]["0"])
