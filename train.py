# this module provides training functions
#
from state import x_to_state, learn, get_policy
from dynamics import dynamics, control
import numpy as np


TAU = 0.02

def demo(T, Qtab):
	t = 0.
	np.random.seed()
	#x = np.array([np.pi/4, 0., 0.])
	x = np.array([np.random.uniform(-0.1, 0.1), 0., 0.])
	state = x_to_state(x)
	log = []
		
	while t < T:
		print "t:", t, "\tstate", state
		action = get_policy(state, Qtab, eps=0.2)
		u = control(action)

		x = dynamics(x, u, TAU)
		print "action:", action
		state1 = x_to_state(x)
		print "reward:", learn(state, action, state1, Qtab)
		state = state1

		log.append((t,)+tuple(x)+(u,))
		t += TAU
	return log


def train_epoch(T, Qtab):
	t = 0.
	x = np.array([np.random.uniform(-0.1, 0.1), 
				0.,
				 0.])
	state = x_to_state(x)
		
	while t < T:
		#print "t:", t, "\tstate", state
		action = get_policy(state, Qtab, eps=0.3)
		u = control(action)

		x = dynamics(x, u, TAU)
		#print "action:", action, '\tx:', x
		state1 = x_to_state(x)
		learn(state, action, state1, Qtab)
		state = state1

		t += TAU
