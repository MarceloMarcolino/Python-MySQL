entrada = open("16s_bacteria.fasta").read()
saida = open("bacteria.html","w")

cont = {}

'''
AA
AT
AC
AG
TA
TT
TC
TG
CA
CT
CC
CG
GA
GT
GC
GG
'''

for i in ['A','T','C','G']:
	for j in ['A','T','C','G']:
		cont[i+j] = 0

print(cont)

for k in range(len(entrada)):
	cont[entrada[k]+entrada[k+1]] += 1