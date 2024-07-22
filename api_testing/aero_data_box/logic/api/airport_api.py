from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider


class APIAirportApi:
    config = ConfigProvider.load_from_file()

    headers = config["headers"]
    url = config["url"]
    flights_number = config["url-keys"]["flight_number"]
    airports = config["url-keys"]["airports"]
    subscription_webhook = config["url-keys"]["subscriptions_webhook"]
    flights_airports = config["url-keys"]["flights_airports"]
    iata_code_type = config["url-keys"]["code_type"]
    search = config["url-keys"]["search"]
    location = config["url-keys"]["location"]
    ip = config["url-keys"]["ip"]



    def __init__(self, request: APIWrapper):
        self._request = request

    def get_airport_by_code(self):
        url = f"{self.url}{self.airports}{self.iata_code_type}/{self.config["airports-codes"]["1"]}"
        return self._request.get_request(url, headers=self.headers)

    def get_search_airports_by_location(self, querystring1):
        url = f"{self.url}{self.airports}{self.search}{self.location}"
        return self._request.get_request(url, headers=self.headers, params=querystring1)

    def get_search_airports_by_ip_address_geolocation(self, querystring2):
        url = f"{self.url}{self.airports}{self.search}{self.ip}"
        return self._request.get_request(url, headers=self.headers, params=querystring2)
