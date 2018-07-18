#python

def fromatt(string, start=''):
	print('{start} {string}'.format(
		start=start, string=string
		)
	)	

def info(string, start='[+]'):
	fromatt(string=string, start=start)

def error(string, start='[-]'):
	fromatt(string=string, start=start)

