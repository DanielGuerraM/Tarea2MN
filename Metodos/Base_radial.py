import numpy as np
from scipy.interpolate import Rbf
import matplotlib.pyplot as plt

def Metodo_Base_Radial(x, y1, y2):


    # Crear la función de base radial
    rbf = Rbf(x, y1, function='multiquadric', epsilon=1.5)

    # Definir los valores para la interpolación
    dias_interp = np.linspace(0, 28, 100)

    # Interpolar los valores para obtener la curva aproximada
    peso1_interp = rbf(dias_interp)

    # Repetir los pasos 3 al 5 para la segunda muestra
    rbf = Rbf(x, y2, function='multiquadric', epsilon=1.5)
    peso2_interp = rbf(dias_interp)

    # Encontrar el peso máximo de cada muestra
    peso1_max = np.max(peso1_interp)
    peso2_max = np.max(peso2_interp)

    print(f'El peso promedio máximo de la muestra 1 es aproximadamente {peso1_max:.2f} mg')
    print(f'El peso promedio máximo de la muestra 2 es aproximadamente {peso2_max:.2f} mg')

    #Se instancia el plano donde iran las dos graficas
    fig, (plt1, plt2) = plt.subplots(1, 2, figsize=(10, 5))

    plt1.plot(x, y1, '*',label='Muestra 1', color='red')
    plt1.plot(dias_interp, peso1_interp, label='Muestra 2')
    plt1.set_xlabel('Días')
    plt1.set_ylabel('Peso Promedio (mg)')
    plt1.set_title('Muestra 1')

    plt2.plot(x, y2, '*',label='Muestra 1', color='red')
    plt2.plot(dias_interp, peso2_interp, label='Muestra 2')
    plt2.set_xlabel('Días')
    plt2.set_ylabel('Peso Promedio (mg)')
    plt2.set_title('Muestra 2')

    fig.suptitle('Metodo de funciones en base radial')
    plt.show()