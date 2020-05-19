## The below code takes a string and Pattern and return 'True' if string follows the pattern.
## If the string doesn't follow the pattern, The code return 'False'
##
## Input:
## 
## 1. 'aa','a'
## 2. 'aa', 'aa'
## 3. 'abc', 'a*c'        
## 4. 'acd', 'ab*c.'
## 5. 'abbb', 'ab*'
##
## Output:
##
## 1. False
## 2. True
## 3. False
## 4. True
## 5. True
##

def is_Match(s,p):
    m = len(s)
    n = len(p)
    dp = [[False for i in range(n+1)] for j in range(m+1)]
    dp[0][0] = True
    for j in range(1,n+1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]
    for i in range(1,m+1):
        for j in range(1, n+1):
            if s[i-1] == p[j-1] or p[j-1]== '.':
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i][j-2]
                if p[j-2] == s[i-1] or p[j-2] == '.':
                    dp[i][j] = dp[i][j] or dp[i-1][j]
            else:
                dp[i][j] = False
    return dp[m][n]

print(is_Match('abc','ab*c'))