## You’re testing a new driverless car that is located at the Southwest (bottom-left) corner 
## of an n×n grid. The car is supposed to get to the opposite, Northeast (top-right), corner of 
## the grid. 
# 
## Given n, the size of the grid’s axes, write a function numOfPathsToDest that 
## returns the number of the possible paths the driverless car can take.
##
## For convenience, let’s represent every square in the grid as a pair (i,j). 
## The first coordinate in the pair denotes the east-to-west axis, and the second coordinate 
## denotes the south-to-north axis. The initial state of the car is (0,0), and the 
## destination is (n-1,n-1).

## The car must abide by the following two rules: it cannot cross the diagonal border. 
## In other words, in every step the position (i,j) needs to maintain i >= j. 
## When n = 5. In every step, it may go one square North (up), or one square East (right), 
## but not both. E.g. if the car is at (3,1), it may go to (3,2) or (4,1).

## Input:Output
##
## 1:1
## 2:1
## 3:2
## 4:5
## 5:14
## 6:42

## Dynamic Programming Approach:

def num_of_paths_to_dest(n):
  lastrow = [1]*n
  currrow = [1]*n
  for j in range(1,n):
    for i in range(j,n):
      if i == j:
        currrow[i] = lastrow[i]
      else:
        currrow[i] = currrow[i-1]+lastrow[i]
    lastrow = currrow
  return currrow[n-1]

## Recursive Approach

def num_of_paths_to_dest2(n):
  return helper(n,0,0)

def helper (n,i,j):
  if i==n-1 and j==n-1:
    return 1
  elif i>=n or j>=n:
    return 0
  elif j>i:
    return 0
  else:
    return helper(n,i,j+1) + helper(n,i+1,j)