def fibonacci(n):
	""" Conventional Fibonacci """
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_without_rec(n):
	""" Fibonacci without Recursion """
	a, b = 0, 1

	for i in range(n):
		a, b = b, a+b
	return a

def fibonacci_last_digit(n):
	""" Fibonacci with only last digit """
	if n == 0:
		return 0
	if n == 1:
		return 1
	return (fibonacci(n - 1) + fibonacci(n - 2)) % 10

def max_subset(arr):
	""" this takes the subset which has the maximum total value in a given list """
	prev = current = 0

	for i in arr:
		prev, current = current, max(prev + i, current)
	return current

if __name__ == "__main__":
	n = 10
	# === Fibonacci Sequence Part ===
	print(fibonacci(n))
	print(fibonacci_without_rec(n))
	print(fibonacci_last_digit(n))

	# === Maximum Subarray Part ===
	a = [1, 5, 3, 2]
	b = [1, 5, 3, 2, 7]
	c = [1, 5, 3, 2, 7, 2]

	res = max_subset(arr=a)
	print(res)
	res = max_subset(arr=b)
	print(res)
	res = max_subset(arr=c)
	print(res)