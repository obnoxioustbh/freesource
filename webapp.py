import urllib
import re

from pymongo import MongoClient
from flask import Flask
from flask import render_template
from flask import request

def tableCreator(ths):
	baseString = '<table class="table table-inverse"><tbody>'
	for key, value in ths.items():
		baseString += '<tr><th>{0}</th><td>{1}</td></tr>'.format(key, value)
	baseString += '</tbody></table>'
	return baseString

app = Flask(__name__)
client = MongoClient('mongodb://93.190.142.215', 27017)
db = client.admin
print('Signed in: {0}'.format(db.authenticate('admin', '.gpe7h+99W:P}gU}')))
data = db['data']

def doLookup(lookup):
	res = data.find({"$query": {lookup['type']: lookup['data']}, "$maxTimeMS": 1000})
	return res

@app.route('/')
def freesource():
	#return 'REBUILDING INDEXES, I WANNA SLEEP THO SO WE GO UP TOMORROW IG'
	lookupData = ''
	lookup = False

	content = request.args.get('content')

	if content:

		if '127.0.0.1' in content:
			return 'fuck off broooo'

		if '@' in content:
				lookup = {'type': 'email', 'data': content}

		elif re.search(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', content):
			lookup = {'type': 'ip', 'data': content}

		else:
			lookup = {'type': 'username', 'data': content}

	if lookup != False:
		lookup['data'] = lookup['data']
		for result in doLookup(lookup):
			baseData = ''
			table = tableCreator(result)
			baseData += table
			lookupData += baseData
	else:
		lookupData = ""

	return render_template('new_index.htm', data=lookupData.encode('utf-8'))

#data.insert_one({'username': 'test', 'password': 'testPassword', 'email': 'test@test.com', 'database': 'myspaceTest', 'ip': '127.0.0.1'})
