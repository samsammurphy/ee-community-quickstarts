# usages:
# $ python ee-index.py [your repo folder]
import os, sys
for f in os.popen('find ee-examples').read().splitlines():
	if f.find('.git') != -1: continue
	if f.find('README.md') != -1: continue
	if os.path.isdir(f):
		print '## ', f.lstrip('ee-examples')
	elif os.path.isfile(f):
		print '[%s](%s)' % (os.path.basename(f), f.lstrip('ee-examples/'))
		flag = True
		for line in open(f):
			if line.startswith('//'):
				if line.replace('/','').strip() == '': continue
				print '\t', line.lstrip('/'),
			else:
				print
				break
