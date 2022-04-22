#1
from tkinter import E
from typing import Iterable


lista_vacia = []
i = -15
while(i < 0):
    lista_vacia.append(i)
    i = i + 1

print(lista_vacia)

#2
print (i)
while(i < len(lista_vacia)):
    if( lista_vacia[i] % 2 == 0):
        print(lista_vacia[i])
    i+=1
print("ejecicio 2")

#3
i = 0
for i in range(len(lista_vacia)):
    if(lista_vacia[i] % 2 == 0):
        print(lista_vacia[i])

#4 y #5
for l, s in enumerate(lista_vacia):
    print(l ,"tiene de valor" ,s)
    if l == 2:
        break

# no es el 5
cadena = "holanda"
numero_tupla = 3,2,1
numerogrande = 128312312312

print("cadena", isinstance (cadena, Iterable))
print("numero_tupla", isinstance (numero_tupla, Iterable))
print("numerogrande", isinstance (numerogrande, Iterable))

#6

lista = [1,2,5,7,8,10,13,14,15,17,20]
i = 1

while( i < 20):
    if(lista[i - 1] != i):
        print(lista,"no")
        print(i)
        lista.insert(i - 1,i)
        print(lista)
    i = i + 1

#7
fibonacci = [0,1]
n = 2
while(n < 30):
    fibonacci.append(fibonacci[n - 1] + fibonacci[ n - 2])
    n = n + 1

print(fibonacci)

#8
suma = 0
for i in fibonacci:
    suma+= i
print(suma)

#10
contador_n = 0
cadena_de_n ="Hola mundo. Esto es una practica del lenguaje de programacion Python"
for buscando in cadena_de_n:
    if(buscando == "n"):
        contador_n +=1

print(contador_n)

#11
dicc = {
    "juegospreferido1": "gtav",
    "scondjuego":"smite",
    "tercer juego":"kill zone shadow fall"
}
for elemete in enumerate(dicc):
    print(elemete)

#12

lista_cadena_de_n = list(cadena_de_n)
print(lista_cadena_de_n) 
cantidade_de_caracteres = 0
for itera in lista_cadena_de_n:
    
    cantidade_de_caracteres += 1
print(cantidade_de_caracteres)

#14
lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

numero_divisibles = []
z = 0
while(z < len(lis)):
    if lis[z] % 7 == 0:
        numero_divisibles.append(lis[z])
    z +=1
print (numero_divisibles)

for a in lis:       
    print(a)

#15

lis_2 = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
contador_elementos = 0
for iteradore in lis_2:
    print(iteradore)
    if type(iteradore) == list:
        print(iteradore)
        contador_elementos += len(iteradore)
    else: contador_elementos +=1
print(contador_elementos)

#16
print("#16")

for itera, elemetno in enumerate(lis_2):
    print(itera,elemetno,"---------------")
    if type(elemetno) != list:
        lis_2[itera] = [elemetno]
print(lis_2)
