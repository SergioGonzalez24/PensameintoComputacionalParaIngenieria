'''
Author @Sergio Gonzalez
A01745446

Quizz For
'''
print("")
print("Leer 20 números e imprimir cuantos son positivos, cuantos negativos y cuantos neutros. ")
print("")
neu=0
pos=0
neg=0
for i in range(1,21):
    d=int(input("Ingrese un numero positivo negativo o neutro"))
    if d>0:
        pos+=1
    elif d==0:
        neu+=1
    elif d<0:
        neg+=1
print("el total son: ",f"positivos: {pos}",f"neutrales: {neu}",f"negativos: {neg}",sep="\n")

print("__________________")
print("")
print(" Obtener el promedio de calificaciones de un grupo de n alumnos. ")
print("")

n=int(input("Ingrese total de alumnos "))
califtot=0

for i in range(1,n+1):

    calif=int(input(f"la calificacion del alumno numero {i} es: "))
    califtot+=calif
    
prom=califtot/n
print(f"El promedio es de {prom}")


print("_____________________________")
print("")
print("En la Cámara de Diputados se levanta una encuesta con todos los integrantes con el fin de determinar que porcentaje de los n diputados esta a favor del Tratado de Libre Comercio, que porcentaje esta en contra y que porcentaje se abstiene de opinar. ")
print("")
#Simulacion con 50 diputados pq en la camara son 500
fav=0
cont=0
abst=0
tot=0
for i in range(1,50):
    print("A favor o encontra de la mocion")
    voto=str(input("favor-->fav, encnotra-->cont, abtinencia-->abst "))
    votad=voto.lower()
    if votad=="fav":
        fav+=1
        tot+=1
    elif votad=="cont":
        cont+=1
        tot+=1
    elif votad=="abst":
        abst+=1
        tot+=1
por_fav=(fav*tot)/100
por_cont=(cont*tot)/100
por_abst=(abst*tot)/100
print(f"Total de votantes: {tot}")
print(f"{por_fav}% votos a favor",f"{por_cont}% votos a favor",f"{por_abst}% votos a favor",sep="\n")
print("el total son: ",f"positivos: {pos}",f"neutrales: {neu}",f"negativos: {neg}",sep="\n")
print("______________________")