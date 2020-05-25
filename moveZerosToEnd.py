## The below code moves all zeros in the array to the end of the array. 
##
## Input:
##
## [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]
##
## Output:
##
## [1, 10, 2, 8, 3, 6, 4, 5, 7, 0, 0, 0, 0, 0]

def moveZerosToEnd(arr):
  if len(arr) <=1:
    return arr
  zero_id = -1
  for i in range(len(arr)):
    if arr[i] == 0: 
      if zero_id == -1:
        zero_id = i # [0,0,3]
    elif zero_id != -1:
      arr[i],arr[zero_id] = arr[zero_id],arr[i]
      zero_id+=1
  return arr

"""
def moveZerosToEnd(arr):
  if len(arr) <=1:
    return arr
  left = 0
  right = 1
  while right < len(arr):
    if arr[left] != 0 and arr[right] != 0:
      left+=2
      right+=2
    elif arr[left] == 0 and arr[right] != 0:
      arr[left], arr[right] = arr[right], arr[left]
      left+=1
      right+=1
    elif arr[left] != 0 and arr[right] == 0:
      left+=1
      right+=1
    else:
      right+=1
  return arr
"""