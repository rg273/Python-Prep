#1
from turtle import color


ciudades = ["Nueva York", "PARIS", "Tokio", "Los angeles","Quatar"]
#2
print(ciudades[1])
#3
print("segundo al cuarto:  ", ciudades[1:4])
#4
print(type(ciudades))
#5
print(ciudades[2:])
#6
print("ultima valor, con -1",ciudades[-1:])
#7
ciudades.append("PARIS")
ciudades.append("Rio de janeiro")
print(ciudades)
#8
ciudades.insert(3,"Mexico city")
print(ciudades)
#9
listafrases =["lista de ",1,"frases ","incesarias"]
listaconcatenadas = ciudades + listafrases
print(listaconcatenadas)
#10
i = 0
while(i < len(ciudades)):
    if ciudades[i] =="PARIS":
        print(i)
    i=i+1
#10
print(ciudades.index("PARIS"))
#11 arroja error
 
#12 
print(ciudades.pop(6))
print(ciudades)

#13 salee error

#14
carajo = ciudades.pop()
print(carajo)

#15
lista_multiplicada = ciudades * 4
print(lista_multiplicada)

#16
tuplita = tuple((range(1,21)))
print(tuplita)

#17
u = 10
while(u < 15):
    print(tuplita[u])
    u = u + 1

#18 prueba
cui = [1,2,"rojo",3,4,5,6]
tuplaprueba = (1,2,"rojo",3,4,5,6)

print(1 in tuplaprueba) 

#18
j = 20
while(j < 31):
    if (j in tuplita):
        print(j ,"se ecuentra en tuplita")
    else:
        print(j,"NO SE ENCUETRA EN TUPLITA")
    j = j + 1

#19
elemento_a_buscar = "Paris"
if (not(elemento_a_buscar in ciudades)):
    ciudades.append("Paris")
    print(ciudades, "agrgamos Paris")
else:
    print("paris ya se encuentra en ciudades")

#20
print(ciudades.count("Paris"))
print(tuplaprueba.count("rojo"))

#21
tuplaprueba = list(tuplaprueba)
print(tuplaprueba)
ciudades = tuple(ciudades)
print(ciudades)

#22
a,b,c, _, _, _ , _ = ciudades

print(c)

#23
ciudades = list(ciudades)
print(ciudades)

mi_primer_diccionario_21_4 = {
    "CIUDAD":ciudades,
    "PAISES":["RUSIA", "ARGENTINA", "SIRIA", "RUMANIA", "ARMENIA"],
    "CONTINENTE": ["alla","aca","porArriba","ojalanadieleaesto"]

}
for keys in mi_primer_diccionario_21_4.keys():
    print(keys, "keys sin sus valores")
print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
for values in mi_primer_diccionario_21_4.values():
    print(values, "son las lugares que elegi")
print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
for var_items, var_valore in mi_primer_diccionario_21_4.items():
    print("keys", var_items, "Y", var_valore,"estos los valores")