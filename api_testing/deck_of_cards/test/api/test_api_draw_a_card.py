import unittest

from api_testing.deck_of_cards.infra.api.api_wrapper import APIWrapper
from api_testing.deck_of_cards.infra.api.config_provider import ConfigProvider
from api_testing.deck_of_cards.logic.api.api_logic import APIDecksOfCards


class TestDeckOfCards(unittest.TestCase):


    config = ConfigProvider().load_from_file("../../config.json")

    def test_back_of_cards(self):
        api_request = APIWrapper()
        api_deck_of_cards = APIDecksOfCards(api_request)
        result = api_deck_of_cards.get_back_of_card(self.config['base_url'])
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.ok)

    def test_shuffle_the_cards(self):
        api_request = APIWrapper()
        api_deck_of_cards = APIDecksOfCards(api_request)

        response = api_deck_of_cards.shuffle_the_cards(self.config['base_url'])

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)


    def test_draw_a_card(self):
        api_request = APIWrapper()
        api_deck_of_cards = APIDecksOfCards(api_request)
        self.assertTrue(api_deck_of_cards.draw_a_card(self.config['base_url'], "new").ok)
        self.assertNotEqual(api_deck_of_cards.draw_a_card(self.config['base_url'], "50").status_code, 200)