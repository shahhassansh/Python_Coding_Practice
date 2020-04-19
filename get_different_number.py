## The code takes input an array of whole numbers and returns the first whole number that does
## not appear in the array.
##
## Input:
##
## [4,3,2,1,0]
##
## Output:
##        
## 5
## 
## Input:
##
## [0,1,3,2,5]
##
## Output:
##
## 4

## First Approach (Time: O(n), Space: O(n))

def get_different_number2(arr):
  s = set()
  for a in arr:
    s.add(a)
  i = 0  
  while 1:
    if i not in s:
      return i
    i+=1

## Second Approach (Time: O(n), Space: O(1))

def get_different_number(arr):
  for i in range(0,len(arr)):
    while arr[i] < len(arr) and arr[i] != i:
      tmp = arr[arr[i]]
      arr[arr[i]] = arr[i]
      arr[i] = tmp
  for i in range(0,len(arr)):
    if i != arr[i]:
      return i
  return len(arr)

