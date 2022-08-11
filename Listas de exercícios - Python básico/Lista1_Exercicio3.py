# -*- coding: utf-8 -*-
from math import sqrt

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