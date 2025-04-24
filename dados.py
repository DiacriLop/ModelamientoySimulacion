import random  # Importa la librería random para generar números aleatorios
import numpy as np  # Importa numpy para manipulación de arreglos y cálculos numéricos
import matplotlib.pyplot as plt  # Importa matplotlib para visualización de datos

N = 200000  # Número de simulaciones o lanzamientos de los dados

# Arreglo que representa los posibles valores de la suma de dos dados (mínimo 2, máximo 12)
casos = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])

# Contador para registrar la frecuencia de cada suma posible
contador = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0])

# Simulación de lanzamientos de dos dados
for i in range(0, N):
    dado1 = random.randint(1, 6)  # Genera un número aleatorio entre 1 y 6 para el primer dado
    dado2 = random.randint(1, 6)  # Genera un número aleatorio entre 1 y 6 para el segundo dado
    suma = dado1 + dado2  # Calcula la suma de los dos dados
    contador[suma] += 1  # Incrementa el contador de la suma obtenida

# Muestra el número de veces que ocurrió cada suma
print("sumas por casos", contador)

# Calcula la frecuencia relativa dividiendo la cantidad de veces entre el total de simulaciones
fr = contador / N

# Imprime la frecuencia relativa de cada suma
print("frecuencia relativa", fr)
print("casos de sumas", casos)

# Crea una nueva figura para la gráfica
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])  # Define el área de la gráfica
ax.bar(casos, fr)  # Crea un gráfico de barras con las frecuencias relativas
plt.bar(casos, fr)  # Otra forma de graficar barras con matplotlib

# Etiquetas para los ejes
plt.xlabel("casos")
plt.ylabel("distribucion de probabilidad")

# Muestra el gráfico
plt.show()