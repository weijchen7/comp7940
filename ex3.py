l = [52633, 8137, 1024, 999]

for num in l:
	factor = []
	for i in range(1, num+1):
		if num%i == 0:
			factor.append(i)
	print('The factor of', num, ' are ', factor)
	
