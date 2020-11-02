textoin=('''Hola me llamo juan
tengo 20 años
soy de jalisco''')

sep=("\n")

textosep=textoin.split(sep)
newlist=list(textosep)
for i in range (len(newlist)):
    a=newlist[i]
