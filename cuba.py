# This program simulates dynamics of cubli-robot
#   -- link --
# 

import numpy as np
import cPickle
import sys, os
from train import train_epoch


def run(t=5):
	## load Qtab

	data = demo(t=5)
	[t, a, a1, w, u] = zip(*data)

	## show graphs


def train(epoch=1000, t=5):
	Qtab = load_Qtab()

	for ep in xrange(epoch):
		if ep % 100 == 0:
			print ep, "done"

		train_epoch(t, Qtab)

	f = open("Qtab.data",'wr')
	cPickle.dump(Qtab, f)
	f.close

	return Qtab


def load_Qtab():
	if not os.path.isfile('Qtab.data'):
		return {}

	f = open("Qtab.data",'b')
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
		if len(args) == 4:
			epoch = int(args[2])
			t = float(args[3])
			train(epoch=epoch, t=t)
		else:
			print warning

	elif args[1] == 'demo':
		pass

	else:
		print warning




