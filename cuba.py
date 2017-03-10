# This program simulates dynamics of cubli-robot
#   -- link --
# 

import numpy as np
import cPickle
import sys, os


def run(t=5):
	## load Qtab

	data = demo(t=5)
	[t, a, a1, w, u] = zip(*data)

	## show graphs


def train(epoch=1000, t=5):
	## load Qtab

	for ep in xrange(epoch):
		if ep % 100 == 0:
			print ep, "done"

		train_epoch(t, Qtab)

	## dump Qtab

	return Qtab


def load_Qtab():
	if not os.path('Qtab.data'):
		return "initialize Qtab"

	with open("Qtab.data",'b') as f:
		Qtab = cPickle.load(f)
	f.close()

	return Qtab



if __name__ == '__main__':
	args = sys.argv[:]
	warning = """
USAGE:
for training: python cuba.py train n t
	where:	n = number of epochs; default value 1000 
	t = simulation time of each epoch; default value 5 sec
			
for demo: python cuba.py demo t
	where: t = time of simulation, default value 5 sec
	"""

	if len(args) == 1:
		print warning

	elif args[1] == 'train':
		pass

	elif args[1] == 'demo':
		pass

	else:
		print warning




