## A letter can be encoded to a number in the following way:
## 'A' -> '1', 'B' -> '2', 'C' -> '3', ..., 'Z' -> '26'
## Given a string of digits S from 0-9 representing an encoded message, 
## the below code returns the number of ways to decode it.
##
## Input:
##
## '1262'
##
## Output:
##
## 3
##
## i.e. [1,2,6,2],[12,6,2],[1,26,2]

def decodeVariations(S):
  dp = [1]*(len(S)+1)
  for i in range(len(S)-1,-1,-1):
    if S[i] == '0':
      dp[i]=0
    elif S[i]=='1':
      dp[i]=dp[i+1]
      if i+1<len(S):
        dp[i]+=dp[i+2]
    elif S[i] =='2':
      dp[i]=dp[i+1]
      if i+1<len(S):
        if S[i+1] < '7':
          dp[i]+=dp[i+2]
    else:
      dp[i] = dp[i+1]
  return dp[0]

print(decodeVariations('1262'))