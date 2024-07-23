from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider

class APIFlightApi:
    config = ConfigProvider.load_from_file()

    headers = config["headers"]
    url = config["url"]
    flights_number = config["url-keys"]["flight_number"]
    subscription_webhook = config["url-keys"]["subscriptions_webhook"]
    flights_airports = config["url-keys"]["flights_airports"]
    iata_code_type = config["url-keys"]["code_type"]
    flyby_number = config["url-keys"]["flight_bynumber"]

    def __init__(self, request: APIWrapper):
        self._request = request

    def get_fids_schedules_airport_departures_relative_time(self):
        url = f"{self.url}{self.flights_airports}{self.iata_code_type}/{self.config['airports-codes']['0']}"
        return self._request.get_request(url, headers=self.headers)

    def get_flight_departure_dates(self):
        url = f"{self.url}{self.flights_number}/{self.config['flight-numbers']['0']}/dates/{self.config['time']['dates_for_status_by_date']}"
        return self._request.get_request(url, headers=self.headers)

    def get_flight_status_by_date(self):
        url = f"{self.url}{self.flights_number}/{self.config['flight-numbers']['1']}/{self.config['time']['date_of_flight_status_by_date']}"
        return self._request.get_request(url, headers=self.headers)

    def get_flight_departure_nearest(self):
        url = f"{self.url}{self.flights_number}/{self.config['flight-numbers']['1']}"
        return self._request.get_request(url, headers=self.headers)