import numpy as np
import matplotlib.pyplot as plt


N = 1000000
U = np.random.rand(N)

X = U**(2/3)


plt.figure(figsize=(10, 6))

plt.hist(X, bins=500, density=True, alpha=0.6, color='g', edgecolor='black')

x_vals = np.linspace(0, 1, 500)
f_vals = (3/2) * np.sqrt(x_vals)

plt.plot(x_vals, f_vals, 'r', lw=2, label='Densidad teórica')

plt.title("Histograma de X = U^(2/3) y función de densidad teórica")
plt.xlabel("X")
plt.ylabel("Densidad (normalizada)")
plt.legend()
plt.grid(True)
plt.show()
