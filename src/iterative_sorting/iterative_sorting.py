# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    length = len(arr)

    for i in range(length):

        for j in range(0, length-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    if len(arr) == 0:
        return arr

    maximum = max(arr)
    minimum = min(arr)

    count_dict = {}
    for i in range(minimum, maximum+1):
        count_dict[i] = 0

    sorted_arr = [None] * len(arr)

    for num in arr:
        if num < 0:
            return "Error, negative numbers not allowed in Count Sort"
        else:
            count_dict[num] += 1

    for i in range(minimum+1, maximum+1):
        count_dict[i] = count_dict[i] + count_dict[i-1]

    for num in arr:
        sorted_arr[count_dict[num]-1] = num
        count_dict[num] -= 1

    return sorted_arr
