def merge(left, right):
	result = []
	left_idx, right_idx = 0, 0
	while left_idx < len(left) and right_idx < len(right):
		if left[left_idx] <= right[right_idx]:
			result.append(left[left_idx])
			left_idx += 1
		else:
			result.append(right[right_idx])
			right_idx += 1

	if left_idx < len(left):
		result.extend(left[left_idx:])
	if right_idx < len(right):
		result.extend(right[right_idx:])
	return result

def merge_sort(m):
	if len(m) <= 1:
		return m

	mid = len(m) // 2
	left = m[:mid]
	right = m[mid:]

	left = merge_sort(left)
	right = merge_sort(right)
	return list(merge(left, right))

if __name__ == '__main__':
	arr = [4,6,1,7,5,9]
	res = merge_sort(arr)
	print(res)