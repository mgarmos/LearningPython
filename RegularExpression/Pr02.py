# -*- coding: utf-8 -*-

# Search for lines that contain 'From'
# import re
# hand = open('My Clippings.txt',encoding="Latin-1")
# for line in hand:
	# line = line.rstrip()
	# print(line)
		

# hand.close()

encodings = ['ISO-8859-1','ANSI', 'cp1252', 'windows-1250', 'windows-1252', 'utf-8']
for e in encodings:
	try:
		fh = open('My Clippings.txt', 'r', encoding=e)
		fh.readlines()
		fh.seek(0)
	except UnicodeDecodeError:
		print('got unicode error with %s , trying different encoding' % e)
	else:
		print('opening the file with encoding:  %s ' % e)
		break

# for line in fh:
	# line = line.rstrip()
	# print(line)
	
fh.close()	
				
