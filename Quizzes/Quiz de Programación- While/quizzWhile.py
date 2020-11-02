'''
Author @Sergio Gonzalez
A01745446

Quizz de Programacion: While

'''
print("")
print("Realizar un programa que transforme todas las letras del alfabeto de mayúsculas a minúsculas. ")
print("")
abecedario=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
letra_min=abecedario[0]
num=0
while not(letra_min == "z"):

    letra_min=abecedario[num]
    print(letra_min.lower())
    if num<25:
        num+=1
    else:
        break

print("_____________________________")
print("")
print("Determinar cuantos hombres y cuantas mujeres se encuentran en un grupo de n alumnos, suponiendo que los datos son extraídos alumno por alumno.")
print("")
print("El Total de Alumnos Son 26")
nombres=["Juan","Jose","Daviv","Diana","Eloisa","Fernanda","Guadalupe","susana","Iker","Julia","Kimberly","Lizbeth","Marion","Nimbe","Omar","Patricio","Roberta","Roberto","Panfila","Tania","Blanca","Valeria","Wiliam","Xochitl","Diana","Zapata"]
alumn_num=0
hom=0
muj=0
nobi=0
while alumn_num<=25:

    print(f"{nombres[alumn_num]} es hombre o mujer? ")
    print("")
    res=input("si es hombre escriba h si es mujer escriba f si no es nunguno de los dos escriba x ")
    res_min=res.lower()
    

    if res_min=="h":
        hom+=1
        alumn_num+=1
    elif res_min=="f":
        muj+=1
        alumn_num+=1
    elif res_min=="x":
        nobi+=1
        alumn_num+=1
    else:
        print("valor no valido vuelva a intenarlo")
        print("")



print("el total fue:",f"hombres: {hom}",f"mujeres: {muj}",f"no definidos: {nobi}", end="\n")

print("___________________________________________________________")
print("")
print("2.30. Escribir un programa que lea números enteros de teclado hasta que encuentre uno que cumpla las siguientes condiciones:","Múltiplo de 2.","No múltiplo de 5.","Mayor que 100.","Menor que 10.000.",sep="\n")
print("")

num=eval(input("Ingrese numero para saber si es  múltiplo de 2, no múltiplo de 5, mayor que 100 y menor que 10.000."))

while not(num%2==0 and not(num%5==0) and num >100 and num<10000):
    num=eval(input("Ingrese otro numero que si cumpla las condiciones"))
print(f"bien su numero {num} si cumple ")