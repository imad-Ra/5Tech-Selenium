from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider

class APIHealthCheckAndStatus:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_from_file()
        self.headers = self.config["headers"]
        self.url = self.config["url"]
        self.health_services_url = self.config["url-keys"]["health_services"]
        self.feeds_url = self.config["url-keys"]["feeds"]
        self.flights_schedules_url = self.config["url-keys"]["flights_schedules"]
        self.airports_url = self.config["url-keys"]["airports"]

    def get_airports_supporting_data_feed(self):
        url = f"{self.url}{self.health_services_url}{self.feeds_url}{self.flights_schedules_url}{self.airports_url}"
        return self._request.get_request(url, headers=self.headers)

    def get_airport_data_feed_services_status(self):
        url = f"{self.url}{self.health_services_url}{self.airports_url}/{self.config['airports-codes']['2']}{self.feeds_url}"
        return self._request.get_request(url, headers=self.headers)

    def get_general_status_of_data_feed(self):
        url = f"{self.url}{self.health_services_url}{self.feeds_url}{self.flights_schedules_url}"
        return self._request.get_request(url, headers=self.headers)