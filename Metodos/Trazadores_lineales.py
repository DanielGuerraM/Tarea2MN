import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


def Metodo_Trazadores_lineales(x, y1, y2):

    # Interpolación por trazadores lineales
    f1 = interp1d(x, y1, kind='linear')
    f2 = interp1d(x, y2, kind='linear')

    # Peso máximo aproximado de la muestra 1
    xnew1 = np.linspace(0, 28, num=100, endpoint=True)
    pesos1 = f1(xnew1)
    peso_max1 = np.max(pesos1)
    dia_peso_max1 = xnew1[np.argmax(pesos1)]
    print("El peso promedio máximo aproximado de la muestra 1 es:", peso_max1, "mg")

    # Peso máximo aproximado de la muestra 2
    xnew2 = np.linspace(0, 28, num=100, endpoint=True)
    pesos2 = f2(xnew2)
    peso_max2 = np.max(pesos2)
    dia_peso_max2 = xnew2[np.argmax(pesos2)]
    print("El peso promedio máximo aproximado de la muestra 2 es:", peso_max2, "mg")


    fig, (plt1, plt2) = plt.subplots(1, 2, figsize=(10, 5))

    plt1.plot(x, y1, '*', label='Muestra 1', color='red')
    plt1.plot(xnew1, f1(xnew1), label='Interpolación 1')
    plt1.legend(loc='best')
    plt1.set_xlabel('Días después del nacimiento')
    plt1.set_ylabel('Peso promedio (mg)')
    plt1.set_title('Muestra 1')

    plt2.plot(x, y2, '*', label='Muestra 2', color='red')
    plt2.plot(xnew2, f2(xnew2), label='Interpolación 2')
    plt2.legend(loc='best')
    plt2.set_xlabel('Días después del nacimiento')
    plt2.set_ylabel('Peso promedio (mg)')
    plt2.set_title('Muestra 2')

    fig.suptitle('Metodo de trazadores lineales')
    plt.show()