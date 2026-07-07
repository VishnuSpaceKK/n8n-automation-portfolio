# Sends user data to an n8n webhook via POST request
# Logs name, age, HTTP status code, and timestamp to log.txt
# Built as proof of Python + n8n integration

import requests
import datetime

name = input('Enter your name')
age = input('Your age')
age = int(age)

response = requests.post('https://xgaami.app.n8n.cloud/webhook-test/0ac31fba-7a22-46d8-bcee-437a1a21e9cc', json = {'name':name, 'age':age})

f = open('log.txt', 'w')
f.write(f"Name: {name}, Age: {age}, Status: {response.status_code}, Time: {datetime.datetime.now()}")

