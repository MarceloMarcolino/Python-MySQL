# -*- coding: utf-8 -*-
from math import sqrt

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