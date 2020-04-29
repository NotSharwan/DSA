def BubbleSort(a):
    # Sorting in Ascending order.
    for i in range(0, len(a)):
        for j in range(0, len(a)-i-1):  # largest number gets bubbled to the right
            if a[j+1] <= a[j]:  # check adjacent numbers and swap them based on requirement
                a[j], a[j+1] = a[j+1], a[j]

    return a


# Funtion call
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(BubbleSort([1, 6, 8, 0, 3, 9, 7, 4, 2, 5]))
