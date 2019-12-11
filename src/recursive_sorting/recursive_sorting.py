## QUICKSORT (guided project)
def partition(data):
	left = []
	pivot = data[0]
	right = []

	for v in data[1:]:
		if v <= pivot:
			left.append(v)
		else:
			right.append(v)

	return left, pivot, right

def quicksort(data):

	if len(data) <= 1:
		return data

	left, pivot, right = partition(data)

	return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([5, 9, 3, 7, 2, 8, 1, 6]))


# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a = 0
    b = 0

    for i in range(len(merged_arr)):
        if b == len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif a == len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif arrA[a] <= arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        elif arrB[b] <= arrA[a]:
            merged_arr[i] = arrB[b]
            b += 1
      
    return merged_arr

# print(merge([1], [3]))
print(merge([1,3,5,23,41,57, 62], [0,2,4,28,39]))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
