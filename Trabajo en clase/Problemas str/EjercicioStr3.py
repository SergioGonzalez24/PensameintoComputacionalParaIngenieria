def sum (list1,list2,same):
    pos=0
    newlist=[]
    if same==True:
        for len in list1:
            join=list1[pos]+list2[pos]
            newlist.append(join)
            pos+=1
    else:
        return 0
    print(newlist)

def main():
    l1=eval(input("lista 1 "))
    l2=eval(input("lista 2 "))
    sum(l1,l2,(len(l1)==len(l2)))

main()

