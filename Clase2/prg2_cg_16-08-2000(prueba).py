# def Sumar(a,b=8):
#     return (a+b)
#
# print (Sumar(10))
# print (Sumar(10,5))
#----------------------------------------------------------
def Sumar(a,b,c=8):
    res= (a+b) *c
    return res, c

v1,v2=Sumar(10,5)
print (v1,v2)
