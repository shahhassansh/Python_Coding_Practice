## The below code takes two strings as input and return the number of deletion operations
## that would make these two strings same.
##
## Input:
##
## "heat", "hit"
##
## Output:
##
## 3
##
## Input:
##
## "Some", "thing"
##
## Output:
##
## 9

def deletionDistance(A,B):
    m = len(A)
    n = len(B)
    memo = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(0,len(memo)):
        for j in range(0,len(memo[0])):
            if i == 0:
                memo[i][j] = j
            elif j == 0:
                memo[i][j] = i
            elif A[i-1] == B[j-1]:
                memo[i][j] = memo[i-1][j-1]
            else:
                memo[i][j] = 1 + min(memo[i-1][j], memo[i][j-1])
    return memo[i][j]

print(deletionDistance("some","thing"))