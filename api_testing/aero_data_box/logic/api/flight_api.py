from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider


class APIFlightApi:

    config = ConfigProvider.load_from_file()
    # get_flight_status_by_nearset
    querystring1 = {"withAircraftImage": "false", "withLocation": "true"}
    # get_flight_status_by_date
    querystring2 = {"withAircraftImage": "false", "withLocation": "false"}
    querystring3 = {"withLeg": "true", "direction": "Both", "withCancelled": "true", "withCodeshared": "true",
                    "withCargo": "true", "withPrivate": "true", "withLocation": "false"}

    querystring4 = {"offsetMinutes": "-120", "durationMinutes": "720", "withLeg": "true", "direction": "Both",
                    "withCancelled": "true", "withCodeshared": "true", "withCargo": "true", "withPrivate": "true",
                    "withLocation": "false"}

    payload1 = {"url": "http://your-url"}

    headers = config["headers"]
    url = config["url"]
    flights_number = config["url-keys"]["flight_number"]
    subscription_webhook = config["url-keys"]["subscriptions_webhook"]
    flights_airports = config["url-keys"]["flights_airports"]


    def __init__(self, request: APIWrapper):
        self._request = request

    def post_create_web_hook_subscription(self):
        url = f"{self.url}{self.subscription_webhook}/FlightByNumber/{self.config["flight-numbers"]["0"]}"
        return self._request.post_request(url, headers=self.headers, json=self.payload1)

    def get_flight_status_by_date(self):
        url = f"{self.url}{self.flights_number}/{self.config["flight-numbers"]["1"]}/2024-11-02"
        return self._request.get_request(url, headers=self.headers, params=self.querystring2)

    # We can do "flights_number" in ENUM .

    def get_flight_departure_dates(self):
        url = f"{self.url}{self.flights_number}/{self.config["flight-numbers"]["0"]}/dates/2020-06-01/2024-10-10"
        return self._request.get_request(url, headers=self.headers)

    def get_flight_departure_nearest(self):
        url = f"{self.url}{self.flights_number}/{self.config["flight-numbers"]["1"]}"
        return self._request.get_request(url, headers=self.headers)

    def get_fids_schedules_airport_departures_time_range(self):
        url = f"{self.url}{self.flights_airports}/iata/{self.config["airports-codes"]["1"]}/2024-04-04T20:00/2024-04-05T08:00"
        return self._request.get_request(url, headers=self.headers, params=self.querystring3)

    def get_fids_schedules_airport_departures_relative_time(self):
        url = f"{self.url}{self.flights_airports}/iata/{self.config["airports-codes"]["0"]}"
        return self._request.get_request(url, headers=self.headers, params=self.querystring4)



