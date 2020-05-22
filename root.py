## The below code implements a function root that calculates the n’th root of a number. 
## The function takes a nonnegative number x and a positive integer n, and returns the 
## positive n’th root of x within an error of 0.001.
##
## Input:
##
## 27,3
##
## Output:
##
## 3

def root(x, n):
  lowerBound = 0
  upperBound = x
  mid = ((lowerBound + upperBound)*1.0) /2
  while abs(mid**n - x) >0.001:
    print(mid)
    if mid**n > x:
      upperBound = mid
    else:
      lowerBound = mid
    mid = ((lowerBound + upperBound)*1.0) /2
  return mid

print(root(7,3))