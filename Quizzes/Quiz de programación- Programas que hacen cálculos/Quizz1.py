###Sergio Gonzalez
#A01745446

#Quiz de programación: Programas que hacen cálculos

print("Quizz 1")
print("")

a="hola"

#Ejercicio 1.2
print("Ejercicio 1.2","\n","")
print("Plantea el algoritmo y desarrolla el código para resolver los siguientes problemas.","\n")

#Instrucciones
print("Convierte una cantidad dada por el usuario en pesos a dolares.",)

#Algoritmo
print("Algoritmo: ","1-.Introduce la cantidad a convertir","2-.Hacer la conversion","3-.Regresar el input convertido","",sep="\n",end="")

#Codigo
dineroPesos=eval(input("Introduce la cantidad a convertir a dolares "))

#Dolar = 22.06MXN
conv=(dineroPesos/22.06)

print("Son ",conv,"dlls")

print("______________________________________________________","\n","")

#Ejercicio 2.1
from math import *
print("Ejercicio 2.1","\n","")
print("Ahora algo más matemático","\n")

#Instrucciones
print("Desarrolla un programa que calcule el volumen de una esfera.","\n")

rad=eval(input("Introduce el radio de tu esfera en m "))

vol=(((1/3)*4)*pi)*(rad**3)
 
print("El volumen es ",vol,"m^3")

print("_________________________________________________________")

#Ejercicio 3.1
print("Ejercicio 3.1","\n","")
print("Ahora algo más matemático","\n")

#Instrucciones
print("Escribe un programa que reciba dos números y despliegue en pantalla la suma, la resta y la multiplicación de los mismos.","\n")

num=eval(input("Introduce un numero "))
num2=eval(input("Introduce tu segundo numero "))

num_s=num+num2
num_r=num-num2
num_m=num*num2

print("La suma es: ",num_s,"\n","la restaes: ",num_r,"\n","la multipliocacion es: ",num_m)
