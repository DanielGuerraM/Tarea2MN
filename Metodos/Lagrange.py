import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

def Metodo_Lagrange(x, y1, y2):
    # Creamos una variable en la cual almacenamos el polinomio de lagrange
    # Creamos una variable en la cual almacenamos el polinomio de lagrange
    polinomio_1 = lagrange(x, y1)
    polinomio_2 = lagrange(x, y2)

    # Imprimimos por consola el polinomio
    print(polinomio_1)
    print(polinomio_2)

    # Evaluar el polinomio en un punto
    # valor_interpolado = polinomio(2.5)
    # print(valor_interpolado)

    x_interp_1 = np.linspace(x.min(), x.max(), 100)
    x_interp_2 = np.linspace(x.min(), x.max(), 100)

    y_interp_1 = polinomio_1(x_interp_1)
    y_interp_2 = polinomio_2(x_interp_2)

    # Graficar los puntos originales y el polinomio interpolado
    plt.scatter(x, y1, color='red', marker='*', label='Dias')
    plt.scatter(x, y2, color='red', marker='*', label='Dias')

    plt.plot(x_interp_1, y_interp_1, color='blue', label='Peso promedio m1')
    plt.plot(x_interp_2, y_interp_2, color='yellow', label='Peso promedio m2')

    plt.xlabel('Día')
    plt.ylabel('Peso Promedio(mg)')
    plt.title('Interpolación con polinomio de lagrange')

    # Mostrar la gráfica
    plt.legend()
    plt.show()