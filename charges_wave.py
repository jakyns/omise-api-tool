import configparser
import os
import random
import sys

import omise

ENV_MODE = os.environ.get('ENV_MODE', 'development')

config = configparser.ConfigParser()
config.read_file(open('config/default.cfg'))
config.read('config/{}.cfg'.format(ENV_MODE))

omise.api_main = config['omise']['api_main']
omise.api_vault = config['omise']['api_vault']
omise.api_secret = config['omise']['api_secret']
omise.api_public = config['omise']['api_public']

customer_id = sys.argv[1]
charges_amount = int(sys.argv[2])

customer = omise.Customer.retrieve(customer_id)

for n in range(0, charges_amount):
    charge = omise.Charge.create(
        amount=int(str(random.randint(20, 100)) + '00'),
        currency='thb',
        description='charge no.' + str(random.randrange(100)),
        customer=customer.id,
        card=customer.cards[0].id,
    )

print('{} charge(s) have been created'.format(charges_amount))
