#!/usr/bin/env python3
import random
def run():
	a = [i**2 for i in range(12) if i%2 !=0 ]
	i = 0
	while i < random.choice(a):
		print(i)
		i += 1
	print()	
	
run()	
