# customer_class.py
# The customer class represents a customer at the lemondade stand.
# The customer has preferences for lemonade sweetness and ice level,
# and a price point they are willing to pay.
# All of these attributes will influence their purchasing decision and
# are returned as a list of attributes.

import random

class Customer:
    def __init__(self, condiments_preference=None, meat_preference=None, price_point=None):
        self.condiments_preference = (
            condiments_preference if condiments_preference is not None
            else random.randint(1, 6)
        )
        self.meat_preference = (
            meat_preference if meat_preference is not None
            else random.randint(1, 3)
        )
        self.price_point = (
            price_point if price_point is not None
            else round(random.uniform(3.0, 4.0),2)
        )

    def get_customer_attributes(self):
        return {
            "condiments": self.condiments_preference,
            "meat": self.meat_preference,
            "price": self.price_point
        }