import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


def Metodo_Trazadores_lineales(x, y1, y2):
    # Crear una función de interpolación con trazadores lineales
    f_1 = interp1d(x, y1, kind='linear')
    f_2 = interp1d(x, y2, kind='linear')

    # Evaluar la función de interpolación en puntos intermedios
    x_interp = np.linspace(0, 28, 29)
    y_interp_1 = f_1(x_interp)
    y_interp_2 = f_2(x_interp)

    # Graficar los puntos originales y el polinomio interpolado
    plt.scatter(x, y1, color='red', marker='*', label='Dias')
    plt.scatter(x, y2, color='red', marker='*', label='Dias')

    plt.plot(x_interp, y_interp_1, color='blue', label='Peso promedio m1')
    plt.plot(x_interp, y_interp_2, color='yellow', label='Peso promedio m2')

    plt.xlabel('Día')
    plt.ylabel('Peso Promedio(mg)')
    plt.title('Interpolación con trazadores lineales')

    # Mostrar la gráfica
    plt.legend()
    plt.show()