"""
SOURCE: ABCDEFG
TARGET: ABDFFGH
DP MATRIX:
  A B D F F G H
A 0 1 2 3 4 5 6
B 1 0 1 2 3 4 5
C 2 1 2 3 4 5 6
D 3 2 1 2 3 4 5
E 4 3 2 3 4 5 6
F 5 4 3 2 3 4 5
G 6 5 4 3 4 3 4
OUTPUT:
["A", "B", "-C", "D", "-E", "F", "+F", "G", "+H"]

SOURCE: CBBC
TARGET: CABAABBC 
DP MATRIX:
  C A B A A B B C
C 0 1 2 3 4 5 6 7              
B 1 2 1 2 3 4 5 6
B 2 3 2 3 4 3 4 5
C 3 4 3 4 5 4 5 4
OUTPUT: 
["C","+A","B","+A","+A","B","+B","C"]

SOURCE: "CABAAABBC" 
TARGET: "CBBC"
DP MATRIX:
  C B B C
C 0 1 2 3
A 1 2 3 4
B 2 1 2 3
A 3 2 3 4
A 4 3 4 5
A 5 4 5 6
B 6 5 4 5
B 7 6 5 6
C 8 7 6 5
OUTPUT:
["C","-A","B","-A","-A","-A","B","-B","C"]
"""

def diffBetweenTwoStrings(source, target):
  m = len(source)
  n = len(target)
  dp =[[0 for i in range(n)] for j in range(m)]
  for i in range(m):
    for j in range(n):
      if i == 0:
        dp[i][j] = j
      elif j == 0:
        dp[i][j] = i
      elif source[i]==target[j]:
        dp[i][j] = dp[i-1][j-1]
      else:
        dp[i][j]= 1 + min(dp[i-1][j],dp[i][j-1])
  print(dp)   

  i = j = 0
  ans = []
  while i < len(source)-1 and j < len(target)-1:
    if source[i] == target[j]:
      ans.append(source[i])
      print(source[i]+str(i)+str(j))
      i+=1
      j+=1
    else:
      if dp[i+1][j] < dp[i][j+1]:
        ans.append('-'+source[i])
        print('-'+source[i]+str(i)+str(j))
        i+=1

      else:
        ans.append('+'+target[j])
        print('+'+target[j]+str(i)+str(j))
        j+=1
  while j < len(target):
    if i>=len(source):
      ans.append('+'+target[j])
      j+=1
    elif source[i] == target[j]:
      ans.append(source[i])
      i+=1
      j+=1
    else:
      ans.append('+'+target[j])
      j+=1
      
      
  return ans
      
"""
  while j < len(target):
    ans.append('+'+target[j])
    j+=1

  """  
                   


print(diffBetweenTwoStrings('CBBC','CABAABBC'))
#print(diffBetweenTwoStrings('ABCDEFG','ABDFFGH'))