#
# This module provides modeling the cubli-like robot
#

Mb = 1. 	# the mass of cube body
Md = 0.5	# the mass of the balancing disc
G = 9.81
L = 0.2		# the half diagonal of the cube
R = 0.1		# the disc radius
K = 1. 		# the torque parameter
Wmax = 3000	# the maximum angular velosity of the disk


def control(action):
	return action


def dynamics(x, u, tau):
	"""
	d2a/dt2 = L*G*sin(a) + L/(Mb+Md)*K*u
	Md*R^2*dw/dt = K*u
	"""
