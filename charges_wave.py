import configparser
import os
import random
import sys

import omise

ENV_MODE = os.environ.get('ENV_MODE', 'development')

config = configparser.ConfigParser()
config.read_file(open('default.cfg'))
config.read('{}.cfg'.format(ENV_MODE))

omise.api_main = config['omise']['api_main']
omise.api_vault = config['omise']['api_vault']
omise.api_secret = config['omise']['api_secret']
omise.api_public = config['omise']['api_public']

charges_amount = int(sys.argv[1])

customer = omise.Customer.retrieve('cust_test_5b4fhq8na545dyxhhdq')

for n in range(0, charges_amount):
    charge = omise.Charge.create(
        amount=int(str(random.randint(20, 100)) + '00'),
        currency='thb',
        description='charge no.' + str(random.randrange(100)),
        customer=customer.id,
        card='card_test_5b4fhq6kixz8ks2egae',
    )

print('{} charge(s) have been created'.format(charges_amount))
