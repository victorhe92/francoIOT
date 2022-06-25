from urllib import response
import requests
import json

response_API=requests.get('https://www.askpython.com/')
print(response_API.status_code)
print(response_API.text)
print(response_API.json())
