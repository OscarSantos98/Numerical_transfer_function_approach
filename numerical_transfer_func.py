import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sympy as sp
from scipy import linspace
from scipy.signal import lti, step, TransferFunction

# Matplotlib style
plt.style.use("ggplot")

# Read data from csv file
csv_data = pd.read_csv("assets/data.csv")
print(csv_data)

time = csv_data['TIME']
oven_temperature = csv_data['OV1(T)']
time_array = np.array(time)
unnormalized_temperature_array = np.array(oven_temperature)

# Normalize values to [0, 1]
abs_max = np.amax(np.abs(unnormalized_temperature_array))
normalized_temperature_array = unnormalized_temperature_array / abs_max
step_data = np.vstack((time_array,normalized_temperature_array))
# print(step_data.shape)

# Plots
# First figure
plt.plot(step_data[0], step_data[1], marker='x', markersize=2, linestyle='None')
plt.xlabel('Time')
plt.ylabel('Normalized temperature')
plt.title("Experiment")
# plt.grid(True)
plt.tight_layout()
plt.show()

# Second figure
plt.plot(step_data[0], step_data[1], marker='x', markersize=2, linestyle='-', label="Data from Proteus's oven")
plt.axhline(0.283, c='k', linestyle='--')		# 
plt.axhline(0.632, c='k', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Normalized temperature')
plt.title("Experiment")
# plt.grid(True)
plt.tight_layout()
plt.show()

# Find T and L values which are necessary to evaluate a transfer function approach
t1=13.6383				# hard-coded values from the previous figure
t2=20.3296				# hard-coded values from the previous figure
T=3*(t2-t1)/2			# from control-theory
L=t2-T					# from control-theory

# Calculate and print transfer function approach
s = sp.Symbol('s')
Ghat = sp.exp(-L*s)/(1+T*s);
print("\nTransfer function approach\nG\u0302(s) = {}".format(Ghat))

# As step can not be apply directly in Python when s is found as exponent e^(-Ls) we separate this term for now. 
sys = lti([1],[T, 1])
t, y = step(sys)

# Third figure
plt.plot(step_data[0], step_data[1], marker='x', markersize=2, linestyle='-', label="Data from Proteus's oven")
# From inverse laplace transform we know e^(-Ls) can be applied as displacement in time, so that is why L is added to the array time
plt.plot(t+L, y, label="Step response to Transfer Function")
plt.xlabel('Time');
plt.ylabel('Normalized temperature')
plt.title("Experiment vs Model")
# plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Calculate gains of PID Controller
kp = 1.2*T/L
ki = kp/(2*L)
kd = 0.5*kp*L
print('Suggested PID controller')
print("kp={},\tki={},\tkd={}".format(kp,ki,kd))