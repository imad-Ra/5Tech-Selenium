from api_testing.aero_data_box.infra.api.api_wrapper import APIWrapper
from api_testing.aero_data_box.infra.api.config_provider import ConfigProvider


class APIFlightAlertPUSH:
    config = ConfigProvider.load_from_file()


    headers = config["headers"]
    headers1 = config["headers_content_type"]
    url = config["url"]
    flights_number = config["url-keys"]["flight_number"]
    subscription_webhook = config["url-keys"]["subscriptions_webhook"]
    flights_airports = config["url-keys"]["flights_airports"]
    flight_by_number = config["url-keys"]["flight_bynumber"]
    refresh = config["url-keys"]["refresh"]


    def __init__(self, request: APIWrapper):
        self._request = request

    def post_create_web_hook_subscription(self, payload):
        url = f"{self.url}{self.subscription_webhook}{self.flight_by_number}/{self.config["flight-numbers"]["0"]}"
        return self._request.post_request(url, headers=self.headers1, json=payload)

    def get_list_of_webhook_subscriptions(self):
        url = f"{self.url}{self.subscription_webhook}"
        return self._request.get_request(url, headers=self.headers)

    def get_web_hook_subscription(self):
        url = f"{self.url}{self.subscription_webhook}/{self.config["subscriptions_id"]["0"]}"
        return self._request.get_request(url, headers=self.headers)

    def patch_refresh_web_hook_subscription(self):
        url = f"{self.url}{self.subscription_webhook}/{self.config['subscriptions_id']['0']}{self.refresh}"
        return self._request.patch_request(url, headers=self.headers1)