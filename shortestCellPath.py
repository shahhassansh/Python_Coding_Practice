## The below code takes input a grid, a source index and a target address and returns 
## the length of path source can reach to target. 
## The path can only contains 1's from the given binary grid (2-d array)
##
## Input:
##
## [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]], 0,0,2,0
##
## Output:
##
## 8


def shortestCellPath(grid, sr, sc, tr, tc):
  queue =[[sr,sc,0]]
  seen = set()
  while queue:
    curr = queue.pop(0)
    temp = [[curr[0]-1,curr[1]],[curr[0]+1,curr[1]],[curr[0],curr[1]-1],[curr[0],curr[1]+1]]
    for x in temp:
      temp2 = [x[0],x[1],curr[2]+1]
      if x[0] >= 0 and x[0]< len(grid) and x[1] >=0 and x[1] <len(grid[0]) and grid[x[0]][x[1]] == 1 and tuple(x) not in seen:
        queue.append(temp2)
        seen.add(tuple(x))
        if x[0] == tr and x[1] == tc:
          return curr[2]+1
  return -1