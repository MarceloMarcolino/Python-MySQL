# -*- coding: utf-8 -*-
x = 2
y = 3

soma = x + y

print(x == y and x == soma)

x = 3
z = 3

print(x == y and x == z)

z = 4

print(x == y and x == z)
print(x == y or x == z)
print(x == y or x == z and z == y)