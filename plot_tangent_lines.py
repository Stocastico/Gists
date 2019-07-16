# I found a cool plot of sin(x) with tangent lines plotted at equal intervals:
# https://www.reddit.com/r/mathpics/comments/3ki2nh/drawing_thousands_of_tangents/
# This script is for generating a similar plot
#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import time


# function params
xbegin = -4.0*np.pi
xend = 4.0*np.pi
f_thickness = 1

# tangent lines params
num_tangent_lines = 9*20
window_bound_x = 30
# window_bounds = [-window_bound_x, window_bound_x, -window_bound_x*9.0/16.0, window_bound_x*9.0/16.0]
window_bounds = [-window_bound_x, window_bound_x, -2, 2]
tan_thickness = 0.1


def sinc(x):
	if x == 0: return 1
	return np.sin(x)/x

def sinc_prime(x):
	if x == 0: return 0
	return ( x*np.cos(x) - np.sin(x))/(x*x)

def sin(x):
	return np.sin(2.0*x)

def sin_prime(x):
	return 2.0 * np.cos(2.0*x)

def cos(x):
	return np.cos(2.0*x)

def cos_prime(x):
	return -2.0 * np.sin(2.0*x)

def slantsin(x):
	return np.sin(2.0*x) + 0.5*x

def slantsin_prime(x):
	return 2.0 * np.cos(2.0*x) + 0.5

def curvesin(x):
	return np.sin(2.0*x) + 0.05*x**2 - 15.0

def curvesin_prime(x):
	return 2.0 * np.cos(2.0*x) + 0.1 * x

square_iter = 1000

def squarewave(x):
	global square_iter
	val = 0.0
	for i in range(square_iter):
		val += np.sin((2*i+1)*x)/(2*i+1)
	return val

def squarewave_prime(x):
	global square_iter
	val = 0.0
	for i in range(square_iter):
		val += np.cos((2*i+1)*x)
	return val

triangle_iter = 100

def trianglewave(x):
	global triangle_iter
	val = 0.0
	for i in range(triangle_iter):
		if i%2 == 0:
			val += np.sin((2*i+1)*x) / (2*i+1)**2
		else:
			val -= np.sin((2*i+1)*x) / (2*i+1)**2
	return val

def trianglewave_prime(x):
	global triangle_iter
	val = 0.0
	for i in range(triangle_iter):
		if i%2 == 0:
			val += np.cos((2*i+1)*x) / (2*i+1)
		else:
			val -= np.cos((2*i+1)*x) / (2*i+1)
	return val

sawtooth_iter = 1000

def sawtoothwave(x):
	global sawtooth_iter
	val = 0.0
	for i in range(1, sawtooth_iter+1):
		val += -1**i * np.sin(i*x) / i
	return val

def sawtoothwave_prime(x):
	global sawtooth_iter
	val = 0.0
	for i in range(1, sawtooth_iter+1):	
		val += -1**i * np.cos(i*x)
	return val

def plot_function_and_tangents(f, fprime, window, num_tangents):
	global f_thickness, tan_thickness, xbegin, xend

	fig = plt.figure(figsize=(16, 9), dpi=120, facecolor='black')
	ax = fig.add_axes([0,0,1,1])
	ax.axis('off')

	for perc, newx in zip(np.linspace(0, 1, num=num_tangents), np.linspace(xbegin, xend, num=num_tangents)):
		linex = np.linspace(window[0], window[1])
		liney = fprime(newx) * linex + (f(newx) - fprime(newx)*newx)
		ax.plot(linex, liney, color=(perc, 0, 1-perc/2), linewidth=tan_thickness)
		# ax.plot(linex, liney, color=(0, 0, 1), linewidth=tan_thickness)

	x = np.linspace(xbegin, xend, num=1000)
	ax.plot(x, map(f, x), 'w', linewidth=f_thickness)

	# ax.plot(x, [np.pi/2.0]*x.size, 'w')
	# ax.plot(x, [-np.pi/2.0]*x.size, 'w')

	ax.axis(window)

starttime = time.time()

# plot_function_and_tangents(sinc, sinc_prime, window_bounds, num_tangent_lines)
# plt.savefig('output.png', facecolor='black', transparent=True, dpi=120)

# window_bound_x = 8.0*np.pi + 0.5
# window_bounds = [-window_bound_x, window_bound_x, -window_bound_x*9.0/16.0*2.0, window_bound_x*9.0/16.0*2.0]
# plot_function_and_tangents(cos, cos_prime, window_bounds, 9*5000)
# plt.savefig('output2.png', facecolor='black', transparent=True, dpi=120)


# Square Wave
# plot_function_and_tangents(squarewave, squarewave_prime, window_bounds, 10000)
# plt.savefig('output.png', facecolor='black', transparent=True, dpi=120)

# Triangle Wave
# tan_thickness = 0.01
# plot_function_and_tangents(trianglewave, trianglewave_prime, window_bounds, 100000)
# plt.savefig('output.png', facecolor='black', transparent=True, dpi=120)

# Sawtooth Wave
tan_thickness = 0.01
plot_function_and_tangents(sawtoothwave, sawtoothwave_prime, window_bounds, 100000)
plt.savefig('output.png', facecolor='black', transparent=True, dpi=120)







endtime = time.time()
print("Took " + str(endtime - starttime) + " seconds to plot.")
