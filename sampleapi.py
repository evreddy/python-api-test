import requests

base_url = 'https://api.cisco.com/product/v1/information/serial_numbers/SPE181700LN,REF_CSJ07306405'
rep = requests.get(base_url)
data = resp.jason()
