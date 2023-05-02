import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

def Metodo_Trazadores_Cubicos(x, y1, y2):
    # Interpolación cúbica
    f1 = interp1d(x, y1, kind='cubic')
    f2 = interp1d(x, y2, kind='cubic')

    # Generar puntos de la interpolación
    dias_interp = np.linspace(x[0], x[-1], num=1000)

    # Calcular valores de la interpolación
    muestra1_interp = f1(dias_interp)
    muestra2_interp = f2(dias_interp)

    # Encontrar el peso máximo de cada muestra
    peso_max_muestra1 = np.max(muestra1_interp)
    peso_max_muestra2 = np.max(muestra2_interp)


    fig, (plt1, plt2) = plt.subplots(1, 2, figsize=(10, 5))
    # Graficar los puntos y la interpolación

    plt1.plot(x, y1, '*', label='Muestra 1', color='red')
    plt1.plot(dias_interp, muestra1_interp, label='Interpolación 1')
    plt1.set_title('Peso promedio de larvas en hojas de roble')
    plt1.set_xlabel('Días después del nacimiento')
    plt1.set_ylabel('Peso promedio (mg)')

    plt2.plot(x, y2, '*', label='Muestra 2', color='red')
    plt2.plot(dias_interp, muestra2_interp, label='Interpolación 2')
    plt2.set_title('Peso promedio de larvas en hojas de roble')
    plt2.set_xlabel('Días después del nacimiento')
    plt2.set_ylabel('Peso promedio (mg)')


    # Mostrar el gráfico
    fig.suptitle('Metodo de trazadores cubicos')
    plt.show()

    # Imprimir los pesos máximos
    print("Peso máximo de la muestra 1:", peso_max_muestra1.round(2), "mg")
    print("Peso máximo de la muestra 2:", peso_max_muestra2.round(2), "mg")