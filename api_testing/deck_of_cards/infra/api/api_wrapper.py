import requests


class APIWrapper:

    def __init__(self):
        self._request = None

    @staticmethod
    def get_request(url, headers=None, body=None):
        """Sends a GET request to the specified URL with optional headers and body.

        Args:
            url (str): The URL to send the GET request to.
            headers (dict, optional): The headers to include in the request.
            body (dict, optional): The body of the request, if any.

        Returns:
            Response: The response from the GET request.
        """
        return requests.get(url, headers=headers, json=body)

    def get_request(self, url, body=None):
        return requests.get(url, json=body)

    def post_request(self, url, body=None):
        return requests.post(url, json=body)

    def delete_request(self, url, data=None):
        return requests.delete(url, json=data)

    def get_status_code(self):
        return requests.get().status_code

    def get_ok(self):
        return requests.get().ok