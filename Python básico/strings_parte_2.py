# -*- coding: utf-8 -*-
a = "Diego"
b = "Mariano"

concatenar = a + " " + b
print(concatenar)
print(concatenar.lower())
print(concatenar.upper())
print(concatenar)

concatenar = concatenar.upper()
print(concatenar)

concatenar = a + " " + b + "\n"
print(concatenar)
print(concatenar.strip())

concatenar = a + " " + b + " "
print(concatenar)
print(concatenar.strip())

minha_string = "O rato roeu a roupa do rei de Roma"

minha_lista = minha_string.split(" ")
print(minha_lista)

minha_lista = minha_string.split()
print(minha_lista)

minha_lista = minha_string.split("r")
print(minha_lista) # case sensitive

busca = minha_string.find("rei")
print(busca)
print(minha_string[busca:])

busca = minha_string.find("rainha")
print(busca)

minha_string = minha_string.replace("o rei", "a rainha")
print(minha_string)