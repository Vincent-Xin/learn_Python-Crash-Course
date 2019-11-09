from __future__ import (absolute_import,division,
	print_function,unicode_literals)

from urllib.request import urlopen
import json
import requests

json_url='http:///btc_master/btc_close_2017.json'
response=urlopen(json_url)
req=response.read()
with open('btc_close_2017_urllib.json','wb') as f:
	f.write(req)

file_urllib=json.loads(req)
print(file_urllib)

json_url='http://btc/master/btc_close_2017.json'
req=requests.get(json_url)
with open('btc_close_2017_request.json','w') as f:
	f.write(req)
file_requests=req.json()
