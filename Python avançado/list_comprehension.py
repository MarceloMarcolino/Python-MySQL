# list comprehension

x = [1, 2, 3, 4, 5]
y = []

for i in x:
	y.append(i**2)

print("Sem usar list comprehension")
print(x)
print(y)

y = [i**2 for i in x]

print("Usando list comprehension")
print(x)
print(y)

z = [i for i in x if i%2==1]

print("Usando list comprehension com condição para imprimir números impares")
print(z)