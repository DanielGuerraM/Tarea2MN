import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

def Metodo_Lagrange(x, y1, y2):
   
    # Se realiza la interpolacion por el polinomio de Lagrange
    poly1 = lagrange(x, y1)
    poly2 = lagrange(x, y2)

    # Evaluamos el polinomio previamente calculado en un rango de valores
    x_new = np.linspace(0, 28, 100)
    y_new1 = poly1(x_new)
    y_new2 = poly2(x_new)

    # Hallamos el máximo de la interpolación
    max1 = y_new1.max()
    max2 = y_new2.max()

    #Se inicializa nuestro plano donde estaran las 2 graficas
    fig, (plt1, plt2) = plt.subplots(1, 2, figsize=(10, 5))

    #Se grafica la primera muestra
    plt1.plot(x, y1, '*', label='Muestra 1', color='red')
    plt1.plot(x_new, y_new1, label='Interpolación')
    plt1.set_xlabel('Días')
    plt1.set_ylabel('Peso promedio (mg)')
    plt1.legend()
    plt1.set_title('Muestra 1')

    #Se grafica la segunda muestra
    plt2.plot(x, y2, '*', label='Muestra 2', color='red')
    plt2.plot(x_new, y_new2, label='Interpolación')
    plt2.set_xlabel('Días')
    plt2.set_ylabel('Peso promedio (mg)')
    plt2.legend()
    plt2.set_title('Muestra 2')

    fig.suptitle('Metodo de Lagrange')
    plt.show()

    print(f'El peso promedio máximo de la muestra 1 es aproximadamente {max1:.2f} mg')
    print(f'El peso promedio máximo de la muestra 2 es aproximadamente {max2:.2f} mg')