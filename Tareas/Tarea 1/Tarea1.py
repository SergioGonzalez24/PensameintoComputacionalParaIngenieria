###Sergio Manuel Gonzalez Vargas 
###A01745446
###Tarea 1

#Ejercicio 1
#Escribe un algoritmo para verificar si un precio dado por el usuario es válido o no lo es, para ser válido debe ser un valor positivo.

print("Ejercicio 1")

precio = float(input("Ingrese precio"))

if precio > 0:
    print("Valido")

else:
    print("Invalido")


print("____________________________________________________________")

#Ejercico 2
#Escribe un algoritmo que muestre la velocidad promedio de un automóvil dadas la distancia recorrida en kilómetros y el tiempo que se tardó en recorrer esa distancia dado en horas.

print("Ejercicio 2")

distancia_km = float(input("Introducir distancia recorrida en KM"))
tiempo_hrs= float(input("Introducir el tiempo que tardo en recorrer la distancia total en hras "))

vel = distancia_km/tiempo_hrs

print(vel, "km/hrs")


print("____________________________________________________________")

#Ejercico 3
#Escribe un algoritmo que dada una longitud en metros, calcule y muestre su equivalente en pies.

print("Ejercicio 3")

longitud = float(input("Escribe la longitud en metros"))

#1m = 3.28pies

longitud = (longitud*3.28)
print(longitud,"ft")

print("____________________________________________________________")

#Ejercico 4
#Escribe un algoritmo que verifique si una persona puede obtener su licencia de conducir. Para hacerlo debe ser mayor de edad (18 años o más) y traer una identificación oficial. 

print("Ejercico 4")

edad = int(input("Intruduce tu edad"))

if edad >= 18 :
    doc_official = input("¿Tiene identificacion oficial? (escribir si o no)")
    
    if doc_official == "si" :
        print("Entregar licencia")
    else:
        print("no cumple con los requisitos")
else:
    print("no tiene 18 años aun ")