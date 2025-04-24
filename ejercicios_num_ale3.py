import numpy as np
import matplotlib.pyplot as plt


# 1) Transformada inversa (función por tramos)
def inv_transform(u):
    """
    Parámetros:
        u: array de valores uniformes en [0,1).
    Retorna:
        x: array con la misma forma que u,
           con valores siguiendo la densidad dada.
    """
    x = np.zeros_like(u)

    # Primer tramo: 0 <= u < 0.5 => x = sqrt(200u)
    mask1 = (u < 0.5)
    x[mask1] = np.sqrt(200.0 * u[mask1])

    # Segundo tramo: 0.5 <= u < 1 => x = 20 - 10*sqrt(2)*sqrt(1-u)
    mask2 = ~mask1  # (u >= 0.5)
    x[mask2] = 20.0 - 10.0 * np.sqrt(2) * np.sqrt(1.0 - u[mask2])

    return x


# 2) Función de densidad (piecewise)
def f(x):
    """
    f(x) = x/100,        0 <= x < 10
         = (20 - x)/100, 10 <= x < 20
         = 0,            en otro caso
    """
    x = np.asarray(x)
    fx = np.zeros_like(x)

    # 0 <= x < 10
    mask1 = (x >= 0) & (x < 10)
    fx[mask1] = x[mask1] / 100.0

    # 10 <= x < 20
    mask2 = (x >= 10) & (x < 20)
    fx[mask2] = (20.0 - x[mask2]) / 100.0

    return fx


# 3) Función de distribución acumulada (CDF) (piecewise)
def F(x):
    """
    F(x) =  0,                         x < 0
         =  x^2/200,                  0 <= x < 10
         =  1/2 + (1/100)(20x - x^2/2 - 150), 10 <= x < 20
         =  1,                         x >= 20
    """
    x = np.asarray(x)
    Fx = np.zeros_like(x)

    # x < 0 => 0
    mask0 = (x < 0)
    Fx[mask0] = 0.0

    # 0 <= x < 10 => x^2/200
    mask1 = (x >= 0) & (x < 10)
    Fx[mask1] = (x[mask1] ** 2) / 200.0

    # 10 <= x < 20 => -1 + 0.2x - x^2/200  (o la forma "1/2 + ...")
    mask2 = (x >= 10) & (x < 20)
    Fx[mask2] = -1.0 + 0.2 * x[mask2] - (x[mask2] ** 2) / 200.0

    # x >= 20 => 1
    mask3 = (x >= 20)
    Fx[mask3] = 1.0

    return Fx


# 4) Generación y validación
def generar_y_validar(N=10000):
    # 4.1 Generar valores uniformes
    u = np.random.rand(N)

    # 4.2 Transformar con la inversa
    x = inv_transform(u)

    # 4.3 Histograma vs densidad teórica
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.hist(x, bins=30, density=True, alpha=0.6, label='Histograma')
    x_vals = np.linspace(0, 20, 300)
    plt.plot(x_vals, f(x_vals), 'r-', lw=2, label='f(x) teórica')
    plt.title('Histograma vs. f(x)')
    plt.xlabel('x')
    plt.ylabel('Densidad')
    plt.legend()

    # 4.4 CDF empírica vs CDF teórica
    plt.subplot(1, 2, 2)
    x_sorted = np.sort(x)
    ecdf = np.arange(1, N + 1) / N
    plt.step(x_sorted, ecdf, where='post', label='ECDF empírica')
    plt.plot(x_vals, F(x_vals), 'r-', lw=2, label='F(x) teórica')
    plt.title('CDF empírica vs. F(x)')
    plt.xlabel('x')
    plt.ylabel('F(x)')
    plt.legend()

    plt.tight_layout()
    plt.show()


# 5) Ejecución principal (punto c)
if __name__ == "__main__":
    generar_y_validar(N=10000)
