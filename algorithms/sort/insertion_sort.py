a = [1,5,10]
target = 3

def insertion_sort(arr, target):
	arr.append(target)

	for i in range(len(arr)-1, 0, -1):
		if arr[i-1] <= arr[i]:
			return arr
		else:
			_temp = arr[i-1]
			arr[i-1] = arr[i]
			arr[i] = _temp

if __name__ == '__main__':
	res = insertion_sort(a, target)
	print(res)