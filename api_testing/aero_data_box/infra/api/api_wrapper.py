import requests


class APIWrapper:

    def __init__(self):
        self._request = None

    def get_request(self, url, params=None, body=None, headers=None, cookies=None, auth=None, json=None):
        try:
            response = requests.get(
                url,
                params=params,
                data=body,
                headers=headers,
                cookies=cookies,
                auth=auth,
                json=json
            )
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            print(f'HTTP error occurred: {e}')
        except Exception as e:
            print(f'Other error occurred: {e}')
        return None

    def post_request(self, url, params=None, body=None, headers=None, cookies=None, auth=None, json=None):
        try:
            response = requests.post(
                url,
                params=params,
                data=body,
                headers=headers,
                cookies=cookies,
                auth=auth,
                json=json
            )
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            print(f'HTTP error occurred: {e}')
        except Exception as e:
            print(f'Other error occurred: {e}')
        return None




















# class APIDecksOfCards:
#
#     def __init__(self, request: APIWrapper):
#         self._request = request
#         self.config = ConfigProvider.load_from_file('../../config.json')
#
#     def get_user_details(self, url, headers):
#         """Requests to shuffle the deck with a specified number of decks.
#
#             Args:
#                 url (str): The base URL of the API.
#                 headers (dict): The headers to include in the request.
#
#             Returns:
#                 Response: The response from the API.
#             """
#         url = f"{url}/details?username=omarmhaimdat&user_id=96479162"
#         return self._request.get_request(url, headers=headers)
#
#     @staticmethod
#     def post_request(url, headers=None, body=None):
#         """Sends a POST request to the specified URL with optional headers and body.
#
#         Args:
#             url (str): The URL to send the POST request to.
#             headers (dict, optional): The headers to include in the request.
#             body (dict, optional): The body of the request, if any.
#
#         Returns:
#             Response: The response from the POST request.
#         """
#         return requests.post(url, headers=headers, json=body)