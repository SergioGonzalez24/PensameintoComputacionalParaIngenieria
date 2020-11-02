'''
Diseña y codifica un programa en Python en el cual el usuario ingrese la cantidad de elementos que va a ingresar a la lista,
posteriormente el programa debe leer cada uno de los elementos de la lista, uno por línea y se van agregando a la lista. 
Importante: El programa debe validar que el número de elementos a ingresar sea mayor que cero, sino debe volver a pedir el 
valor hasta que cumpla.
'''


cond=True
while cond ==True:
    l1=[]
    pos=0

    n1=int(input("elementos en lista 1 "))
    
    if n1<=0:
        print("numero no valido")

    else:
        for i in range (n1):
            num1=int(input(""))
            l1.append(num1)
        for len in l1:
            print(f"lista[{pos}]","=",l1[pos],sep=" ")
            pos+=1

        print(l1[-1],sum(l1),sum(l1)/pos,sep="\n")
        cond=False5