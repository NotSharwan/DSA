def InsertionSort(a):
    # sorting in ascending order
    pos = 0
    for i in range(0, len(a)):  # ith element is to be compared with all elements before
        # j elements are to left of i which are to be checked for insertion of ith element
        for j in range(0, i):
            if a[i] <= a[j]:
                pos = j  # postion the ith element is to be inserted
                # store the ith element before removing from the list
                elem = a[i]
                a.pop(i)  # pop the ith element
                a.insert(pos, elem)  # insert ith element at the right position
    return a


# Function Call
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(InsertionSort([1, 6, 8, 0, 3, 9, 7, 4, 2, 5]))
