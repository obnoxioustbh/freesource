import codecs
import sys
import time

file = codecs.open(sys.argv[1], 'r', errors='ignore').readlines()
while True:
	time.sleep(1)
print('Opened')
