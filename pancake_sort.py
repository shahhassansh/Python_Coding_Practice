## The below code implements pancakeSort using flip function.
##
## The function flip(arr, k) reverses the order of the first k elements in the array arr.
## The function pancakeSort(arr) sorts and returns the input array using only the function flip.
##
## Input:
##
## [1, 5, 4, 3, 2]
##
## Output:
##
## [1, 2, 3, 4, 5]

def pancake_sort(arr):
  for i in range(len(arr)-1,0,-1):
    max_index = find_max_index(arr[0:i+1])
    arr = flip(arr,max_index+1)
    arr = flip(arr,i+1)
  return arr
    
def flip(arr,k):
  start = 0
  end = k-1
  while start<end:
    arr[start],arr[end] = arr[end],arr[start]
    start+=1
    end-=1
  return arr

def find_max_index(arr):
  max = float('-inf')
  for i in range(len(arr)):
    if arr[i] > max:
      res = i
      max = arr[i]
  return res

arr = [1, 5, 4, 3, 2]
print(flip(arr,3))
print(find_max_index(arr))
print(pancake_sort(arr))