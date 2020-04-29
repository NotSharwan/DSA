def LinearSearch(array, element):

    for i in range(len(array)):

        if array[i] == element:
            return i+1

    return -1


# Function call
print(LinearSearch([7, 4, 88, 35, 7, 33, 89], 88))  # 3
print(LinearSearch([7, 4, 88, 35, 7, 33, 89], 87))  # -1
