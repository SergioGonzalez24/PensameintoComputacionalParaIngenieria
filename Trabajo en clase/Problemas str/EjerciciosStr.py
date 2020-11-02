def condicion(nums):
    pares=0
    pos=0
    impar=[]
    for len in nums:
        if (nums[pos]%2==0):
            pares+=nums[pos]
            pos+=1
        elif not(nums[pos]%2==0):
            impar.append(nums[pos])
            pos+=1
    print(f"la suma total de los pares es {pares}","\n",f"los impares son {impar}")



def main():
    lista=[]
    n=int(input(""))
    for i in range (n):
        nums=int(input(""))
        lista.append(nums)
    condicion(lista)

main()

