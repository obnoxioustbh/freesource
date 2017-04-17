from codecs import open

file = open('lizard.txt', errors='ignore', encoding='utf-8')
parsed = open('lizard_parsed', 'w')

for line in file:
	try:
		uid, username, password, email = line.split('VALUES (')[1].split(')')[0].strip().rstrip().lower().replace("'", '').split(',')[0:4]
		parsed.write('{0} {1} {2} {3} lizardsquad\n'.format(uid, username, password, email))
	except:
		continue

parsed.close()