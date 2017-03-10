# this module provides training functions
#
from state import x_to_state, learn, get_policy
from dynamics import dynamics, control
import numpy as np


TAU = 0.01


def train_epoch(T, Qtab):
	""" d2a/dt2 = L*G*sin(a) + L/(mb+md)*U
	"""
	t = 0.
	x = np.array([np.pi/4, 0., 0.])
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
