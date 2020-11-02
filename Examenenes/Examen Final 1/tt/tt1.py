def divisibles3 (lista):
    copylist=[]
    len(lista)
    for pos in range (len(lista)):
        if pos%2==0:
            copylist.append(lista[pos])
    for element in copylist:
        if not(element%3==0):
            q=copylist.index(element)
            copylist.pop(q)

    if len(copylist)>0:
        print(lista)
        print(copylist)
            
list1=[3,-2,2,5,6,12,15,2,4]
divisibles3(list1)
