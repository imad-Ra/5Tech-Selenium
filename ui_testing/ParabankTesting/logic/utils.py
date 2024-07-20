import random
from enum import Enum


class Field(Enum):
    FIRST_NAME = ["John", "Jane", "Alice", "Bob"]
    LAST_NAME = ["Smith", "Doe", "Johnson", "Brown"]
    CITY = ["New York", "Los Angeles", "Chicago", "Houston"]
    STATE = ["NY", "CA", "IL", "TX"]
    ADDRESS = ["123 Main St", "456 Elm St", "789 Maple St", "101 Oak St"]
    ZIP_CODE = ["10001", "90001", "60601", "77001"]
    SSN = ["123-45-6789", "987-65-4321", "555-55-5555", "666-66-6666"]


def generate_random_value(field):
    return random.choice(field.value)