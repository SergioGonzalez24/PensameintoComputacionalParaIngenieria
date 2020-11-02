""" 
@author: Sergio Gonzalez
Funciones

"""
def perimetro_rec(base,altura):
    '''Calcule el perimetro de un triangulo'''
    perimetro=base*2+altura*2
    print(f"el permietro es {perimetro}")
    return(perimetro)


#llamada de funcion
var_per=perimetro_rec(10,5)
