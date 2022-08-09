# -*- coding: utf-8 -*-
'''
>CABEÇALHO_DA_SEQUENCIA
MCADCDACDAAKKKLPQWYTYTYTYTYYTQQQVVVAAAAAL
CDACDAAKKKLPQWYTYTYTCDACDAAKKKLPQWYTYTYT
'''

import re

# Exercício 5

arquivo = open("seq_dicionario.fasta")
linhas = arquivo.readlines()
multifasta = {}

for linha in linhas:
	if linha[0] == ">":
		seq_atual = linha[1:].strip()
		multifasta[seq_atual] = ""
	else:
		multifasta[seq_atual] = multifasta[seq_atual] + linha.strip()

print(multifasta)
print(multifasta["seq2"])
arquivo.close()