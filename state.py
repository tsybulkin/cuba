#
# this module deals with state of the robot
#



def x_to_state(x):
	"""digitize continious x"""
	return np.int32(x * np.array([50, 50, 5]))


def get_legal_actions(state):
	if state[2] > 1000.: return [-2, -1, 0]
	elif state[2] < -1000.: return [0, 1, 2]
	return [-2, -1, 0 , 1, 2]



	