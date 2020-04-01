## The below code sort the input array based on absolute value.
## When two elements have same absolute value and they are different, 
## the negative value would appear first before the positive one.
##
## Input:
##
## [2, -7, -2, -2, 0]
##
## Output:
## 
## [0, -2, -2, 2, -7]


def absSort_helper(A):
    if len(A)>1:
        mid = len(A)//2
        L = A[:mid]
        R = A[mid:]
        absSort_helper(L)
        absSort_helper(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if abs(L[i]) < abs(R[j]):
                A[k] = L[i]
                k+=1
                i+=1
            elif abs(L[i]) == abs(R[j]) and L[i] < R[j]:
                A[k] = L[i]
                k+=1
                i+=1
            else:
                A[k] = R[j]
                k+=1
                j+=1
        while i < len(L):
            A[k] = L[i]
            k+=1
            i+=1
        while j < len(R):
            A[k] = R[j]
            k+=1
            j+=1

def absSort(arr):
    absSort_helper(arr)
    return arr

arr = [2, -7, -2, -2, 0]
print(absSort(arr))

        