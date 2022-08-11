# Função enumerate

lista = ["abacate", "bola", "cachorro"]

for i in range(len(lista)):
	print(i, lista[i])

#usando função enumerate
for i, nome in enumerate(lista):
	print(i, nome)