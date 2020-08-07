a = [1,2,3,4,5]
target = 2

def binary_search_rec(arr, target):
	if len(arr) == 1:
		return False

	mid = len(arr) // 2

	if arr[mid] == target:
		return True, mid
	else:
		if arr[mid] > target:
			return binary_search_rec(arr[:mid], target)
		else:
			return binary_search_rec(arr[mid+1:], target)

if __name__ == '__main__':
	res = binary_search_rec(a, target)
	print(res)