import configparser
import os
import random
import sys

import omise

omise.api_secret = os.environ.get("API_SECRET")
omise.api_public = os.environ.get("API_PUBLIC")

token = omise.Token.create(
    name="Somchai Prasert",
    number="4242424242424242",
    expiration_month=10,
    expiration_year=2022,
    city="Bangkok",
    postal_code="10320",
    security_code=123,
)

customer = omise.Customer.create(
    email="johndoe_no{0}".format(random.randint(0, 99)), card=token.id
)


omise.Charge.create(
    amount=int(str(random.randint(20, 100)) + "00"),
    currency="thb",
    description="create charge since the beginning flow",
    customer=customer.id,
    card=customer.cards[0].id,
)

print("generate token, create customer with card then create charge")
