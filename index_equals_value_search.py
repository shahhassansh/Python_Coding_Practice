## The below code implements a function index_equals_value_search that returns the lowest index 
## of the array where index equals the element itself.
##
## The given array has distinct integers.
##
## Input:
##
## [-8,0,2,5]
##
## Output:
##
## 2

def index_equals_value_search(arr):
  start = 0
  end = len(arr)-1

  ans = -1
  while start <=end:
    mid = (start+end)//2
    if arr[mid] == mid:
      ans = mid
      end = mid-1
    elif arr[mid] < mid:
      start = mid+1
    else:
      end = mid-1
        
  return ans

arr = [-8,0,2,5]
print(index_equals_value_search(arr))