import codecs
import sys
import time
import multiprocessing
import time

from pymongo import MongoClient

def pushLines(lines):
		client = MongoClient('mongodb://127.0.0.1', 27017)
		db = client.admin
		print('Signed in: {0}'.format(db.authenticate('admin', '.gpe7h+99W:P}gU}')))
		data = db['data']
		data.insert_many(lines)
		lines = []

if __name__ == "__main__":
	lines = []

	for line in codecs.open(sys.argv[1], encoding='utf-8', errors='ignore'):
			try:
					if len(lines) >= 10000000:
						print('Pushing Normal')
						pushLines(lines)
						lines = []
					username, password, email, dob, country, gender, ip, name = line.strip().rstrip().lower().split(':')
					lines.append({'username': username, 'password': password, 'email': email, 'database': sys.argv[2], 'ip': ip, 'dob': dob, 'name': name})
			except:
					continue

	print('Pushing leftover...')
	pushLines(lines)
	lines = []

#data.insert_one({'username': 'test', 'password': 'testPassword', 'email': 'test@test.com', 'database': 'myspaceTest', 'ip': '127.0.0.1'})
