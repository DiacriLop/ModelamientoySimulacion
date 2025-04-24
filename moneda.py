import random  # Importa la librería random para generar valores aleatorios
import numpy as np  # Importa numpy para cálculos numéricos eficientes
import matplotlib.pyplot as plt  # Importa matplotlib para la visualización de datos

N = 2000000  # Número de simulaciones o experimentos
cantidad_lanzamientos = 10  # Número de lanzamientos de moneda por experimento

# Define los posibles valores de aciertos (de 0 a la cantidad de lanzamientos)
casos = np.array([i for i in range(0, cantidad_lanzamientos + 1)])

# Inicializa los arreglos de frecuencia absoluta y relativa
f_absoluta = np.zeros(len(casos))  # Frecuencia absoluta de cada cantidad de aciertos
f_relativa = np.zeros(len(casos))  # Frecuencia relativa de cada cantidad de aciertos

# Arreglo auxiliar para almacenar los lanzamientos de cada experimento
lanzamiento = np.zeros(cantidad_lanzamientos)

# Simulación de los experimentos
for i in range(0, N):
    # Simula una serie de lanzamientos de moneda (0 = fallo, 1 = acierto)
    lanzamiento = [random.randint(0, 1) for j in range(0, len(lanzamiento))]

    # Suma la cantidad de aciertos en los lanzamientos
    suma_de_aciertos = np.sum(lanzamiento)

    # Incrementa la frecuencia absoluta de esa cantidad de aciertos
    f_absoluta[suma_de_aciertos] += 1

# Calcula el total de lanzamientos realizados
Total_de_lanzamientos = cantidad_lanzamientos * N

# Calcula la frecuencia relativa dividiendo por el total de lanzamientos
f_relativa = f_absoluta / Total_de_lanzamientos

# Muestra la distribución de probabilidad
print("distribucion de probabilidad", f_relativa)

# Creación de la gráfica
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # Define el área de la gráfica
ax.bar(casos, f_absoluta)  # Crea un gráfico de barras con la frecuencia absoluta

# Etiquetas para los ejes
plt.xlabel("numero de aciertos")
plt.ylabel("distribucion de probabilidad")

# Muestra la gráfica
plt.show()
