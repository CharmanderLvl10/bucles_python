#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: Ejercicio 1 de la Clase Numero 4

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Alejandro Villaboa"
__email__ = "alejandrocesarv@gmail.com"
__version__ = "Clase numero 4"

condicion = False


def ej1():
    # Ejercicios con bucles "while"

    # Dado el siguiente "while", complete la condicion
    # para que el "while" itere siempre que <x sea menor a 6>
    # Además, complete la línea de código necesaria para que
    # el valor de "x" incremente "1" en cada iteración
    # reemplace "condicion" por lo que crea necesario
    # Coloque la línea de código para que "X" incremente "1"

    x = 0
    while x <= 6:
        print('El valor de x ahora es', x)
        print('Sumamos 1 a x')
        x = x + 1
        if x > 6:
            print('El valor de x ahora es mayor que 6')


    # Dado el siguiente "while", complete la condicion
    # para que el "while" itere siempre que <x sea mayor o igual a 0>
    # Además, complete la línea de código necesaria para que
    # el valor de "x" decremente "1" en cada iteración
    # Coloque la línea de código para que "X" decremente "1"
    # reemplace "condicion" por lo que crea necesario

    x = 5
    while x >= 0:
        print('El valor de x ahora es', x)
        print('restamos 1 a x')
        x = x - 1
        if x == 0:
            print('El valor de x ahora es igual a 0')


def ej2():
    # Ejemplos con bucles "for"

    # Dado la siguiente lista de colores, utilizar "for"
    # para imprimir en pantalla todos los colores

    # Itere el "for" utilizando la lista como parámero
    # y utilizar como elemento del "for" cada color
    # for color ...

    # Itere el "for" utilizando el tamaño de la lista
    # como parámetro y utilizar el índice para acceder a
    # los elementos de la lista
    # for i ...

    colores = ['rojo', 'naranja', 'verde', 'azul']

    # for colores ...
    for paleta in colores:
        print('Colore en la agenda:', paleta)

    # for i colores ...
    for i in range(len(colores)):
        print('Colore en la agenda: {}'.format(colores[i]))


def ej3():
    # Ejemplos con bucles "for"

    # Dado la siguiente lista de números, utilizar "for"
    # para recorrer toda la lista y realizar la sumatoria de todos los números
    # La sumatoria se deberá ir guardando en la variable "suma"

    numeros = [1, 5, -1, 6, 10, 2, -5]
    suma = 0

    print('Lista de numeros:\n',numeros)
    print('Sumamos los numero de la lista paso por paso')
    
    for i in range(len(numeros)):
        anterior = suma
        suma += numeros[i]
        print('\nNumero:', anterior)
        print('Suma:', numeros[i])
        print('Resultado:\n', suma)

    print('\nResultado final:\n',suma)


def ej4():
    # Ejercicios con bucles "while"

    # Realizar un bucle "while" cuya condición de continuidad
    # sea que <x sea menor a 10> y que <x sea distinto de 6>
    # Colocar ambas condiciones como condicion del "while" realizando
    # una condición compuesta (utilice el operador "and" o "or" según corresponda)
    # En cada iteracion del bucle debe incrementar el valor de "x" en "2"
    # e imprimir en pantalla el resultado de X (antes de incrementar) con print

    # Realice el mismo bucle "while" pero en vez de estar formado por una condición
    # compuesta, que el "while" siga iterando mientras <x sea menor a 10>, y dentro del
    # "while" consultar si <x es igual a 6>, y en ese caso realizar una interrupción del bucle
    # En cada iteracion del bucle debe incrementar el valor de "x" en "2"
    # e imprimir en pantalla el resultado de X (antes de incrementar) con print

    # Realizar bucle "while" cuya condición sea que <x sea menor a 10> o que <x sea distinto de 6>
    # con resultado anterior
    x = 0

    while x < 10 and x != 6 or x > 10 and x == 6:
        anterior = x
        x += 2
        print("\nx antes de incrementar era:\n", anterior, '\nx despues de incrementar es:\n', x)

    # Realizar bucle "while" cuya condición sea que <x sea menor a 10> o que <x es igual a 6>
    # con resultado anterior y realizar una interrupción del bucle
    x = 0

    while x < 10:
        anterior = x
        x += 2
        print("x antes de incrementar era:\n", anterior, '\nx despues de incrementar es:\n', x)
        if x == 6:
            print(x, 'Es igual a 6')
            break


def ej5():
    # Ejercicio de secuencias numéricas

    # Pedir por consola dos números que representen el principio y fin de una
    # secuencia numérica.
    # Realizar un bucle "for" que recorra esa secuencia armada con "range"
    # y calcule a sumatoria total de todos los números dentro de esa secuencia
    # Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    # sino que va hasta el anterior
    # Imprimir el valor de la sumatoria

    inicio = int(input('Ingrese el primero número de la secuencia\n'))
    fin = int(input('Ingrese el ultimo número de la secuencia\n'))

    # Realizar un bucle "for" que recorra esa secuencia armada con "range"
    print('\nLa secuencia numerica es:\n')  
    for secuencia_n in range(inicio, fin + 1):
        print(secuencia_n)

    # Realizar e imprimir el valor de la sumatoria

    suma_rango = 0
    for i in range(inicio, fin + 1):
        suma_rango += i
    print("\nLa suama del rango de los numeros ingresados es:\n",suma_rango)


def ej6():
    # Ejercicio de secuencias numéricas
    # Pedir por consola dos números que representen el principio y fin de una
    # secuencia numérica.
    # Realizar un bucle "for" que recorra esa secuencia armada con "range"
    # y cuante cuantos números son negativos y cuantos números son mayor o igual a cero
    # Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    # sino que va hasta el anterior
    # Imprimir el valor de la cantidad de números positivos y negativos

    inicio = int(input('Ingrese el primero número de la secuencia\n'))
    fin = int(input('Ingrese el ultimo número de la secuencia\n'))

    secuencia_num = list(range(inicio, fin + 1))

    print('\nEl rango de numeros ingresado es del {} al {}'.format(inicio, fin))
    print('\nLa secuencia numerica es:', secuencia_num)

    cantidad_numeros_positivos = 0 
    cantidad_numeros_negativos = 0

    for i in range(len(secuencia_num)):
        if i >= 0:
            cantidad_numeros_positivos += 1
        else:
            cantidad_numeros_negativos += 1

    print('\nLa cantidad de numeros positivos son:', cantidad_numeros_positivos)
    print('\nLa cantidad de numeros negativos son:', cantidad_numeros_negativos)


if __name__ == '__main__':
    print("\nBienvenidos a otra clase de Inove con Python\n")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
    ej6()
