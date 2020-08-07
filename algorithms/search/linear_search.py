a = [1,2,3,4]
target = 2

def linear_search(arr, target):
	cnt = 0
	for i in arr	:
		if i == target:
			return cnt
		else:
			cnt += 1

if __name__ == '__main__':
	res = linear_search(a, target)
	print(res)