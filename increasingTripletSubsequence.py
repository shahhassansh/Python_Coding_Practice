# The below code takes input an array of numbers and returns 1 if the input array has 
# an increasing triplet subsequence. An increasing triplet subsequence is defined as 
# for any i,j,k in the array A such that -1<i<j<k<len(array), there should exist atleast 
# one scenario when A[i] < A[j] < A[k]
# 
# Input:
# 
# [5,3,8,2,7,9,4]
#   
# Output:
#
# 1

def increasingTripletSubsequence(A):
    mini = float('inf')
    sec_mini = float('inf')
    for a in A:
        if a <= mini:
            mini = a
        elif a <= sec_mini:
            sec_mini = a
        else:
            return 1
    return 0

A = [5,3,8,2,7,9,4]
print(increasingTripletSubsequence(A))