import random
import numpy as np
import matplotlib.pyplot as plt

casosFA = [0,1]
probabilidadFA=[0.2,0.8]

N=200000
cantidadCobros = 5
casos = np.array ([i for i in range(0,cantidadCobros)])
frecuenciaAbsoluta = np.zeros(len(casos))
frecuenciaRelativa = np.zeros(len(casos))


for i in range(0,N):
    cobro = [random.choices(casosFA,probabilidadFA)[0] for k in range(0,cantidadCobros)]
    if cobro[0] == 1:
        frecuenciaAbsoluta[0] += 1

    elif cobro[1] == 1:
        frecuenciaAbsoluta[1] += 1

    elif cobro[2] == 1:
        frecuenciaAbsoluta[2] += 1

    elif cobro[3] == 1:
        frecuenciaAbsoluta[3] += 1

    elif cobro[4] == 1:
        frecuenciaAbsoluta[4] += 1

frecuenciaRelativa = frecuenciaAbsoluta / N
print(frecuenciaRelativa)

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.bar(casos, frecuenciaRelativa , color="skyblue", edgecolor="black")
plt.xlabel('Cantidad de Cobros antes del acierto')
plt.ylabel("distribucion de probabilidad")
plt.show()

frecuenciaAcumulada = np.zeros_like(frecuenciaRelativa)

for i in range (len(frecuenciaAcumulada)):
    for j in range(0,i +1):
        frecuenciaAcumulada[i] += frecuenciaRelativa[j]
    print("distribucion de probabilidad acumulada",frecuenciaRelativa)

    fig = plt.figure()
    ax = fig.add_axes([0.1,0.1,0.8,0.8])
    plt.xlabel("Cantidad de cobros antes del acierto")
    plt.ylabel("Distribucion de probabilidad acumulada")
    ax.bar(casos,frecuenciaAcumulada, color="plum", edgecolor="black")
    plt.show()