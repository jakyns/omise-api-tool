#!/usr/bin/python
import requests
import random
import time

iin_list = ['439137', '520000', '400555', '356342']
round = 0

while True:
    try:
        start = time.clock()
        r = requests.get("https://iin.omise.co/v1/%s" % random.choice(iin_list), timeout=1)
        request_time = time.clock() - start
        print("Round %i request completed in %f ms" % (round, request_time))
        round+=1
    except Exception as e:
        print(e)
        break

