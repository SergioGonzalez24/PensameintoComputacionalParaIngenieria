a=int(input("Ingresa 1 valor"))
b=int(input("Ingresa otro numero mayor "))

while a<=b:
    if a==0:
        print(a)
    elif  a%2==0:
        print(a)
    a+=1

print("_____________________")

a=10 

if a>5:
    print(1)
elif a>=10:
    print(2)
else:
    print(3)