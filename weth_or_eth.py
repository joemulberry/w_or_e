import requests
import json
from time import time

url = 'https://raw.githubusercontent.com/joemulberry/parallel/main/data/opensea_parallel_dumps.json'
resp = requests.get(url)
os_data = json.loads(resp.text)


eth=0
not_eth = 0

for d in os_data:
    
    if d['last_sale'] != None:
        if d['last_sale']['payment_token']['symbol'] == 'ETH':
            eth += 1
        else:
            not_eth += 1

total_count = not_eth+eth
print((eth, not_eth, total_count))

eth = eth / total_count
not_eth = not_eth / total_count

eth = round(eth, 2)
not_eth = round(not_eth, 2)

di = {
    'a': eth,
    'b': not_eth,
    't': time()
    }

print(di)

    