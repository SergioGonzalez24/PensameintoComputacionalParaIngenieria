def fc_cf(t):
    lis=t.split()
    if lis[1].lower()=="f":
        print(f"Correcto")
        return 5/9*(float(lis[0])-32)
    elif lis[1].lower()=="c":
        print(f"Correcto")
        return float(lis[0])*9/5+32
    else:
        print("Incorrecto")
        return 0
def main():
    T=input()
    print(f"{fc_cf(T):.3f}")
    
main()