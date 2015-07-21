#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.system("clear")

def j(n, k):
	p, i, seq = list(range(1,n+1)), 0, []
	while p:
		i = (i+k-1) % len(p)
		seq.append(p.pop(i))
	return 'Ordem dos Soldados mortos: %s.\nSobriventes: %i' % (', '.join(str(i) for i in seq[:-1]), seq[-1])

n = int(input("Entre com o numero de pessoas: "))
k = int(input("Entre com o valor do passo --> "))

print(j(n,k))
