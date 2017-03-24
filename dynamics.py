#
# This module provides modeling the cubli-like robot
#
import numpy as np
from matplotlib import pyplot as plt


Mb = 1. 	# the mass of cube body
Md = 0.5	# the mass of the balancing disc
G = 9.81
L = 0.2		# the half diagonal of the cube
R = 0.1		# the disc radius
K = 1. 		# the torque parameter
Wmax = 3000	# the maximum angular velosity of the disk
Z = 0.5		# torque parameter


def run(T):
	a, da, w = np.pi/4, 0., np.sqrt(2*(L-L/np.sqrt(2))*(Md+Mb)*G/Md/R**2)
	t, tau = 0., 0.001
	u = -55.
	log = []

	while t < T:
		a,da,w = dynamics((a,da,w), u , tau)
		if w < 0:
			u = 0.
		log.append((t,a,da,w,u))
		t += tau

	show(log)


def show(log):
	[T,A,dA,W,U] = zip(*log)
	# Two subplots, the axes array is 1-d
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


def control(action):
	return Z * action


def dynamics(x, u, tau):
	"""
	d2a/dt2 = G/L*sin(a) + 1/((Mb+Md)*L^2)*K*u
	Md*R^2*dw/dt = K*u
	"""
	a, da, w = x
	
	d2a = (np.sqrt(2.)*(Md + Mb)*G * L * np.sin(a) + K*u) / (2.5*Mb + 2*Md) / L**2 
	da += d2a * tau
	a += da * tau
	if a < -np.pi/4:
		a = -np.pi/4
		da = 0.
	elif a > np.pi/4:
		a = np.pi/4
		da = 0.

	w += K * u * tau / (Md * R**2) 

	return np.array([a, da, w])

if __name__ == "__main__":
	run(1)
