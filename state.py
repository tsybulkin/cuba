#
# this module deals with state of the robot
#
import numpy as np
import random

GAMA = 0.95
LRATE = 0.3



def x_to_state(x):
	"""digitize continious x"""
	return np.int32(x[:2] * np.array([15, 15]))


def get_legal_actions(state):
	#if state[2] > 50.: return [-3, -1, 0]
	#elif state[2] < -50.: return [0, 1, 3]
	return [-3, -1, 0, 1, 3]


def get_policy(state, Qtab, eps=0.):
	if flip_coin(eps):
		return get_random_policy(state)

	actions = get_legal_actions(state)
	Vmax = max( [Qtab.get((tuple(state),a), 0.) for a in actions])
	return random.choice([ a for a in actions if Qtab.get((tuple(state),a), 0.) == Vmax ])



def get_random_policy(state):
	return random.choice(get_legal_actions(state))



def learn(state, action, state1, Qtab):
	V = Qtab.get((tuple(state), action), 0.)
	V1 = max( Qtab.get((tuple(state1),a), 0.) for a in get_legal_actions(state1) )
	R = reward(state, action, state1)
	Qtab[ (tuple(state), action) ] = (1 - LRATE) * V + LRATE * (R + GAMA * V1)
	#print "state value:", V
	return R


def reward(state, action, state1):
	if abs(state1[0]) > 9:
		return -50.
	return 3 - 0.1*abs(action) + 0.1*(state[0]**2 - state1[0]**2)


def flip_coin(p):
	return random.random() < p



