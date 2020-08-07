def fibonacci_rec(x):
	if x == 0:
		return 0
	elif x == 1:
		return 1
	else:
		return fibonacci_rec(x-1) + fibonacci_rec(x-2)

def fibonnaci_forloop(x):
	if x == 0:
		return 0
	elif x == 1:
		return 1
	
	temp = [0, 1]

	for i in range(2, x+1):
		temp.append(temp[i-1] + temp[i-2])
	return temp[x]

if __name__ == '__main__':
	res = fibonacci_rec(5)
	print(res)
	res = fibonnaci_forloop(5)
	print(res)

