# -*- coding: utf-8 -*-
arquivo = open("arquivo.txt")
'''
linhas = arquivo.readlines()
print(linhas)
for linha in linhas:
	print(linha)
'''
texto_completo = arquivo.read()
print(texto_completo)
arquivo.close()

w = open("arquivo.txt", "w")
w.write("Esse é o meu arquivo\n")
w.close()

w = open("arquivo.txt", "a")
w.write("Esse é o meu arquivo")
w.close()