import urllib
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
	print(lookup)
	res = data.find({lookup['type']: lookup['data']})
	print(res)
	return res

@app.route('/')
def freesource():
	lookupData = ''
	lookup = False
	opts = {'username': request.args.get('username'), 'email': request.args.get('email'), 'ip': request.args.get('ip')}
	for key, value in opts.items():
		if opts[key]:
			lookup = {'type': key, 'data': opts[key]}

	if lookup != False:
		for result in doLookup(lookup):
			for key, value in result.items():
				lookupData += '<p>{0}: {1}<br/></p>\r\n'.format(key, value)
			#lookupData += '{0}<br/>\r\n'.format(str(result))
	else:
		lookupData = "<p>COCKS IN MY ASSSSSSSSSSSSSS 666</p>"

	print(lookupData)

	return render_template('index.html', data=lookupData)

#data.insert_one({'username': 'test', 'password': 'testPassword', 'email': 'test@test.com', 'database': 'myspaceTest', 'ip': '127.0.0.1'})