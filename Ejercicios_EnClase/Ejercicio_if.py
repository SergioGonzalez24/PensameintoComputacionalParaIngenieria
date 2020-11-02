print("Detector de triangulos")

while True:
    a=int(input("Introduce el lado a: "))
    b=int(input("Introduce el lado a: "))
    c=int(input("Introduce el lado a: "))

    if a>0 and b>0 and c>0:
        if a==b and b==c and c==a:
            print("Es equilatero")
        elif (a==b or b==c or c==a):
            print("Isoc1eles")
        elif not(a==b and b==c and c==a):
            print("escaleno")
    elif not(a+b>c and b+c>a and c+a>b):
        print("no es un triangulo")
    else:
        print("ingrese datos validos")
