# -*- coding: utf-8 -*-
'''
>CABEÇALHO_DA_SEQUENCIA
MCADCDACDAAKKKLPQWYTYTYTYTYYTQQQVVVAAAAAL
CDACDAAKKKLPQWYTYTYTCDACDAAKKKLPQWYTYTYT
'''

import re

# Exercício 1

seq1 = input("Digite a sequência 1: ")
seq2 = input("Digite a sequência 2: ")

if seq1 == seq2:
	print("As duas sequências são iguais.")
else:
	print("As duas sequências são diferentes.")

busca = re.match(seq1,seq2)

if busca:
	print("Sequências idênticas.")
	print(busca.group())
else:
	print("Sequências diferentes.")

seq1 = "AT.GA.*"
seq2 = "ATTGAAAAAAAA"

if seq1 == seq2:
	print("As duas sequências são iguais.")
else:
	print("As duas sequências são diferentes.")

busca = re.match(seq1,seq2)

if busca:
	print("Sequências idênticas.")
	print(busca.group())
else:
	print("Sequências diferentes.")