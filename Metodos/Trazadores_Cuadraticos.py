import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

def Metodo_Trazadores_Cuadraticos(x, y1, y2):

    # Interpolación por trazadores cuadráticos
    f1 = interp1d(x, y1, kind='quadratic')
    f2 = interp1d(x, y2, kind='quadratic')

    # Valores para la gráfica
    xnew = np.linspace(0, 28, num=1000, endpoint=True)
    y1new = f1(xnew)
    y2new = f2(xnew)

    # Peso máximo de la muestra 1
    max_p1 = np.max(y1new)

    # Peso máximo de la muestra 2
    max_p2 = np.max(y2new)

    print(f'El peso promedio máximo de la muestra 1 es aproximadamente {max_p1:.2f} mg')
    print(f'El peso promedio máximo de la muestra 2 es aproximadamente {max_p2:.2f} mg')

    fig, (plt1, plt2) = plt.subplots(1, 2, figsize=(10, 5))

    # Gráfica de la muestra 1
    plt1.plot(x, y1, '*', label='Muestra 1', color='red')
    plt1.plot(xnew, y1new, label='Interpolación 1')
    # Etiquetas y leyenda
    plt1.set_xlabel('Día')
    plt1.set_ylabel('Peso promedio (mg)')
    plt1.set_title('Muestra 1')


    # Gráfica de la muestra 2
    plt2.plot(x, y2, '*', label='Muestra 2', color='red')
    plt2.plot(xnew, y2new, label='Interpolación 2')
    # Etiquetas y leyenda
    plt2.set_xlabel('Día')
    plt2.set_ylabel('Peso promedio (mg)')
    plt2.set_title('Muestra 2')

    # Mostrar gráfica
    fig.suptitle('Metodo de trazadores cuadraticos')
    plt.show()