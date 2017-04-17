from codecs import open

for line in open('lastfm.txt', 'r', encoding='utf-8', errors='ignore'):
	try:
		uid, username, email, password = line.strip().rstrip().split('\t')[0:4]
		string = "{0} {1} {2} {3} lastfm"
		print(string.format(uid, username, email, password), file=open('lastfm_parsed', 'a'))
	except:
		continue