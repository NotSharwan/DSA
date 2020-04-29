def BinarySearch(array, element):
    low = 0
    high = len(array)-1
    while low <= high:
        mid = int((low+high)/2)
        if element < array[mid]:
            high = mid-1
        elif element > array[mid]:
            low = mid+1
        else:
            return mid
    return -1


# function call
print(BinarySearch([1, 4, 6, 8, 9], 1))  # 0
