import urllib
import re

from pymongo import MongoClient
from flask import Flask
from flask import render_template
from flask import request

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
	opts = {'username': request.args.get('username'), 'email': request.args.get('email'), 'ip': request.args.get('ip'), 'password': request.args.get('password')}
	for key, value in opts.items():
		if opts[key]:
			lookup = {'type': key, 'data': opts[key]}

	if lookup != False:
		lookup['data'] = lookup['data']
		for result in doLookup(lookup):
			for key, value in result.items():
				lookupData += '<p>{0}: {1}<br/></p>\r\n'.format(key, value)
			lookupData += "--------------------------------------<br/>"
			#lookupData += '{0}<br/>\r\n'.format(str(result))
	else:
		lookupData = "<p>Ready.</p>"

	return render_template('new_index.htm', data=lookupData)

#data.insert_one({'username': 'test', 'password': 'testPassword', 'email': 'test@test.com', 'database': 'myspaceTest', 'ip': '127.0.0.1'})
