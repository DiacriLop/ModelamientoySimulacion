import numpy as np
import matplotlib.pyplot as plt

# Definición de la función de densidad f(x)
def f(x):
    if 0 <= x < 10:
        return x / 100
    elif 10 <= x < 20:
        return (20 - x) / 100
    else:
        return 0

# Cálculo de la función de distribución acumulada (CDF)
def cdf(x):
    if 0 <= x < 10:
        return (x**2) / 200
    elif 10 <= x < 20:
        return 1 - ((20 - x)**2) / 200
    else:
        return 1

# Generar números aleatorios usando la transformada inversa
def generate_random_numbers(n):
    random_numbers = []
    for _ in range(n):
        u = np.random.uniform(0, 1)  # Genera un número aleatorio uniforme
        if u < 0.5:
            # Si u está en el rango [0, 0.5], se genera un número en el rango [0, 10)
            x = np.sqrt(200 * u)
        else:
            # Si u está en el rango [0.5, 1), se genera un número en el rango [10, 20)
            x = 20 - np.sqrt(200 * (1 - u))
        random_numbers.append(x)
    return np.array(random_numbers)

# Generar números aleatorios
n = 1000000
random_numbers = generate_random_numbers(n)

# Graficar la función de densidad acumulada (CDF)
x_values = np.linspace(0, 20, 1000)
cdf_values = np.array([cdf(x) for x in x_values])

plt.figure(figsize=(10, 6))
plt.plot(x_values, cdf_values, label="Función de distribución acumulada (CDF)", color='blue')
plt.title('Función de distribución acumulada (CDF)')
plt.xlabel('x')
plt.ylabel('CDF(x)')
plt.grid(True)
plt.legend()
plt.show()

# Graficar el histograma de los números aleatorios generados
plt.figure(figsize=(10, 6))
plt.hist(random_numbers, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
plt.title('Histograma de los números aleatorios generados')
plt.xlabel('x')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()
