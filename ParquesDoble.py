import random
import matplotlib.pyplot as plt
import numpy as np

N = 1000000

primer_intento = 0
segundo_intento = 0
tercer_intento = 0

for _ in range(N):

    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    if dado1 == dado2:
        primer_intento += 1
        continue

    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    if dado1 == dado2:
        segundo_intento += 1
        continue

    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    if dado1 == dado2:
        tercer_intento += 1
        continue


sim_primer = primer_intento / N
sim_segundo = segundo_intento / N
sim_tercer = tercer_intento / N

print("Probabilidades teóricas:")
print("Intento 1: {:.4f}".format(1 / 6))
print("Intento 2: {:.4f}".format(5 / 36))
print("Intento 3: {:.4f}".format(25 / 216))
print("\nProbabilidades simuladas:")
print("Intento 1: {:.4f}".format(sim_primer))
print("Intento 2: {:.4f}".format(sim_segundo))
print("Intento 3: {:.4f}".format(sim_tercer))

# Gráfica de comparación
intentos = ['Intento 1', 'Intento 2', 'Intento 3']
teorico = [1 / 6, 5 / 36, 25 / 216]
simulado = [sim_primer, sim_segundo, sim_tercer]

x = np.arange(len(intentos))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, teorico, width, label='Teórico', color='pink')
rects2 = ax.bar(x + width / 2, simulado, width, label='Simulado', color='plum')

ax.set_ylabel('Probabilidad')
ax.set_title('Probabilidad de obtener dobles en cada intento')
ax.set_xticks(x)
ax.set_xticklabels(intentos)
ax.legend()

plt.show()
