""" In Search problems, we normally assume that the given array is sorted!! """


def linear_search(arr, target):
    """ Linear Search: Time complexity is O(n)
    - Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
    - If x matches with an element, return the index
    - If x doesn’t match with any of elements, return -1
    """
    for _id, item in enumerate(arr):
        if item == target:
            return _id
    return -1


def binary_search(arr, target):
    """ Binary Search: Time complexity is O(log n)
    - Compare x with the middle element
    - If x matches with it, then return the mid index
    - Else if x > mid, then we look to the right half
    - Else(x < mid) we look to the left half
    """
    cursor = len(arr) // 2
    while cursor < len(arr):
        # Check if x is present at mid
        if target == arr[cursor]:
            return cursor
        # If x is greater, ignore left half
        elif target > arr[cursor]:
            cursor += len(arr[cursor:]) // 2
        # If x is smaller, ignore right half
        else:
            cursor -= len(arr[:cursor]) // 2
    return -1


if __name__ == '__main__':
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 3, 4, 5, 10, 20, 30, 40]
    target = 10
    print(linear_search(arr=arr, target=target))
    print(binary_search(arr=arr, target=target))
