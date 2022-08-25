import requests, json
#declaring the url
base_url = 'https://api.cisco.com/product/v1/information/serial_numbers/SPE181700LN'

headers = { 'Accept': 'application/json', 'Content_Type': 'application/json' }

response = requests.request("GET", base_url=base_url, headers=headers, data={})
data = response.json()
print(data)
