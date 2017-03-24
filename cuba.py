# This program simulates dynamics of cubli-robot
#   -- link --
# 

import numpy as np
import cPickle
import sys, os
from train import train_epoch, demo
from matplotlib import pyplot as plt


def run(t=5):
	Qtab = load_Qtab()

	data = demo(t, Qtab)
	[T, A, A1, W, U] = zip(*data)
	
	# plt.title()
	# plt.plot(T,A,'-')
	# plt.show()
	plt.figure(1)
	plt.title('simulation results')
	plt.subplot(311)
	plt.ylabel('angle')
	plt.plot(T,A,'b-')

	plt.subplot(312)
	plt.ylabel('wheel rotation')
	plt.plot(T,W,'r--')

	plt.subplot(313)
	plt.ylabel('robot control')
	plt.plot(T,U,'k')

	plt.show()


def train(epoch=1000, t=5):
	Qtab = load_Qtab()
	se = len(Qtab)

	for ep in xrange(epoch):
		if ep % 100 == 0:
			print ep, "done"

		train_epoch(t, Qtab)

	print len(Qtab)-se, "new states-actions explored" 
	f = open("Qtab.data",'wb')
	cPickle.dump(Qtab, f)
	f.close

	return Qtab


def load_Qtab():
	if not os.path.isfile('Qtab.data'):
		return {}

	f = open("Qtab.data",'rb')
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
	np.random.seed()

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
		if len(args) == 3:
			t = float(args[2])
			run(t)
		else:
			print warning
	else:
		print warning




