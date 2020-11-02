def orden(list1,list2):
    lt=list1+list2
    lt.sort(reverse=True)
    print (f"la lista es {lt} y tiene {len(lt)} elementos")
    return lt

def main():
    l1=[]
    l2=[]
    n1=int(input("elementos en lista 1 "))
    for i in range (n1):
        num1=int(input(""))
        l1.append(num1)

    n2=int(input("elementos en lista 2 "))
    for i in range (n2):
        num2=int(input(""))
        l2.append(num2)

    orden(l1,l2)

main()