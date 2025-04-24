import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rv_continuous


# Función para la transformada inversa para la densidad f(x) = (b+1)(1-x)^b, 0<x<1
def inv_transform(u, b):
    return 1 - (1 - u) ** (1 / (b + 1))


# Función teórica de densidad
def f(x, b):
    return (b + 1) * (1 - x) ** b


# Función teórica de la CDF
def F(x, b):
    return 1 - (1 - x) ** (b + 1)


# Parámetros y número de muestras
N = 10000
b_values = [2, 5]

# Generar números aleatorios para cada valor de b
u = np.random.rand(N)

plt.figure(figsize=(12, 6))

for i, b in enumerate(b_values, 1):
    # Aplicar la transformada inversa
    x = inv_transform(u, b)

    # Gráficos: Histograma y función de densidad teórica
    plt.subplot(2, 2, 2 * i - 1)
    plt.hist(x, bins=30, density=True, alpha=0.6, label='Histograma')

    x_vals = np.linspace(0, 1, 200)
    plt.plot(x_vals, f(x_vals, b), 'r-', lw=2, label='f(x) teórica')
    plt.title(f'Densidad para b = {b}')
    plt.xlabel('x')
    plt.ylabel('Densidad')
    plt.legend()

    # Gráficos: Función de distribución acumulada teórica vs. empírica
    plt.subplot(2, 2, 2 * i)
    # Función de distribución empírica
    x_sorted = np.sort(x)
    ecdf = np.arange(1, N + 1) / N
    plt.step(x_sorted, ecdf, where='post', label='ECDF empírica')
    plt.plot(x_vals, F(x_vals, b), 'r-', lw=2, label='F(x) teórica')
    plt.title(f'Función acumulada para b = {b}')
    plt.xlabel('x')
    plt.ylabel('F(x)')
    plt.legend()

plt.tight_layout()
plt.show()
