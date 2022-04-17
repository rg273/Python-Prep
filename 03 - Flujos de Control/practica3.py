#1
from re import M


number_menor_cero = -4

if(number_menor_cero > 0):
    print(number_menor_cero)
else:
  print("el numero es negativo")    
  
#2
var1 = 2
var2 = "string"

if(type(var1) == type(var2)):
    print("SON DEL MISMO TIPO DE DATO")

#3
for n in range(1,21):
    if(n % 2 == 0):
        print(n)   
    
#4
for n in range(0,6):
    print("valor:",n, "-Elevado a la potencia es", n**3)

#5
