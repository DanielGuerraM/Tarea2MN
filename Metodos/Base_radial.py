import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics.pairwise as sk
from sklearn.linear_model import LinearRegression

def Metodo_Base_Radial(x, y1, y2):
    # Crea una matriz de características X y un vector objetivo y
    # X = np.array([0, 6, 10, 13, 17, 20, 28])
    # y = np.array([6.67, 17.33, 42.67, 37.33, 30.10, 29.31, 28.74])

    # Se calcula la matriz de distancias usando la función de base radial
    gamma = 0.1
    K = sk.rbf_kernel(x.reshape(-1, 1), gamma=gamma)

    # Ajusta un modelo de regresión lineal usando la matriz de distancias como características
    model_1 = LinearRegression().fit(K, y1)
    model_2 = LinearRegression().fit(K, y2)


    # se Predice el valor de 'y1' para una nueva observación x
    x_new = np.array([7])
    k_new = sk.rbf_kernel(x.reshape(-1, 1), x_new.reshape(1, -1), gamma=gamma)


    plt.scatter(x, y1, color='red', marker='*', label='Dias')
    plt.plot(x, model_1.predict(K), color='blue', label='Peso promedio m1')

    plt.scatter(x, y2, color='red', marker='*', label='Dias')
    plt.plot(x, model_2.predict(K), color='yellow', label='Peso promedio m2')

    plt.xlabel('Día')
    plt.ylabel('Peso Promedio(mg)')
    plt.title('Interpolación en Base Radial')

    plt.legend()
    plt.show()