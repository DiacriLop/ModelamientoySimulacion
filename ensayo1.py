import numpy as np
import matplotlib.pyplot as plt


multiplicador = 7**5
modulo = 2**31 - 1
semilla = 42
N = 200000
lamda = -1.5

def generadorCongruenteMulp(semilla, n):
    numeros = []
    for _ in range(n):
        semilla = (multiplicador * semilla) % modulo
        numeros.append(semilla / modulo)
    return numeros

numAleatorios = generadorCongruenteMulp(semilla, N)

datosExponenciales = [(1 / lamda) * np.log(x) for x in numAleatorios]

plt.hist(datosExponenciales, bins=400, density=True)
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.title('Histograma de distribución exponencial')
plt.show()
