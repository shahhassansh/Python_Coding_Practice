## The code implements a function which return True if the given 2-d Matrix is Toeplitz or not.
## A Toeplitz matrix is a matrix where every left-to-right-descending diagonal has the same element.
## Input:
##
## [[1,2,3,4],
## [5,1,2,3],
## [6,5,1,2]]
##
## True

def isToeplitz(arr):
  if len(arr) <= 1 or len(arr[0]) <= 1:
    return True
  for i in range(1,len(arr)):
    for j in range(1,len(arr[0])):
      if arr[i][j] != arr[i-1][j-1]:
        return False
  return True