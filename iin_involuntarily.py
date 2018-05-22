#!/usr/bin/python
import requests
import random
import time

iin_list = ['439137', '520000', '400555', '356342']

while True:
    start = time.clock()
    r = requests.get("https://iin.omise.co/v1/%s" % random.choice(iin_list), timeout=1)
    request_time = time.clock() - start
    print("Request completed in %f ms" % request_time)
