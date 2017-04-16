import codecs
import sys

from pymongo import MongoClient

sys.argv = ['', 'dbs/xsplit.txt']

client = MongoClient('mongodb://127.0.0.1', 27017)
db = client.admin
print('Signed in: {0}'.format(db.authenticate('admin', '.gpe7h+99W:P}gU}')))
data = db['data']

def pushLines():
	global lines
	data.insert_many(lines)

file = codecs.open(sys.argv[1], encoding='utf-8', errors='ignore').readlines()
lines = []

for line in file:
	try:
		username, name, email, password = line.strip().rstrip().split('\t')
		lines.append({'username': username, 'password': password, 'email': email, 'database': 'xsplit', 'ip': '127.0.0.1'})
	except:
		continue
		
print('Pushing..')
pushLines()
print('Pushed..')

#data.insert_one({'username': 'test', 'password': 'testPassword', 'email': 'test@test.com', 'database': 'myspaceTest', 'ip': '127.0.0.1'})