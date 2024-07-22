from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider


class APIAircraftApi:
    config = ConfigProvider.load_from_file()


    headers = config["headers"]
    url = config["url"]
    flights_number = config["url-keys"]["flight_number"]
    aircrafts = config["url-keys"]["aircrafts"]
    subscription_webhook = config["url-keys"]["subscriptions_webhook"]
    flights_airports = config["url-keys"]["flights_airports"]
    iata_code_type = config["url-keys"]["code_type"]
    search = config["url-keys"]["search"]
    location = config["url-keys"]["location"]
    ip = config["url-keys"]["ip"]
    all = config["url-keys"]["all"]





    def __init__(self, request: APIWrapper):
        self._request = request

    def get_single_aircraft_by_registration_details(self):
        url = f"{self.url}{self.aircrafts}/{self.config["search_by"]["0"]}/{self.config["aircraft_registration"]["0"]}"
        return self._request.get_request(url, headers=self.headers)

    def get_all_aircraft_by_registration_details(self):
        url = f"{self.url}{self.aircrafts}/{self.config["search_by"]["0"]}/{self.config["aircraft_registration"]["0"]}"
        return self._request.get_request(url, headers=self.headers)

