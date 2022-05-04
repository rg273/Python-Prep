#1
from math import factorial
from re import U
import re


# numerorecibed = int(input("Elige un numero:  "))
# def esprimo(parametor):
#     esprimo = 0
#     for i in range(2,parametor):
#         if(parametor % i == 0):
#             esprimo +=1
#     if(esprimo == 0):
#         return True
#     elif(esprimo >= 1):
#          return False

# print(esprimo(numerorecibed))

#2

# lis = [12,3,4,5,6,7,8,9,20,21,22,23,24,25,26,27,28,229,230,231,232,233]

# def haciendo_call_back(lista):
#     a = 0
#     milista_primos = []
#     while(a < len(lista)):
#         if(esprimo(lista[a]) == True ):
#             milista_primos.append(lista[a])
#         a = a + 1
#     return milista_primos

# print(haciendo_call_back(lis))

#3
"""lista_de_repetidos = [2,2,2,3,4,5,6,76,76,7,7,8,9,0,8,6,5,4,3,2,1,2,4,5,6,7,8,6,4,3,2,24,5,6,7,9,6]
concepto = [2,4,2,4,2,2,4]
lamaspesada = 0
cuantas_veces_lo_hizo = 0
concepto.sort() 
o = 1
count = 1
while (o < len(concepto)):  #recoremos todo el list
    if concepto[o] == concepto[o - 1]:  #verificamos que el siguiente sea igual para sumar mas 1
        count = count + 1
    if (count > cuantas_veces_lo_hizo):     # guardamos y verificamos si hay otro mayor 
        cuantas_veces_lo_hizo = count
        lamaspesada = concepto[o]
    o+=1
print("El numero que mas se repite es el",lamaspesada,"y se repite", cuantas_veces_lo_hizo )
"""
#5

# def convertir_grados (valor, medidadeorigen,medida_de_destino):
    
#     if  medidadeorigen == "C" and medida_de_destino == "K":
#         valor = valor + 273.15
#         return ("serian "+ str(valor)+"° kelvin" )
#     if  medidadeorigen == "C" and medida_de_destino == "F":
#         valor = (valor * 9/5) + 32
#         return ("serian "+ str(valor)+"° Farenheint" )
#     if  medidadeorigen == "K" and medida_de_destino == "C":
#         valor = valor - 273.15
#         return ("serian "+ str(valor)+"° Celcius" )
#     if  medidadeorigen == "K" and medida_de_destino == "F":
#         valor = valor - 273.15
#         valor = (valor * 9/5) + 32
#         return ("serian "+ str(valor)+"° Farenheint" )
#     if  medidadeorigen == "F" and medida_de_destino == "C":
#         valor = (valor - 32)  
    

# grados= int(input("cuantos grados quieres convertir:   "))
# medida_origen = input("Elige una medida C, K o F :  ")
# medida_final = input("elige la medida final que quieres C, K o F:   ")

# print(convertir_grados(grados,medida_origen,medida_final))

         

def fatorial (numero):

    if numero < 0 or type(numero) != int:
        return print("Elige un numero sin coma y psotivo")
    if numero == 1:
        return 1
    return numero * fatorial(numero - 1)

print(fatorial(-12))


def esNegativo_O_positivo (number):
    if number < 0:
        print("es negativo")
    elif number == 0:
        print("es neutro")
    else: 
        print("es positivo")

esNegativo_O_positivo(-10)