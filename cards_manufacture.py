import configparser
import os
import sys

import omise

omise.api_secret = os.environ.get("API_SECRET")
omise.api_public = os.environ.get("API_PUBLIC")

customer_id = sys.argv[1]
cards_amount = int(sys.argv[2])

customer = omise.Customer.retrieve(customer_id)

for n in range(0, cards_amount):
    token = omise.Token.create(
        name="Somchai Prasert",
        number="4242424242424242",
        expiration_month=10,
        expiration_year=2022,
        city="Bangkok",
        postal_code="10320",
        security_code=123,
    )

    customer.update(card=token.id)

print("{} card(s) have been created for {}".format(cards_amount, customer.id))
