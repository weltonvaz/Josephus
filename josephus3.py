#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.system("clear")

def josephus(n, k):
	r = 0
	for i in range(1, n+1):
		r = (r+k)%i
	return 'Survivor: %d' %r
 
print(josephus(5, 2))
