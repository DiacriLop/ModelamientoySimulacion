import random
import numpy as np
import matplotlib.pyplot as plt

N = 20000

casos = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
contador = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

for i in range(0, N):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    dado3 = random.randint(1, 6)
    suma = dado1 + dado2 + dado3
    contador[suma] += 1
print("sumas por casos", contador)

frecuenciaRelativa = contador / N

print("frecuencia relativa", frecuenciaRelativa)
print("casos de sumas", casos)

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])  # Define el área de la gráfica
ax.bar(casos, frecuenciaRelativa)  # Crea un gráfico de barras con las frecuencias relativas
plt.bar(casos, frecuenciaRelativa)  # Otra forma de graficar barras con matplotlib
ax.bar(casos, frecuenciaRelativa, color='pink')

# Etiquetas para los ejes
plt.xlabel("casos")
plt.ylabel("distribucion de probabilidad")

# Muestra el gráfico
plt.show()