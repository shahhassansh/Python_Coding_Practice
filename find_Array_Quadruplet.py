## The below code takes an array and a number as inputs.
## And it returns a list of 4 elements from the array whose sum is equal to 
## the given number.
##
## Input:
##
## [2, 7, 4, 0, 9, 5, 1, 3]
##
## Output:
##
## [0, 4 , 7, 9]

def find_Array_Quadruplet(A,B):
    A.sort()
    for i in range(0,len(A)):
        for j in range(i+1,len(A)):
            start = j+1
            end = len(A)- 1
            while start < end:
                s = A[i] + A[j] + A[start] + A[end]
                if s == B:
                    return [A[i],A[j],A[start],A[end]]
                elif s < B:
                    start +=1
                else:
                    end -=1
    return []

arr = [2, 7, 4, 0, 9, 5, 1, 3]
s = 20

print(find_Array_Quadruplet(arr,s))
                