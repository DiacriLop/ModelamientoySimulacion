# simLib es tu biblioteca de simulación, que reutilizarás
# en tus tareas y proyectos.
# Está disponible en el repositorio de GitHub

from simLib import mm1
from random import seed
from statistics import mean

lamda = 1.3
mu = 2
n = 100000  # Número de paquetes a simular

Num_Rep1 = 50  # Número de replicaciones (repeticiones)
Delay = []  # Conjunto de datos

for i in range(Num_Rep1):
    seed()  # Reinicia el generador de números aleatorios
    d = mm1(lamda, mu, n)  # Simulación M/M/1
    Delay.append(d)

# Estimación de la medida de desempeño
print("Average Delay = ", round(mean(Delay), 4))