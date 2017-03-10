#
# this module deals with state of the robot
#

GAMA = 0.95
LRATE = 0.3



def x_to_state(x):
	"""digitize continious x"""
	return np.int32(x * np.array([50, 50, 5]))


def get_legal_actions(state):
	if state[2] > 1000.: return [-2, -1, 0]
	elif state[2] < -1000.: return [0, 1, 2]
	return [-2, -1, 0 , 1, 2]


def get_policy(state, Qtab, eps=0.):
	if flip_coin(eps):
		return get_random_policy(state)

	actions = get_legal_actions(state)
	i = np.argmax( Qtab.get((state,a), 0.) for a in actions)
	return actions[i]



def get_random_policy(state):
	return np.random.choice(get_legal_actions(state))



def learn(state, action, state1, Qtab):
	V = Qtab.get((state, action), 0.)
	V1 = max( Qtab.get((state1,a)) for a in get_legal_actions(state1) )
	R = reward(state, action, state1)
	Qtab[(state, action)] = (1 - LRATE) * V + LRATE * (R + GAMA * V1)





