print("Calculadora basica")
opcion=input("¿Que operacion quieres? (+,-,/,*):")
a=eval(input("Introduce el primer numero "))
b=eval(input("Introduce el segundo numero "))
if opcion=="+":
    print(f"{a}+{b}={a+b}")
elif opcion=="-":
    print(f"{a}-{b}={a-b}")
elif opcion=="-":
    print(f"{a}/{b}={a/b}")
elif opcion=="-":
    print(f"{a}*{b}={a*b}")        
else:
    print("Opcion no valida")
