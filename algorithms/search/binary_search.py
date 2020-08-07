a = [1,2,3,4,5]
target = 2

def binary_search(arr, target):
	first = 0
	last = len(arr) - 1
	found = False

	while (first <= last and not found):
		mid = (first + last) // 2
		if arr[mid] == target:
			found = True
		else:
			if arr[mid] > target:
				last = mid - 1
			else:
				first = mid + 1
	return found, mid

if __name__ == '__main__':
	res = binary_search(a, target)
	print(res)