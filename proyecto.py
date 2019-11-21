#*******************************
#Proyecto Matematica Discreta
#PARTICION DE NUMEROS
#Majo Castro #181202
#Andrea Paniagua #18
#Juan Diego Solorzano #18
#*******************************

#imports de librerias correspondientes
import sys
#import range
#Inicio del programa
#variables
numero=0
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
        numero = 5
        particiones = [1] + [0] *numero
        for i in range(1,numero+1):
            for j in range(i, numero+1):
                particiones[j] +=particiones[j-i]
            #print(particiones)
                print(particiones[numero])
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
        
    
