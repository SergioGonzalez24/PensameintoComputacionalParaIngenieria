def contra (pa):
    if pa.lower()!= 'hola':
        return 1
    else:
        return 0

def main():
    r=1
    c=1

    while r and  c<=3:
        pa=input()
        r=contra(pa)
        if r==0:
            print("Acceso permitido")
            break
        else:
            print("Acceso denegado")
        c+=1
    
main()
 