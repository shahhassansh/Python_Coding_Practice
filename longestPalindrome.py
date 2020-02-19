# The Below code calculates the length of the longest Palindrome string in a given STring
# 
# Input:
# 
# 'forpracticeecitcarpfor'
# 
# Output:
#
# 16 
# Because the size of the longest palindrome string 'practiceecitcarp' is 16. 


def longestPalindrome(A):
    maxlength = 1
    low = 0
    high = 0
    l = len(A)
    for i in range(1,l):
        low = i-1
        high = i
        while low>=0 and high < l and A[low] == A[high]:
            maxlength = max(maxlength, high - low +1 )
            low = low - 1
            high = high + 1
            
        low = i-1
        high = i+1
        while low>=0 and high < l and A[low] == A[high]:
            maxlength = max(maxlength, high-low+1)
            low = low-1
            high = high + 1
            
    return maxlength

print(longestPalindrome('forpracticeecitcarpfor'))
