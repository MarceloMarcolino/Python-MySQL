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

# Exercício 3
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
delta = pow(b, 2) - (4*a*c)
try:
	raiz_delta = sqrt(delta)
except ValueError:
	raise ValueError("Delta negativo, então não admite solução real.") from None
if raiz_delta >= 0:
	x1 = (-b + raiz_delta)/(2*a)
	x2 = (-b - raiz_delta)/(2*a)
	if x1 == x2:
		print("A raiz é", x1)
	else:
		print("As raízes são", x1, "e", x2)

# Exercício 4
numerica = [500,2,3,9,23,70,3,2,1]

#select sort

for i in range(len(numerica)):

	menor = i

	for j in range(i+1,len(numerica)):

		if numerica[j] < numerica[menor]:
			menor = j

	if numerica[i] != numerica[menor]:
		aux = numerica[i]
		numerica[i] = numerica[menor]
		numerica[menor] = aux

print(numerica)


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