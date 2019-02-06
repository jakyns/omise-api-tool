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

token = omise.Token.create(
    name='Somchai Prasert',
    number='4242424242424242',
    expiration_month=10,
    expiration_year=2019,
    city='Bangkok',
    postal_code='10320',
    security_code=123
)

customer = omise.Customer.create(
    email='johndoe_no{0}'.format(random.randint(0, 99)),
    card=token.id
)


omise.Charge.create(
    amount=int(str(random.randint(20, 100)) + '00'),
    currency='thb',
    description='create charge since the beginning flow',
    customer=customer.id,
    card=customer.cards[0].id
)

print('generate token, create customer with card then create charge')
