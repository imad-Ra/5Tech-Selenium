import random
import string
import time
import logging
from selenium.common import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Utils:
    # This class manages strings and numbers generating functions.
    # This class in infra because it can be used all around the world
    # not only for a specific website or app.

    #------------------------------------------------------------------------------------------------------------
    # This function generate automatically a random string built
    # from letters, digits and punctuations.
    # It requires a"length" as an input.
    @staticmethod
    def generate_random_string(length) -> str:
        letters = string.ascii_letters + string.digits + string.punctuation
        return ''.join((random.choice(letters) for i in range(length)))

    #------------------------------------------------------------------------------------------------------------
    # This function generate automatically a random number
    # It requires a"length" as an input.

    @staticmethod
    def generate_random_number(length) -> str:
        numbers = string.digits
        return ''.join((random.choice(numbers) for i in range(length)))

    #------------------------------------------------------------------------------------------------------------
    # This function can bea added in any test step as a time waiting
    # together with retries to submit a specific action.
    @staticmethod
    def wait_for_action(action, sleep_time, retries):
        result = action
        while retries > 0:
            if result:
                return True
            result = action
            time.sleep(sleep_time)
            retries -= retries
        return False
    #-----------------------------------------------------------------------------------------