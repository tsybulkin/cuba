# this module provides training functions
#
from state import init_state


TAU = 0.001


def train_epoch(T, Qtab):
	""" x = [a, a1, w]
	"""
	t = 0.
	x = np.array([np.pi, 0., 0.])

	while t < T:

		t += TAU
