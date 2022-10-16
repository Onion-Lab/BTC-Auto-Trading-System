import requests
import json
import urllib
from urllib.parse import urljoin
import time

def requestTest(host, path, param):
	try:
		url = urllib.parse.urljoin(host, path)
		r = requests.post(url, json=param)
		return json.loads(r.text)
	except Exception as e:
		pass
	

if __name__ == '__main__':
	# print(requestTest('http://127.0.0.1:3004', '/waitpos', {}))
	# time.sleep(1)
	# print(requestTest('http://127.0.0.1:3004', '/enterPos', {'position':'short'}))
	# time.sleep(1)
	# print(requestTest('http://127.0.0.1:3004', '/setStopLoss', {'price':0}))
	# time.sleep(1)
	# print(requestTest('http://127.0.0.1:3004', '/clear', {}))
	# time.sleep(1)
	# print(requestTest('http://127.0.0.1:3004', '/enterPos', {'position':'short'}))
	# time.sleep(1)
	# print(requestTest('http://127.0.0.1:3004', '/setStopLoss', {'price':0}))
	# time.sleep(1)
	# print(requestTest('http://127.0.0.1:3004', '/clear', {}))
	# time.sleep(1)
	# print(requestTest('http://127.0.0.1:3004', '/enterPos', {'position':'short'}))
	# time.sleep(1)
	# print(requestTest('http://127.0.0.1:3004', '/setStopLoss', {'price':0}))
	# time.sleep(1)
	# print(requestTest('http://127.0.0.1:3004', '/clear', {}))
	# time.sleep(1)
	# print(requestTest('http://127.0.0.1:3004', '/enterPos', {'position':'short'}))
	# time.sleep(1)
	# print(requestTest('http://127.0.0.1:3004', '/setStopLoss', {'price':0}))
	# time.sleep(1)
	# print(requestTest('http://127.0.0.1:3004', '/clear', {}))
	# time.sleep(1)
	# print(requestTest('http://127.0.0.1:3004', '/enterPos', {'position':'short'}))
	# time.sleep(1)
	# print(requestTest('http://127.0.0.1:3004', '/enterPos', {'position':'long'}))
	# time.sleep(1)
	# print(requestTest('http://127.0.0.1:3004', '/enterPos', {'position':'short'}))
	# time.sleep(1)
	# print(requestTest('http://127.0.0.1:3004', '/enterPos', {'position':'short'}))
	# time.sleep(1)
	# print(requestTest('http://127.0.0.1:3004', '/clear', {}))
	# time.sleep(1)
	# print(requestTest('http://127.0.0.1:3004', '/clear', {}))
	# time.sleep(1)
	# print(requestTest('http://127.0.0.1:3004', '/setStopLoss', {'price':0}))
	# time.sleep(1)
	print(requestTest('http://127.0.0.1:3004', '/enterPos', {'position':'long'}))
	time.sleep(1)
	# print(requestTest('http://127.0.0.1:3004', '/setStopLoss', {'price':0}))
	# time.sleep(1)
	# print(requestTest('http://127.0.0.1:3004', '/setStopLoss', {'price':1}))
	# time.sleep(1)
	# print(requestTest('http://127.0.0.1:3004', '/setStopLoss', {'price':23}))
	# time.sleep(1)
	# print(requestTest('http://127.0.0.1:3004', '/setStopLoss', {'price':23}))
	# time.sleep(1)