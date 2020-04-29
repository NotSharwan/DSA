def PowerSet(originalSet):

    subSets = []

    numberOfCombinations = 2 ** len(originalSet)

    for combinationIndex in range(0, numberOfCombinations):

        subSet = []

        for setElementIndex in range(0, len(originalSet)):

            if combinationIndex & 1 << setElementIndex:
                subSet.append(originalSet[setElementIndex])

        subSets.append(subSet)

    return subSets


# funtion call
print(PowerSet(['1', '2', '3']))
#[[], ['1'], ['2'], ['1', '2'], ['3'], ['1', '3'], ['2', '3'], ['1', '2', '3']]
