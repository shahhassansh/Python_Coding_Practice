## The below code takes an array as input and a number.
## and return all possible pair of numbers whose difference is equal to a number
##
## Input:
##
## [0, -1, -2, 2, 1], 1
##
## Output:
##
## [[1, 0],[0, -1],[-1,-2],[2,1]]

def findPairwithGivenDifferences(A,B):
    h = {}
    out = []
    for i in range(0,len(A)):
        h[A[i] - B] = A[i]
    for x in A:
        if x in h:
            out.append([h[x],x])
    return out

arr = [0, -1, -2, 2, 1]
k = 1
print(findPairwithGivenDifferences(arr,k))

