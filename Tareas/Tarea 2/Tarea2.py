"""
@Sergio Gonzalez
A01745446

Tarea 2

"""
###Muestre a un vendedor cu ́anto ganar ́a por la venta de 3 art ́ıculos 
# si la comisi ́on que recibe es del 10 % del total de ventas.
# Debes de pedir al usuario que introduzca los precios de los 
# 3 art ́ıculos.

print("Ejercicio 1")
print("pseudocodigo","1-.Leer los precios","2-.sumar los precios y sacrle el 10% al total","3-.Regresar el 10% del total", sep="\n")

precio1=eval(input("Ingrese el precio de su primer producto "))
precio2=eval(input("Ingrese el precio de su segundo producto "))
precio3=eval(input("ingrese el precio de su tercer producto"))

ganancia=(precio1+precio2+precio3)*0.1

print(ganancia)

print("_____________________________________________________")

###Una yarda(yd) equivale a 0.9144 metros(m). Se requiere hacer la 
# conversi ́on de una distancia en yardas a metros
print("Ejercico 2")
print("pseudocodigo","1-.Leer las yardas a convertir","2-.Hacer la conversion","3-.Regresar las yardas transformadas en metros", sep="\n")

yarda=eval(input("Ingrese las yardas que desea convertir a metros "))

#1yd = 0.9144m
convertido=yarda*0.9144
print(convertido,"m")

print("_____________________________________________________")

###El ındice de masa corporal (IMC) se calcula con la formula: 
# IMC= masa/estatura^2 Teniendo esto en consideracion, hay que 
# implementar una solucion que pida la masa (en kg) y la estatura 
# (en m) para mostrar el IMC.
print("Ejercico 3")
print("pseudocodigo","1-.Leer la masa en kg y la estatura en m","2-.Hacer la operacion para obtener imc","3-.Regresar el imc", sep="\n")

mass=eval(input("Ingrese la masa en kg: "))
tamaño=eval(input("Ingrese la estatura en m: "))

imc = mass/(tamaño**2)
print (imc)

print("_____________________________________________________")

###Consulte en internet la equivalencia entre una milla y un kilometro, 
# hacer un programa en Python que solicite una distancia en millas y la 
# convierta a kilometros.
print("Ejercicio 3")
print("pseudocodigo","1-.Leer millas a convertir","2-.Hacer la conversion a km","3-.Regresar la distancia en km", sep="\n")

dist_m=eval(input("Introduzca la distancia en millas: "))
dist_k= dist_m*1.609
print(dist_k,"km")

print("_____________________________________________________")
