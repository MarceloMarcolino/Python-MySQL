# -*- coding: utf-8 -*-
minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista_2 = [1,2,3,4,5]
minha_lista_3 = ["abacaxi", 2, 9.89, True]
minha_lista_4 = []

for item in minha_lista:
	print(item)

tamanho = len(minha_lista)
print(tamanho)

minha_lista.append("limao")
print(minha_lista)

if 3 in minha_lista_2:
	print("3 esta na lista")

del minha_lista[2:]
print(minha_lista)

minha_lista_4.append(57)
print(minha_lista_4)