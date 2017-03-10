#
# This module provides modeling the cubli-like robot
#
import numpy as np

Mb = 1. 	# the mass of cube body
Md = 0.5	# the mass of the balancing disc
G = 9.81
L = 0.2		# the half diagonal of the cube
R = 0.1		# the disc radius
K = 1. 		# the torque parameter
Wmax = 3000	# the maximum angular velosity of the disk
Z = 10. 		# torque parameter


def control(action):
	return Z * action


def dynamics(x, u, tau):
	"""
	d2a/dt2 = L*G*sin(a) + L^2/(Mb+Md)*K*u
	Md*R^2*dw/dt = K*u
	"""
	a, da, w = x
	
	d2a = L * G * np.sin(a) + K / (Mb + Md) * u
	da += d2a * tau
	a += da * tau
	if a < -np.pi/4:
		a = -np.pi/4
		da = 0.
	elif a > np.pi/4:
		a = np.pi/4
		da = 0

	w += K / Md / R**2 * u

	return np.array([a, da, w])


