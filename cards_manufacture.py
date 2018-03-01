import configparser
import os
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

cards_amount = int(sys.argv[1])

customer = omise.Customer.retrieve('cust_test_5b4fhq8na545dyxhhdq')

for n in range(0, cards_amount):
    token = omise.Token.create(
        name='Somchai Prasert',
        number='4242424242424242',
        expiration_month=10,
        expiration_year=2019,
        city='Bangkok',
        postal_code='10320',
        security_code=123
    )

    customer.update(card=token.id)

print('{} card(s) have been created for {}'.format(cards_amount, customer.id))
