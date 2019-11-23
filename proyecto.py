#*******************************
#Proyecto Matematica Discreta
#PARTICION DE NUMEROS
#Majo Castro #181202
#Andrea Paniagua #18
#Juan Diego Solorzano #18
#*******************************



#Definicion de Funciones
def particionesDe(n):
    a=[0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]

        
def Calcular(n,k):
	particiones = particionesDe(int(n))
	for i in particiones:
		if int(k) == 0:
			print(i)
		elif len(i) == int(k):
			print(i)


                
#imports de librerias correspondientes
import sys
#import range
#Inicio del programa
#variables
numero = 0
k=0
opcion= 0
#menu
while opcion !=3:
    print("************************************")
    print("      PARTICION DE NUMEROS         ")
    print("1. Mostrar pariciones")
    print("2. Mostrar autores")
    print("3. Salir")
    print("************************************")
    opcion = input("Ingrese la opcion ")
    while not opcion.isdigit():
        opcion = input("Ingrese su opcion")
    opcion = int(opcion)
    #Particion de numeros
    if opcion ==1:
        print ("Usted ha elegido mostrar las parcticiones")
        numero = input("Ingrese el numero para partir ")
        k = input("Ingrese longitud de particiones ")
        Calcular(numero,k)
        print("********************************************")
    #Mostrar dosos los integrantes
    elif opcion == 2:
        print("GRUPO:")
        print("Majo Castro #181202")
        print("Andrea Paniagua #18 ")
        print("Juan Diego Solorzano #18 ")
    #opcion para salir del programa 
    elif opcion == 6:
        print("Adios")
        
    
