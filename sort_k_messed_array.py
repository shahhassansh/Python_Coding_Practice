## Given an array of integers arr where each element is at most k places 
## away from its sorted position, the below code sorts the given array.
##
## Input:
##
## [1,4,3,2,5,7,6,10,8,9], 2
## 
## Output:
##
## [1, 2, 3, 4, 5, 6, 7, 8, 9]      


def sort_k_messed_array(arr, k):
  for i in range(len(arr)):
    start = i+1
    end = min(i+k+1, len(arr)-1)
    for j in range(start,end+1):
      if arr[j] < arr[i]:
        arr[i],arr[j] = arr[j],arr[i]
  return arr

arr = [1,4,3,2,5,7,6,10,8,9]
k = 2
print(sort_k_messed_array(arr,k))