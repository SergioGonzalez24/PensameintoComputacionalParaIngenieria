###Sergio Gonzalez
##A01745446

#Tarea 5
print("")
print("Ejercicio 1\n")
print("Se requiere repetir una palabra en n cantidad de veces. Genere un programa que pida la palabra y el nu ́mero de veces a repetirla.")

def palabra (texto,num):
    repetir=texto*num
    return repetir

def main():
    p=input("Ingrese palabra")
    n=int(input("Ingrese el numero"))
    r=palabra(p,n)
    print(r)

main()

print("______________________")
print("")
print("Ejercicio 2\n")
print("Se quiere saber si un caracter esta ́ dentro de una frase. Genere un programa que reciba la frase y que devuelva True si el caracter est ́a dentro de la frase y False en caso contrario.")

palabra=input("ingrese alguna frase")
caracter=input("ingrese el caracter a buscar")

if caracter in palabra:
    print(True)
else:
    print(False)

print("______________________")
print("")
print("Ejercicio 3\n")
print("Se requiere un programa que de la bienvenida a los empleados de la empresa FANCY ENTERPRI- SE. As ́ı que hay que pedir el nombre del empleado y mostrarle el mensaje: “Hola [Nombre], bienvenido a FANCY ENTERPRISE.")

n=input("Ingrese su Nombre")
print(f"Hola{n}, bienvenido a FANCY ENTERPRISE")

print("______________________")
print("")
print("Ejercicio 4\n")
print("Para entrar a una empresa se requiere tener un ćodigo de empleado, donde los codigos de acceso de los empleados estan previamente cargados en algun tipo de base de datos. Genere una funci ́on en Python que tenga cargados 3 c ́odigos de 3 d́ıgitos en una lista y que reciba un codigo, si el codigo no esta en la lista debera imprimir un mensaje de error y regresar True, en caso que el c ́odigo si est ́e en la lista devolver ́a False y mostrar ́a un mensaje de bienvenida.")

def contraseña (acceso):
    lista=["123","XYZ","1A2"]
    condicion=acceso in lista
    print(condicion)
    return condicion

def main ():
    a=input("Ingrese contraseña")
    contraseña(a)

main()

print("______________________")
print("")
print("Ejercicio 5\n")
print("Trending topic (tt) para 2 tweets. Escriba un programa que reciba dos tweets y que encuentre todos sus hashtags y despliegue una string con los hashtags que se encuentren en ambos tweets, mostrando tambi ́en cu ́antos son.")

t=input('Introduzca tweet: ') 
t2=input('Introduzca otro tweet: ') 
lt1=t.split(' ')
lt2=t2.split(' ')
hashtags=[[a] for a in lt1 if "#" in a] 
hashtags.extend([a] for a in lt2 if "#" in a) 
print(hashtags)
print(f'Existen {len(hashtags)} hashtags ')