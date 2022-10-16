from flask import Flask, request
import json
from FinebitOperator import FinebitOperator
import csv
from datetime import datetime
from requestTester import requestTest
app = Flask(__name__)
fbo = FinebitOperator()


def saveCSV(param, csvPath='output.csv'):
	f = open(csvPath, 'a', encoding='utf-8', newline='')
	wr = csv.writer(f)
	wr.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), param['type'], param['data']])
	f.close()

@app.route('/waitpos', methods=['POST'])
def onWaitpos():
	ret = {'result': True, 'type':'waitpos'}
	try:
		data = json.loads(request.data.decode('utf-8'))
		ret['result'] = fbo.actionLogin()
		ret['data'] = data
	except Exception as e:
		ret['result'] = False
		ret['error'] = str(e)
	finally:
		saveCSV(ret)
		return json.dumps(ret)

@app.route('/enterPos', methods=['POST'])
def onEnterPos():
	ret = {'result': True, 'type':'enterPos'}
	try:
		data = json.loads(request.data.decode('utf-8'))
		ret['data'] = data
		if data['position'] == 'long':
			ret['result'] = fbo.actionLong()
			pass
		elif data['position'] == 'short':
			ret['result'] = fbo.actionShort()
			pass
		else:
			pass
	except Exception as e:
		ret['result'] = False
		ret['error'] = str(e)
	finally:
		saveCSV(ret)
		return json.dumps(ret)

@app.route('/setStopLoss', methods=['POST'])
def onSetStopLoss():
	ret = {'result': True, 'type':'setStopLoss'}
	try:
		data = json.loads(request.data.decode('utf-8'))
		ret['data'] = data
		ret['result'] = fbo.actionStopLoss(int(data['price']))
	except Exception as e:
		ret['result'] = False
		ret['error'] = str(e)
	finally:
		saveCSV(ret)
		return json.dumps(ret)

@app.route('/clear', methods=['POST'])
def onClear():
	ret = {'result': True, 'type':'clear'}
	try:
		data = json.loads(request.data.decode('utf-8'))
		ret['data'] = data
		ret['result'] = fbo.actionClear()
	except Exception as e:
		ret['result'] = False
		ret['error'] = str(e)
	finally:
		saveCSV(ret)
		return json.dumps(ret)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3004)