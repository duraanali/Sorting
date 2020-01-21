# TO-DO: complete the helpe function below to merge 2 sorted arrays


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):

    # TO-DO
    if len(arr) > 1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i = i+1
            else:
                arr[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            arr[k] = righthalf[j]
            j = j+1
            k = k+1

    return arr


arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort(arr))
# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO
    L = arr[start:mid]
    R = arr[mid:end]
    i = 0
    j = 0
    k = start
    for l in range(k, end):
        if j >= len(R) or (i < len(L) and L[i] < R[j]):
            arr[l] = L[i]
            i = i + 1
        else:
            arr[l] = R[j]
            j = j + 1
    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO
    if r - l > 1:
        mid = int((l+r)/2)
        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid, r)
        merge_in_place(arr, l, mid, r)
        return arr


arr = [1, 3, 4, 23, 3054, 4005]
merge_sort_in_place(arr, 0, len(arr))
print(arr)
# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt


# def timsort(arr):
#     from random import random
#     arr = [random() for i in range(n)]
#     print(arr)
#     return arr
