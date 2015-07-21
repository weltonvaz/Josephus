#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.system("clear")

import math 

n = int(input("Entre com o numero de pessoas: "))
m = int(input("Entre com o valor do passo --> "))

x = 0
suiciders = []
soldier = set(range(1,n+1))

for i in range(1,n):
	x = m * i
	while x > n:
		x = (m *(x - n)-1)/(m-1)
	suiciders.append(x)
		
print("A sequencia de pessoas a serem mortas é: ",suiciders)

# salvo = soldier.symmetric_difference(suiciders)
# print("Nesta sequência foi salvo o soldado :", list(salvo))
	
