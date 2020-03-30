import configparser
import os
import random
import sys

import omise

omise.api_secret = os.environ.get("API_SECRET")
omise.api_public = os.environ.get("API_PUBLIC")

customer_id = sys.argv[1]
charges_amount = int(sys.argv[2])

customer = omise.Customer.retrieve(customer_id)

for n in range(0, charges_amount):
    charge = omise.Charge.create(
        amount=int(str(random.randint(20, 100)) + "00"),
        currency="thb",
        description="charge no." + str(random.randrange(100)),
        customer=customer.id,
        card=customer.cards[0].id,
    )

print("{} charge(s) have been created".format(charges_amount))
