# -*- coding: utf-8 -*-
from math import sqrt

# Exercício 5
num1 = int(input("Digite o primeiro número: "))
sinal = input("Digite um sinal: ")
num2 = int(input("Digite o segundo número: "))

# soma +
if sinal == "+":
	operacao = num1 + num2
	print("O resultado da soma é",operacao)
# subtração -
elif sinal == "-":
	operacao = num1 - num2
	print("O resultado da subtração é",operacao)
# divisão /
elif sinal == "/":
	operacao = num1 / num2
	print("O resultado da divisão é",operacao)
# multiplicação *
elif sinal == "*" or sinal == "X" or sinal == "x":
	operacao = num1 * num2
	print("O resultado da multiplicação é",operacao)
# modulo %
elif sinal == "%":
	operacao = num1 % num2
	print("O resultado do módulo é",operacao)
# modulo %
elif sinal == "**":
	operacao = num1 ** num2
	print("O resultado da exponenciação é",operacao)
else:
	print("Insira um sinal válido. Eles são '+,-,/,* ou X,%,**'.")