## The below code takes an array and a number as input 
## and returns the two indices from the array whose element's sum is the Number.
##
##
## Input:
##
## [4, 6, 10, 15, 16], 21
##
## Output:
##
## [1,3]


def twoSumIndices(A,B):
    d = {}
    for i in range(0,len(A)):
        if B - A[i] in d:
            return [d[B-A[i]],i]
        else:
            d[A[i]] = i
    return []

arr = [4, 6, 10, 15, 16]
lim = 21

print(twoSumIndices(arr,lim))