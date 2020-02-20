# The below code returns all unique triplets in an array whose sum is 0
# Input:
#
# [-1,2,1,0,4,-3]
#
# Output:
#
# [[-1,0,1],[-3,1,2],[4,-3,-1]]

def threeSumZeros(A):
    n = len(A)
    A.sort()
    res = set()
    for i in range(n-2):
        left = i+1
        right = n-1
        while left < right:
            s = A[i] +A[left]+A[right]
            if s == 0:
                res.add((A[i],A[left],A[right]))
                left = left + 1
            elif s > 0:
                right = right - 1
            else:
                left = left + 1
    return list(res)



