ne=int(input())
totS=0
for i in range(1,ne+1):
    vendido=int(input())
    if vendido>=100 and vendido<300:
        tot=(vendido*200000)*0.97
        totS+=tot
    elif vendido>=300 and vendido<500:
        tot=(vendido*200000)*0.96
        totS+=tot 
    elif vendido>=500 and vendido<700:
        tot=(vendido*200000)*0.95
        totS+=tot
    elif vendido>=700 and vendido<=1000:
        tot=(vendido*200000)*0.94
        totS+=tot
    else:
        continue

print(totS)