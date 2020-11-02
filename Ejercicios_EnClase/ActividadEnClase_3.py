#Se requiere una solucíon para poder convertir de cent´ımetros (cm) a pulgadas (in).
print("Ejercicio 1")

convertido=(float(input("Introducir un numero en centimetros para convertirlos a pulgadas")))

#1cm = 1""

convertido= convertido/2.54
print(convertido,"inch", sep=" ")

#Calculo del area de un rectangulo a partir del conocimiento del valor de los lados en metros
print("Ejercicio 2")

largo=eval(input("Introduce el largo de tu rectangulo en metros"))
ancho=eval(input("Introduce el ancho de tu rectangulo en mentros"))

area=largo*ancho

print(area)

#Calculo del area y circunferencia de un cırculo a partir del conocimiento del radio en centımetros

print("Ejercicio 3")

rad=eval(input("Introduce el radio en cm"))
pi=3.1415

area=pi*(rad**2)
perimetro=2*pi*rad

print(area,"cm^2","\n",perimetro,"cm",end=" ")
