##Tarea 2 Metodos numericos
'''
    Integrantes:
    Daniel Mateo Guerra Montoya
    Esteban Arenas Gomez

    Docente: Julian Mauricio Granados Morales

    Ejercicio a resolver: 7mo punto taller s6_Taller_interpolacion

    Se sospecha que las concentraciones altas de “Tanina” en las Hojas Maduras de Roble inhiben el 
    crecimiento de larvas de la polilla de invierno que tanto dañan a estos árboles en algunos años. En la 
    tabla se incluye el peso promedio de dos muestras de larvas en los primeros 28 días después del 
    nacimiento. La primera muestra se crió en hojas de roble joven y la segunda en hojas maduras del 
    mismo árbol. 
    
        a) Por medio una interpolación aproxime la curva de peso promedio de cada muestra. 
        b) Obtenga un peso promedio máximo aproximado de cada muestra, determinando para ello el 
        máximo de la interpolación 

        Día 0 6 10 13 17 20 28 
        Peso Promedio de la muestra 1 (mg) 6.67 17.33 42.67 37.33 30.10 29.31 28.74
        Peso Promedio de la muestra 2 (mg) 6.67 16.11 18.89 15.00 10.56 9.44 8.8
'''

#Importamos las respectivas librerias
import numpy as np
import Metodos.Lagrange as lg
import Metodos.Base_radial as br
import Metodos.Trazadores_lineales as tl

print('Tarea #2, Elija con que metodo desea resolver el ejercicio\n')
print('1. P1olinomio de Lagrange\n2. Funciones de base radial\n3. Trazadores lineales\n4. Trazadores cuadráticos\n5. Trazadores cúbicos\n\n')
idMetodo = int(input('Digite el metodo a ejecutar: '))
x = np.array([0, 6, 10, 13, 17, 20, 28])
y1 = np.array([6.67, 17.33, 42.67, 37.33, 30.10, 29.31, 28.74])
y2 = np.array([6.67, 16.11, 18.89, 15.00, 10.56, 9.44, 8.89])


def ejecuta_lagrenge():
    lg.Metodo_Lagrange(x, y1, y2)

def ejecuta_Base_Radial():
    br.Metodo_Base_Radial(x, y1, y2)

def ejecuta_Trazadores_lineales():
    tl.Metodo_Trazadores_lineales(x, y1, y2)

# def ejecuta_ver_Todas():
#     lg.Metodo_Lagrange(x, y1, y2)
#     br.Metodo_Base_Radial(x, y1, y2)
#     tl.Metodo_Trazadores_lineales(x, y1, y2)

diccionario_Metodos = {
    1:  ejecuta_lagrenge,
    2:  ejecuta_Base_Radial,
    3:  ejecuta_Trazadores_lineales
    # 4:
    # 5:
    # 6: ejecuta_ver_Todas
}

def ejecutar_metodo(argumento):
    if argumento in diccionario_Metodos:
        Metodo = diccionario_Metodos[argumento]
        Metodo()
    else:
        print('Argumento no valido')

ejecutar_metodo(idMetodo)






