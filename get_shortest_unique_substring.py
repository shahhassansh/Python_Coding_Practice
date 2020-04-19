## Given a str and a list of character 'arr', the below code finds shortest substring of str 
## which contains all characters from 'arr'.
##
## Input:
##
## ['x','y','z'], "xyyzyzyx"
##
## Output:
##
## "zyx"


def get_shortest_unique_substring(arr, str):
  head = 0
  tail = len(arr)
  min_len = float('inf')
  min_str = ""
  while tail < len(str)+1:
    if helper(arr,str[head:tail]) == 1:
      if len(str[head:tail]) < min_len:
        min_len = len(str[head:tail])
        min_str = str[head:tail]
      head+=1
    else:
      tail+=1
  return min_str

def helper(arr,substring):
  for a in arr:
    if a not in substring:
      return 0
  return 1