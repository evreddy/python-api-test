import requests
import json

#declaring the url
base_url = 'https://api.cisco.com/product/v1/information/serial_numbers/SPE181700LN,REF_CSJ07306405'

response = requests.get(base_url)
data = response.json()
print(data)
