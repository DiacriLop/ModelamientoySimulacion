from simlib import mm1
from random import seed
from statistics import mean

Lambda = 1.3
mu = 2
n = 100000  # Número de paquetes a simular

Num_Repl = 50  # Número de replicaciones (repeticiones)
Delay = []  # Conjunto de datos

for i in range(Num_Repl):
    seed()  # Reinicia el generador de números aleatorios
    d = mm1(Lambda, mu, n)  # Simulación N/M/1
    Delay.append(d)