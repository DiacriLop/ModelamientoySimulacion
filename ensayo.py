import numpy as np
import matplotlib.pyplot as plt


def generadorEstandarMinimo(num_valores, semilla=1):

    a = 16807
    m = 2 ** 31 - 1  # 2147483647
    x_actual = semilla
    valores_uniformes = []

    for _ in range(num_valores):
        x_actual = (a * x_actual) % m
        valores_uniformes.append(x_actual / m)

    return valores_uniformes


def generarExponencialInversa(lamda, numeros_uniformes):

    return [(1.0 / lamda) * np.log(u) for u in numeros_uniformes]


def main():

    num_iteraciones = 200000
    lamda = -1.5
    semilla_inicial = 42

    numeros_uniformes = generadorEstandarMinimo(num_iteraciones, semilla_inicial)

    datos_exponenciales = generarExponencialInversa(lamda, numeros_uniformes)

    # Visualizamos el histograma de los datos generados
    plt.hist(datos_exponenciales, bins=400, density=True , color='pink')
    plt.title("Histograma de datos generados (Transformada Inversa)")
    plt.xlabel("Valor")
    plt.ylabel("Densidad")
    plt.show()


if __name__ == "__main__":
    main()

