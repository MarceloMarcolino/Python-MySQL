# -*- coding: utf-8 -*-
'''
>CABEÇALHO_DA_SEQUENCIA
MCADCDACDAAKKKLPQWYTYTYTYTYYTQQQVVVAAAAAL
CDACDAAKKKLPQWYTYTYTCDACDAAKKKLPQWYTYTYT
'''

import re

# Exercício 2
nome = input("Digite o nome do arquivo que você deseja abrir: ")
arquivo = open(nome)
linhas = arquivo.readlines()
print(linhas)
for linha in linhas:
	print(linha)
'''
texto_completo = arquivo.read()
print(texto_completo)
'''
arquivo.close()
