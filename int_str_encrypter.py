import random
import json

abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

ABC = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


def encrInt(rnum, dir):
	''' rnum: number to be encryted '''
	''' dir: directory name, without '.json' '''
	try:
		num = rnum
		if rnum:
			strnum = str(rnum)
			nums = []
			for n in strnum:
				n = random.randint(0, 9)
				nums .append(str(n))
			enum = ' '
			for en in nums:
				enum += en

			enum  = int(enum)
			enumdict = {}
			enumdict['key'] = dir
			enumdict['value'] = num
			enumdict['evalue'] = enum

			file = dir + '.json'
			with open(file, 'w') as jf:
				json.dump(enumdict, jf)

			return enum
		else:
			pass
	except:
		return "invalid Int: %s" %rnum
		