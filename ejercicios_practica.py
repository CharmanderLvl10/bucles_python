#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: Ejercicio 2 de la Clase Numero 4

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Alejandro Villaboa"
__email__ = "alejandrocesarv@gmail.com"
__version__ = "Clase numero 4"



def ej1():
    print('Comenzamos a ponernos serios!\n')

    '''
    Realice un programa que pida por consola dos números que representen
    el principio y fin de una secuencia numérica.
    Realizar un bucle "for" que recorra esa secuencia armada con "range"
    y cuente cuantos números ingresados hay, y la sumatoria de todos los números
    Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    sino que va hasta el anterior
    '''
    # inicio = ....
    inicio = int(input('Ingrese el primero número de la secuencia\n'))
    # fin = ....
    fin = int(input('Ingrese el ultimo número de la secuencia\n'))

    numero = 0
    cantidad_num = 0
    suma = 0

    # bucle.....
    for numero in range(inicio, fin + 1):
    # cantidad_numeros =....
        cantidad_num += 1
    # sumatoria =....
        suma += numero
       # promedio = sumatoria / cantidad_numeros
        promedio = suma / cantidad_num

    # Imprimir resultado en pantalla
    print('\nLa cantidad de numeros del rango ingresado es:\n', cantidad_num)
    print('\nLa suma de los numeros del rango ingresado es:\n', suma)
    print('\nEl promedio de numeros del rango ingresado es:\n', promedio)


def ej2():
    print("Mi Calculadora (^_^)\n")

    '''
    Tome el ejercicio de clase:
    <condicionales_python /  ejercicios_practica / ej3>,
    copielo a este ejercicio y modifíquelo, ahora se deberá ejecutar
    indefinidamente hasta que como operador se ingrese la palabra "FIN",
    en ese momento debe terminar el programa

    Se debe debe imprimir un cartel de error si el operador ingresado no es
    alguno de lo soportados o no es la palabra "FIN"
    '''
    while True:

        numero_1 = float(input('Ingrese su primer numero:\n'))
        print('\nIngrese su operacion:\n')
        print('Suma (+)')
        print('Resta (-)')
        print('Multiplicación (*)')
        print('División (/)')
        print('Exponente/Potencia (**)')
        calculo_1 = str(input())
        numero_2 = float(input('\nIngrese su segundo numero:\n'))


        if calculo_1 == '+':
            resultado_1 = numero_1 + numero_2
            print('\nLa suma de {} y {} es:\n{}\n'.format(numero_1, numero_2, resultado_1))

        elif calculo_1 == '-':
            resultado_2 = numero_1 - numero_2
            print('\nLa resta de {} y {} es:\n{}\n'.format(numero_1, numero_2, resultado_2))

        elif calculo_1 == '*':
            resultado_3 = numero_1 * numero_2
            print('\nLa multiplicacion de {} y {} es:\n{}\n'.format(numero_1, numero_2, resultado_3))

        elif calculo_1 == '/':
            resultado_4 = numero_1 / numero_2
            print('\nLa division de {} y {} es:\n{}\n'.format(numero_1, numero_2, resultado_4))

        elif calculo_1 == '**':
            resultado_5 = numero_1 ** numero_2
            print('\nEl exponente de {} y {} es:\n {}\n'.format(numero_1, numero_2, resultado_5))

        else:
            print('****ERROR: Caracteres ingresados no valido****\nIntentelos nuevamente\n')
            continue

        print('Para finalizar ingrese FIN\n')
        print('Para continuar ingrese CONTINUAR\n')
        respuesta = str(input())

        if respuesta == 'FIN':
            print('\nMuchas gracias\n')
            break
        elif respuesta  == 'fin':
            print('\nMuchas gracias\n')
            break
        elif respuesta == 'CONTINUAR':
            print('\nContinuemos\n')
            continue
        elif respuesta == 'continuar':
            print('\nnContinuemos\n')
            continue
        else:
            print('****ERROR: Caracteres ingresados no valido****\nIntentelos nuevamente\n')
            continue


def ej3():
    print("Mi organizador académico (#_#)")

    '''
    Tome el ejercicio de "calificaciones":
    <condicionales_python / ejercicios_clase / ej3>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Las notas del estudinte se encuentran almacenadas en una
    lista llamada "notas" que ya hemos definido al comienzo del archivo

    Debe caluclar el promedio de todas las notas y luego transformar
    la califiación en una letra según la escala establecida en el ejercicio
    "calificaciones" <condicionales_python / ejercicios_clase / ej3>

    A medida que recorre las notas, no debe considerar como válidas aquellas
    que son negativas, en ese caso el alumno estuvo ausente

    Debe contar la cantidad de notas válidas y la cantidad de ausentes
    '''

    # Variable global utilizada para el ejercicio de nota
    notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]

    # Para calcular el promedio primero debe obtener la suma
    # de todas las notas, que irá almacenando en esta variable
    sumatoria = 0

    cantidad_notas = 0
    cantidad_ausentes = 0
    cantidad_presentes = 0

    # Realice aquí el bucle para recorrer todas las notas
    # y cacular la sumatoria

    # Terminado el bucle calcule el promedio como
    # promedio = sumatoria / cantidad_notas

    # Utilice la nota promedio calculada y transformela
    # a calificación con letras, imprima en pantalla el resultado

    # Imprima en pantalla al cantidad de ausentes

    # Recorrer las notas con la sumatoria
    for i in range(len(notas)):
        print('\nEl recorrido de la nota es:\n', notas[i])
        anterior = sumatoria
        sumatoria += notas[i]
        print('\nNumero:', anterior)
        print('Suma:', notas[i])
        print('Resultado:\n', sumatoria)

    print('\nEl resultado final es:\n',sumatoria)

    for i in range(len(notas)):
        if notas[i] >= 0:
            cantidad_presentes += notas[i]
            cantidad_notas += 1
        else:
            cantidad_ausentes += 1

    # Imprima en pantalla al cantidad de notas
    cantidad_notas = len(notas) - cantidad_ausentes
    print('\nla cantidad de notas son:\n',cantidad_notas)

    # Imprima en pantalla al cantidad de ausentes
    print('\nla cantidad de notas por asencia son:\n',cantidad_ausentes)

    # Imprima en pantalla el promedio
    promedio = cantidad_presentes / cantidad_notas
    print('\nEl promedio es:\n', promedio)

    # Utilice la nota promedio calculada y transformela a calificación con letras
    if promedio >= 100:
        print('\nSu calificacion fue:  "A+"')
    elif promedio >= 90:
        print('\nSu calificacion fue:  "A"')
    elif promedio >= 80:
        print('\nSu calificacion fue:  "B"')
    elif promedio >= 70:            
        print('\nSu calificacion fue:  "C"')
    elif promedio >= 60:
        print('\nSu calificacion fue:  "D"')
    else:
        print('\nSu calificacion fue:  "F"')


def ej4():
    print("Mi primer pasito en Data Analytics:\n")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica /ej5>,
    copielo a este ejercicio y modifíquelo para cumplir el
    siguiente requerimiento
    En este ejercicio se lo provee de una lista de temperaturas,
    esa lista de temperaturas corresponde a los valores de temperaturas
    tomados durante una temporada del año en Buenos Aires.
    Usted deberá analizar dicha lista para deducir
    en que temporada del año se realizó el muestreo de temperatura.
    La variable con la lista de temperaturas se llama "temp_dataloger"
    definida al comienzo del archivo
    Debe recorrer la lista "temp_dataloger" y obtener los siguientes
    resultados
    1 - Obtener la máxima temperatura
    2 - Obtener la mínima temperatura
    3 - Obtener el promedio de las temperaturas
    Los resultados se deberán almacenar en las siguientes variables
    que ya hemos preparado para usted.
    
    NOTA: No se debe ordenar la lista de temperaturas, se debe obtener
    el máximo y el mínimo utilizando los mismos métodos vistos
    durante la clase (ejemplos_clase)
    '''

    # Variable global utilizada para el ejercicio de temperaturas
    temp_dataloger = [12.8, 18.6, 14.5, 20.8, 12.1, 21.2, 13.5, 18.6, 14.7, 19.6, 11.2, 18.4]
                  
    temperatura_max = None
    temperatura_min = None
    temperatura_sumatoria = 0
    temperatura_promedio = 0
    temperatura_len = 0

    # Colocar el bucle aqui......
    for i in range(len(temp_dataloger)):
        if (temperatura_max is None) or (temp_dataloger[i] > temperatura_max):
            temperatura_max = temp_dataloger[i]
        if (temperatura_min is None) or (temp_dataloger[i] < temperatura_min):
            temperatura_min = temp_dataloger[i]
        temperatura_sumatoria += temp_dataloger[i]
        temperatura_len += 1

    # Al finalizar el bucle compare si el valor que usted calculó para
    # temperatura_max y temperatura_min coincide con el que podría calcular
    # usando la función "max" y la función "min" de python
    # función "max" --> https://www.w3schools.com/python/ref_func_max.asp
    # función "min" --> https://www.w3schools.com/python/ref_func_min.asp

    # 1 - Obtener la máxima temperatura
    print('La temperatura máxima es:',  temperatura_max)
    # 2 - Obtener la mínima temperatura
    print('La temperatura mínima es:',  temperatura_min)
    # función "max"
    print('La temperatura máxima con la funciones "max" es:',  max(temp_dataloger))
    # función "min"
    print('La temperatura máxima con la funciones "min" es:',  min(temp_dataloger))

    # Al finalizar el bucle debe calcular el promedio como:
    # temperatura_promedio = temperatura_sumatoria / cantidad_temperatuas

    # Corrobore los resultados de temperatura_sumatoria
    # usando la función "sum"
    # función "sum" --> https://www.w3schools.com/python/ref_func_sum.asp

    # 3 - Obtener el promedio de las temperaturas
    temperatura_len = len(temp_dataloger)

    temperatura_promedio = temperatura_sumatoria / temperatura_len
    print('\nLa temperatura promedio es:',  temperatura_promedio)
    
    # Corrobore los resultados de temperatura_sumatoria
    print('\nLa sumatoria de las temperatura es:',  temperatura_sumatoria)
    # función "sum"
    temperatura_sumatoria
    print('\nLa sumatoria de las temperatura con la función "sum" es:',  sum(temp_dataloger)

   
    # Una vez que tengamos nuestros valores correctamente calculados debemos
    # determinar en que epoca del año nos encontramos en Buenos Aires utilizando
    # la estadística de años anteriores. Basados en el siguiente link realizamos
    # las siguientes aproximaciones:

    # verano -->      min = 19, max = 28
    # otoño -->       min = 11, max = 24
    # invierno -->    min = 8, max = 14
    # primavera -->   min = 10, max = 24
    
    # Referencia: https://es.weatherspark.com/y/28981/Clima-promedio-en-Buenos-Aires-Argentina-durante-todo-el-a%C3%B1o

    # En base a los rangos de temperatura de cada estación,
    # ¿En qué época del año nos encontramos?
    # Imprima el resultado en pantalla
    # Debe utilizar temperatura_max y temperatura_min para definirlo
   
    if temperatura_min > 19 and temperatura_max < 28:
        print('\nBuenos Aires se encuentra en la epoca de:  Verano')
    elif (temperatura_min > 11) or (temperatura_max < 24):
        print('\nBuenos Aires se encuentra en la epoca de:  Otoño')
    elif (temperatura_min > 8) or (temperatura_max < 14):
        print('\nBuenos Aires se encuentra en la epoca de:  Invierno')
    elif (temperatura_min > 10) or (temperatura_max < 24):
        print('\nBuenos Aires se encuentra en la epoca de:  Primavera')


def ej5():
    print("Ahora sí! buena suerte :)")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica / ej4>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento
    Realize un programa que corra indefinidamente en un bucle, al comienzo de la
    iteración del bucle el programa consultará al usuario con el siguiente menú:
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)
    3 - Salir del programa
    En caso de presionar "3" el programa debe terminar e informar por
    pantalla de que ha acabado,
    en caso contrario si se presionar "1" o "2" debe continuar con la siguiente tarea
    NOTA: Si se ingresa otro valor que no sea 1, 2 o 3 se debe enviar
    un mensaje de error y volver a comenzar el bucle
    (vea en el apunte "Bucles - Sentencias" para encontrar
    la sentencia que lo ayude a cumplir esa tarea)
    Si el bucle continua (se presionó "1" o "2") se debe ingresar a otro bucle
    en donde en cada iteración se pedirá una palabra. La cantidad de iteración
    (cantidad de palabras a solicitar) lo dejamos a gusto del alumno, intente que esa
    condición esté dada por una variable (ej: palabras_deseadas = 4)
    Cada palabra ingresada se debe ir almacenando en una lista de palabras, dicha
    lista la debe inicializar vacia y agregar cada nuevo valor con el método "append".
    Luego de tener las palabras deseadas almacenadas en una lista de palabras
    se debe proceder a realizar las siguientes tareas:
    Si se ingresa "1" por consola se debe obtener la palabra
    más grande por orden alfabético
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra
    más grande alfabeticamente.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?
    Si se ingresa "2" por consola se debe obtener la palabra
    con mayor cantidad de letras
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra con
    mayor cantidad de letras.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?
    
    NOTA: No se debe ordenar la lista de palabras, se debe obtener
    el máximo utilizando el mismos métodos vistos durante la clase
    (ejemplos_clase), tal como el ejercicio anterior. Ordenar una
    lista representa un problema mucho más complejo que solo
    buscar el máximo.
    NOTA: Es recomendable que se organice con lápiz y papel para
    hacer un bosquejo del sistema ya que deberá utilizar 3 bucles en total,
    1 - El bucle principal que hace que el programa corra hasta ingresar un "3"
    2 - Un bucle interno que corre hasta socilitar todas las palabras deseadas
        que se deben ir guardando en una lista
    3- Otro bucle interno que corre luego de que termine el bucle "2" que
       recorre la lista de palabras y busca la mayor según el motivo ingresado ("1" o "2")
    '''

    # Inicialización de las Variables:

    palabras = [] # Lista Vacía
    max_palabra = None
    max_cant_letras = None

    flag = False  # Variable que Uso como Bandera

    while flag == False:

        print('Bienvenido/a:')
        print('¿Qué desea Realizar?\n')
        print('1 - Ordenar Palabras por Orden Alfabético (usando el operador ">")')
        print('2 - Ordenar Palabras por Cantidad de letras (longitud de la palabra)')
        print('3 - Salir del programa')
        opcion = int(input('\nIngrese a Continuación la Opción que Desee: '))

        if ((opcion == 1) or (opcion == 2)):

            cant_palabras_deseadas = int(input('\nIngrese el Nro. de Palabras que Desee Escribir: '))
            print('\n')

            while cant_palabras_deseadas > 0:
                palabra = str(input('Ingrese la Palabra que Desee: '))
                palabras.append(palabra)
                cant_palabras_deseadas -= 1

            if opcion == 1:
                for i in range(len(palabras)):
                    if ((max_palabra is None) or (max_palabra <= palabras[i])):
                        max_palabra = palabras[i]
                
                print('\n\nLas Palabras Ingresadas son: {}'.format(palabras))
                print('\nLa Mayor Palabra Más Grande Alfabéticamente es: "{}"\n\n'.format(max_palabra))


            if opcion == 2:
                for i in range(len(palabras)):
                    if ((max_cant_letras is None) or (len(max_cant_letras) <= len(str(palabras[i])))):
                        max_cant_letras = palabras[i]

                print('\n\nLas Palabras Ingresadas son: {}'.format(palabras))
                print('\nLa Palabra que Tiene Mayor Cantidad de Letras es: "{}"\n\n'.format(max_cant_letras))


        elif opcion == 3:
            flag = True
            print('\nEl Programa ha Finalizado.\n\n')


        else:
            print('\n¡¡¡¡ERROR!!!! Se ha Ingresado una Opción Inválida.\n\n')
            continue

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    ej4()
    ej5()