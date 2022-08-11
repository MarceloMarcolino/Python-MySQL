# -*- coding: utf-8 -*-
from math import sqrt

# Exercício 2
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
if nota1 < 0.0 or nota2 < 0.0:
	print("Insira nota(s) maior(es) ou igual(is) à 0.")
elif nota1 > 10.0 or nota2 > 10.0:
	print("Insira nota(s) menor(es) ou igual(is) à 10.")
else:
	media = (nota1 + nota2)/2
	if media >= 6.0:
		print("O usuário está aprovado")
	elif media < 6.0:
		print("O usuário está reprovado")