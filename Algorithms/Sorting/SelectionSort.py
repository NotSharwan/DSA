def SelectionSort(a):
    # sorting in ascending order
    for i in range(0, len(a)):
        # set element in position i as minimum for the iteration.
        minimum = a[i]
        pos = i  # position.
        for j in range(i, len(a)):  # run loop from i to length(a)
            if a[j] <= minimum:
                # if jth element is lesser than minimum, update minimum and position.
                minimum = a[j]
                pos = j
        temp = a[i]  # swap ith element with minimum element using it position.
        a[i] = minimum
        a[pos] = temp
    return a


# Function call
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(SelectionSort([1, 6, 8, 0, 3, 9, 7, 4, 2, 5]))
