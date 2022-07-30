# -*- coding: utf-8 -*-
'''
>CABEÇALHO_DA_SEQUENCIA
MCADCDACDAAKKKLPQWYTYTYTYTYYTQQQVVVAAAAAL
CDACDAAKKKLPQWYTYTYTCDACDAAKKKLPQWYTYTYT
'''

import re

# Exercício 3
seq = input("Digite uma sequência: ")

arquivo = open("seq2.fasta", "w")
arquivo.write(">seq\n")
arquivo.write(seq)
arquivo.close()