# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(arr)):     
            if arr[j] < arr[smallest_index]:
                smallest_index = j


        # TO-DO: swap
        temp = arr[i]  
        arr[i] = arr[smallest_index]  
        arr[smallest_index] = temp

    return arr

arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
selection_sort(arr)

print(arr)
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
bubble_sort(arr)

print(arr)
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr