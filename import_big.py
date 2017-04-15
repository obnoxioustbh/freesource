import codecs
import sys
import time
import multiprocessing

from pymongo import MongoClient

def pushLines(lines):
		client = MongoClient('mongodb://127.0.0.1', 27017)
		db = client.admin
		print('Signed in: {0}'.format(db.authenticate('admin', '.gpe7h+99W:P}gU}')))
		data = db['data']
		data.insert_many(lines)

if __name__ == "__main__":
	lines = []

	for line in codecs.open(sys.argv[1], encoding='utf-8', errors='ignore'):
			try:
					if len(lines) >= 1000000:
						print('Pushing 1000000')
						multiprocessing.Process(target=pushLines, args=[lines]).start()
						lines = []
					email, password = line.strip().rstrip().split(':')
					lines.append({'username': None, 'password': password, 'email': email, 'database': 'linkedin', 'ip': None})
			except:
					continue

	print('Pushing leftover...')
	pushLines(lines)
	lines = []

#data.insert_one({'username': 'test', 'password': 'testPassword', 'email': 'test@test.com', 'database': 'myspaceTest', 'ip': '127.0.0.1'})