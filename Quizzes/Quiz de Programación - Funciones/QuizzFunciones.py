'''
Author @Sergio Gonzalez
A01745446

Quizz de programacion: Funciones

'''
#Ejercicio 1 
print("")
print("Crea una función raizCubica, que calcule la raíz cúbica de un real, y devuelva otro real (pista: puedes elevar a 1/3 para hallarla).")
def raizCubica (num):
    numcub=num**(1/3)
    print(numcub)
    
    return numcub

a=eval(input("Ingrese numero para obtener la raiz cubica "))
raizCubica(a)

print("_________________________________________________________________________________________________________")

#Ejercicio 2
print("")
print("Crear una función llamada letraRepetida, que reciba como parámetros una letra y un número, y escriba en pantalla esa letra repetida en pantalla varias veces (tantas como indique el número), sin devolver ningún valor.")
def letraRapida (letr,num):
    
    for i in range(num):
        print(letr)

a=input("ingrese letra a repetir")
b=int(input("Ingrese numero de veces"))

letraRapida(a,b)