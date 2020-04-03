## The below code takes input a 2d Matrix and return spiral copy of the elements
## in a list
##
## Input:
##
## [[1,    2,   3,  4,    5],
##  [6,    7,   8,  9,   10],
##  [11,  12,  13,  14,  15],
##  [16,  17,  18,  19,  20] ]
##
## Output:
##                           
## [1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12]


def spiral_copy(inputMatrix):
  out = []
  rot =0 
  left = 0
  top = 0
  right = len(inputMatrix[0])-1
  bottom = len(inputMatrix)-1
  while left <= right and top <= bottom:
    if rot == 0:
      for i in range(left,right+1):
        out.append(inputMatrix[top][i])
      top+=1
      rot =1
    elif rot == 1:
      for i in range(top,bottom+1):
        out.append(inputMatrix[i][right])
      right-=1
      rot = 2
    elif rot == 2:
      for i in range(right, left-1,-1):
        out.append(inputMatrix[bottom][i])
      bottom-=1
      rot =3
    elif rot == 3:
      for i in range(bottom,top-1,-1):
        out.append(inputMatrix[i][left])
      left +=1
      rot =0
  return out

A = [[1,    2,   3,  4,    5],
[6,    7,   8,  9,   10],
[11,  12,  13,  14,  15],
[16,  17,  18,  19,  20] ]

print(spiral_copy(A))