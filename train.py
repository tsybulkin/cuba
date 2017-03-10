# this module provides training functions
#
from state import x_to_state, learn, get_policy
from dynamics import dynamics, control


TAU = 0.01


def train_epoch(T, Qtab):
	""" d2a/dt2 = L*G*sin(a) + L/(mb+md)*U
	"""
	t = 0.
	x = np.array([np.pi/4, 0., 0.])

	while t < T:
		state = x_to_state(x)
		print "t:", t, "\tstate", state
		action = get_policy(state, Qtab)
		u = control(action)

		x1 = dynamics(x, u, TAU)
		state1 = x_to_state(x1)
		learn(state, action, state1, Qtab)

		t += TAU
