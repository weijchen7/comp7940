def print_factor(x):
	for i in range(1, x+1):
		if x%i == 0:
			print(i)

x = int(input('Please input an integer: '))	
print_factor(x)
