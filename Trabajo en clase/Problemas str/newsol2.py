def orden(list1,list2):
    lt=list1+list2
    lt.sort(reverse=True)
    print (f"la lista es {lt} y tiene {len(lt)} elementos")
    return lt

def main():
    l1=eval(input("LISTA 1"))
    l2=eval(input("Lista 2"))
    orden(l1,l2)

main()