# -*- coding: utf-8 -*-
from math import sqrt

# Exercício 1
idade = int(input("Digite sua idade: "))
if idade >= 18:
	print("Você é maior de idade.")
elif idade < 18 and idade > 0:
	print("Você é menor de idade.")
else:
	print("Insira uma idade maior que 0.")