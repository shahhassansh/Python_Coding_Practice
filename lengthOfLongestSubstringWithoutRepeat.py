# The below Code return the length of largest Substring without repeating characters
# 
# Input:
#
# 'abcabcaba'
#
# Output:
#
# 3


def lengthofLongestSubstringWithoutRepeat(A):
    i = 0
    j = 0
    res = 0
    n = len(A)
    s=set()
    while i < n and j < n:
        if A[j] in s:
            s.remove(A[i])
            i = i + 1
        else:
            s.add(A[j])
            j = j + 1
            res = max(res,j-i)
    return res

A = 'abcabcaba'
print(lengthofLongestSubstringWithoutRepeat(A))