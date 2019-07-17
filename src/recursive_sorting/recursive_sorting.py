# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    # # TO-DO
    merged_list = []
    while len(arrA) > 0 and len(arrB) > 0:
        if(arrA[0] < arrB[0]):
            merged_list.append(arrA[0])
            # print(merged_list)
            arrA.pop(0)
        else:
            merged_list.append(arrB[0])
            arrB.pop(0)
    if(len(arrA) == 0):
        left_list = arrB

    elif(len(arrB) == 0):
        left_list = arrA

    while len(left_list) > 0:
        merged_list.append(left_list[0])
        left_list.pop(0)

    return merged_list


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    # start 0 end middle point
    left_side = arr[0: middle]
    # start middle and end len(arr)
    right_side = arr[middle:]
    left_result = merge_sort(left_side)
    right_result = merge_sort(right_side)

    return merge(left_result, right_result)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    start2 = mid + 1

    # If the direct merge is already sorted
    if (arr[mid] <= arr[start2]):
        return arr

    # Two pointers to maintain start
    # of both arrays to merge
    while start <= mid and start2 <= end:

        # If element 1 is in right place
        if arr[start] <= arr[start2]:
            start += 1

        else:
            value = arr[start2]
            index = start2

            # Shift all the elements between element 1
            # element 2, right by 1.
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1

    return arr


def merge_sort_in_place(arr, l, r):
    if l < r:

        # Same as (l + r) / 2, but avoids overflow
        # for large l and r
        m = l + (r - l) // 2

        # Sort first and second halves
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)

        merge_in_place(arr, l, m, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
