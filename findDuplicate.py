## The below code takes two arrays as input and return a list with all elements 
## which are common in these arrays
# 
# Input: 
#
# arr1 = [1, 2, 3, 5, 6, 7]
# arr2 = [3, 6, 7, 8, 20]
#
# Output:
#
# [3, 6, 7]

def findDuplicate(arr1, arr2):
    out = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            out.append(arr1[i])
            i = i+1
            j = j+1
        else:
            if arr1[i] < arr2[j]:
                i = i+1
            else:
                j = j+1
    return out

arr1 = [1, 2, 3, 5, 6, 7]
arr2 = [3, 6, 7, 8, 20]

print(findDuplicate(arr1, arr2))