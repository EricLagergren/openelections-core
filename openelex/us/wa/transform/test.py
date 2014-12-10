import re

#string = 'State Representative District #21 []'

strings = [
	'State House of Representatives Position #2',
	'State House of Representatives Pos 2',
	'State House of Representatives Pos. 1',
	'State House of Representatives Pos_2',
	'State House of Representatives Pos-1',
	'State House of Representatives Pos no 3',
	'State House of Representatives Position no. 2',
	'State House of Representatives District #23',
	]


regex = re.compile(r'pos(ition|)(|\s|\.|_|-)(\s|)(no\.|no|)(\s|)(#|)(\d)', re.IGNORECASE)

for s in strings:
	try:
		print "{} {}".format(strings.index(s), re.search(regex, s).groups())
	except AttributeError:
		print "{} {}".format(strings.index(s), None)

"""for g in re.search(regex, string).groups():
	try:
		print int(g)
	except Exception,e:
		pass

print re.search(regex, string).groups()"""