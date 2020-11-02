#uberx=7.00
#uberxl= 12.26
#uberblack=16.52
#ubersuv=22.72
km=0
while not (km==-2):
    km_Usr=eval(input())
    tipoUber=int(input())
    if tipoUber==1:
        tarifD=input()
        tarifDlow=tarifD.lower()
        if tarifDlow=="a":
            continue
        elif tarifDlow=="b":
            res=(7.00*km_Usr)
        else:
            print("error")

    elif tipoUber==2:
        tarifD=input()
        tarifDlow=tarifD.lower()
        if tarifDlow=="a":
            continue
        elif tarifDlow=="b":
            res=(12.26*km_Usr)
        else:
            print("error")

    elif tipoUber==3:
        tarifD=input()
        tarifDlow=tarifD.lower()
        if tarifDlow=="a":
            continue
        elif tarifDlow=="b":
            res=(16.52*km_Usr)
        else:
            print("error")

    elif tipoUber==4:
        tarifD=input()
        tarifDlow=tarifD.lower()
        if tarifDlow=="a":
            continue
        elif tarifDlow=="b":
            res=(22.72*km_Usr)
        else:
            print("error")
            
    else:
        print("error")

    
    print(res)