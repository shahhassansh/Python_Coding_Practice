## The below code takes input an array which is sorted and shifted and a number and return the
## index of that number in the array.
##
## Input:
##
## [9, 12, 17, 2, 4, 5], 2
##
## Output:
##
## 3

def shifted_arr_search(shiftArr, num):
  start = 0
  end = len(shiftArr) - 1 
  while start <= end:
    mid = (start + end)//2
    if shiftArr[mid] == num:
      return mid
    elif shiftArr[start] <= num < shiftArr[mid] or (shiftArr[start] > shiftArr[mid] and not shiftArr[mid]<num<=shiftArr[end]):
        # We choose left half if either : 
        #    * left half is sorted and B in this range
        #    * left half is not sorted, 
        #      but B isn't in the sorted right half.
      end = mid-1
    else:
      start = mid +1
  return -1