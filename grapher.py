import os
import numpy as np
import matplotlib.pyplot as plt

# Equation: DelM = -(ILB*sin(phi)/g)
#Change phi
degree = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90]
mass = [71.39,71.49,71.59,71.69,71.80,71.88,71.97,72.06,72.13,72.20,72.27,72.33,72.38,72.43,72.47,72.50,72.51,72.51,72.53]
amp = 2.5
mag_field = 405 #gauss
mag_uncertainty = 50 #+-

#Statistical Error
amp = 4.8
no_current_mass = [70.87,70.84,70.58,70.60,70.54,70.50,71.02,74.26,70.76,71.23]
current_mass = [72.54,78.44,72.61,72.63,72.58,72.50,73.00,75.27,68.74,72.53]

#Change L
num_sides =[3,10,12,7,5,5]
length = [8.2,24.2,21.0,13.6,12.2,8.8]
mass_change = [0.00,-0.07,-0.05,-0.03,-0.03,-0.01]
amp = 2.5
volt = 0.3
mass = 164.83
uncertainty = 0.2 #cm

#Change I
length = 8.48
weight = 91.22
amps = [0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,4.9]
volts = [0.1,0.1,0.2,0.2,0.3,0.3,0.4,0.5,0.5,0.6]
change = [0.0,0.0,-0.01,-0.03,-0.05,-0.07,-0.10,-0.12,-0.14,-0.17]

# Changing B
length = 8.48
amp = 4.9
volt = 0.6
mass_change = [-0.17,-26.53,-39.52,-51.91,-78.61,-64.77,-13.07]
num_magnets = [6,4,3,2,0,1,5]
mass_of_magnets = [13.36,13.18,13.18,13.06,13.21,13.12]
magnet_strength = [580,600,620,560,570,600]
manget_error = 50 #+-
