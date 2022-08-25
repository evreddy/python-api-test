import requests, json
#declaring the url
url = 'https://api.cisco.com/product/v1/information/serial_numbers/SPE181700LN'

headers = { 'Accept': 'application/json', 'Content_Type': 'application/json' }

response = requests.request("GET", url, headers=headers, serial_numbers={})
serial_numbers = response.json()
print(serial_numbers)
