from api_testing.deck_of_cards.infra.api.api_wrapper import APIWrapper
from api_testing.deck_of_cards.infra.api.config_provider import ConfigProvider


class APIDecksOfCards:

    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_from_file('../../config.json')


    def get_back_of_card(self, url):
        return self._request.get_request(f'{url}/static/img/back.png')

    def shuffle_the_cards(self, url):
        return self._request.get_request(f'{url}/api/deck/new/shuffle/?deck_count={self.config["deck_count"]}')


    def draw_a_card(self, url, deck_id):
        return self._request.post_request(f'{url}/api/deck/{deck_id}/draw/?count={self.config['draw_a_card']}')
