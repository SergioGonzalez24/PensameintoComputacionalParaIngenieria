###Sergio Manuel Gonzalez Vargas
#A01745446

#Tarea 1

print("")
print("Estructuras de Seleccion")
print("")
print("Ejercicio 1")

print("Realizar un programa que solicite dos números enteros los ordene en forma ascendente y los imprima.")
print("")
print("Pseudocodigo","1-.Ingresar ambos numeros","2-.Comparar que numero es mas grande","3-.Regresar los numeros ordenados",sep="\n")

a=int(input("Ingrese un numero "))
b=int(input("Ingrese otro numero "))

if a>b:
    print(b,a,sep=",",end="")
else:
    print(a,b,sep=",",end="")
print("")

print("_______________________________________________________")
print("")
print("Ejercicio 2")
print("")
print("Determinar si un alumno aprueba a reprueba un curso, sabiendo que aprobara si su promedio de tres \n calificaciones es mayor o igual a 70; reprueba en caso contrario.")
print("")
print("Pseudocodigo","1-.Ingresar las tres calificaciones","2-.Sumar y sacar promedio","3-.Hacer la comparacion entre el promedio y la calificacion para aprobar","4-.Regresar el resultado obtenido",sep="\n")


calif1=eval(input("Ingresar primera calificacion"))
calif2=eval(input("Ingresar segunda calificacion"))
calif3=eval(input("Ingresar tercera calificacion"))

prom=(calif1+calif2+calif3)/3

if prom<70:
    print("Reprobado con: ",prom)
else:
    print("Aprobado con: ",prom)

print("_______________________________________________________")
print("")
print("Ejercicio 3")
print("")
print("Solicitar al usuario una fecha (dd:mm:aaaa) y comprobar si es correcta. Para que una fecha sea correcta es necesario:")
print("El año debe ser mayor que cero.")
print("El mes debe estar entre 1 y 12.")
print("Dependiendo del mes que sea, el día debe estar dentro de los límites válidos. Los meses que tienen 31 días son 1, 3, 5, 7, 8, 10 y 12. \nLos meses de 30 días son 4, 6, 9 y 11. \nEl mes de 28 días es 2, excepto en un año bisiesto que es 29 días.")
print("")
print("Pseudocodigo","1-.Ingresar las fecha","2-.Verificar que la fecha sea valida","3-.Revisar si la fecha es un año biciesto o no","4-.Revisar los datos obtenidos que cumplan con las especificaciones","5-.Regresar si es una fecha valida, biciesta o no es fecha",sep="\n")

dia=int(input("Introduce el dia "))
mes=int(input("Introduce el mes "))
año=int(input("Introduce el año "))


def fecha ():
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12 and dia>= 31:
        print(f"La fecha es: {dia}/{mes}/{año}")
    elif mes==4 or mes==6 or mes==9 or mes==7 or mes==11 and dia>= 30:
        print(f"La fecha es: {dia}/{mes}/{año}")
    elif mes==2 and dia>=28:
        print(f"La fecha es: {dia}/{mes}/{año}")
    else:
        print("fecha no valida")

def fecha_B ():
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12 and dia>= 31:
        print(f"La fecha es: {dia}/{mes}/{año}")
    elif mes==4 or mes==6 or mes==9 or mes==7 or mes==11 and dia>= 30:
        print(f"La fecha es: {dia}/{mes}/{año}")
    elif mes==2 and dia>=29:
        print(f"La fecha es: {dia}/{mes}/{año}")
    else:
        print("fecha no valida")
    


if mes>0 and mes<=12 and dia>0 and año>0:

    if año%4==0 and not(año%100==0):
        print("año biciesto")
        fecha_B()

    elif año%4==0 and (año%100==0) and (año%400==0):
        print("Año biciesto")
        fecha_B()

    elif año%4==0 and (año%100==0) and not(año%400==0):
        fecha()
    else:
        fecha()
else:
    print("Fecha no valida")