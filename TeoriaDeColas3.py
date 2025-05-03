from simLib import out_var_cum_mm1
from random import seed
import matplotlib.pyplot as plt
import numpy as np

lamda = 1.3  # Changed from 'lambda' (Python keyword) to 'lamda'
mu = 2

n = 10000  # Number of packets to be simulated
R = 5  # Number of replications (repetitions)

Y = np.zeros(shape=(R, n))  # Output variable Delay

# 1. Generate sample paths
for i in range(R):
    seed()
    Y[i] = out_var_cum_mm1(lamda, mu, n)  # Consistent variable name

# 2. Compute the mean
Z = []  # Changed to uppercase Z to match plot command
for i in range(n):
    Z.append(sum(Y[:, i]) / R)

# Plot Y and Z
plt.plot(Y[0], "k--", label="Y[0]")
plt.plot(Y[1], "k--", label="Y[1]")
plt.plot(Y[2], "k--", label="Y[2]")
plt.plot(Y[3], "k--", label="Y[3]")
plt.plot(Y[4], "k--", label="Y[4]")
plt.plot(Z, "k", linewidth=2, label="Z")  # Now matches the variable name

plt.xlabel("$n$", size=16)
plt.ylabel("$W_{cum}$", size=16)
plt.legend(loc='upper right', shadow=True)
plt.show()