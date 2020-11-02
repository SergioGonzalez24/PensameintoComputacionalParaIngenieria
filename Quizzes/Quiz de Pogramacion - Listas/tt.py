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
            
        l2=l1[::1]
        if sum(l1)>0:
            print(l1[-1],l1[0],l2,sep="\n")
        else:
            print(l1[0],l1[-1],l2,sep="\n")

        cond=False