#1
from re import I, M
from unittest import result


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
var_Ciclos = 5
i = 0
for i in range(i,var_Ciclos):
    print(i)

#6
num_Factoriado = 5
limite = num_Factoriado
i = 0
factorizador = num_Factoriado
while( limite > 0  ):
    factorizador-=1
    if factorizador == 1:
        print(num_Factoriado)
        break
    num_Factoriado *= factorizador
    limite -=1

#7

n = 0
while(n < 5 ):
    for i in range(0,n):
        print("El ciclo while esta en ", str(n))
        print("El ciclo for esta en ", str(i))
    n += 1


#8
encontrar = "corridas"
for n in encontrar:
    while(n != "s"):
        print("NO se ha encontrado la letra s")
        break
    if( n == "s" ):
        print("se encontro la letra s en la posicion ", n )

#9


limte = 30
count = 0
primo = True


#13

i = 100
while(i < 301):
    if(i % 12 == 0 ):
        print(i,"es divisble de 12")
    i=i+1
    continue

#15

for i in range(100, 301):
    if(i % 3 == 0 and i % 6 == 0):
        print(i)
        break
    else:
        continue


