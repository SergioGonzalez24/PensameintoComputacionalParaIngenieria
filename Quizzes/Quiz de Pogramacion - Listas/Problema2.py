
cond=True
while cond ==True:
    l1=[]
    pos=-1

    n1=int(input(""))
    
    if n1<=0:
        print("")

    else:
        for i in range (n1):
            num1=int(input(""))
            l1.append(num1)
        for len in l1:
            print(f"lista[{pos}]","=",l1[pos],sep=" ")
            pos-=1

        listaOrd=sorted(l1)
        print(listaOrd[-1],listaOrd[0],listaOrd,sep="\n")
