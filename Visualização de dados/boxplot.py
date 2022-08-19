# Boxplot - diagrama de caixa
import matplotlib.pyplot as plt
import random

#vetor = [1,2,4,6,12,512,12,2]
vetor = []

for i in range(10):
	numero_aleatorio = random.randint(0,5)
	vetor.append(numero_aleatorio)

plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()