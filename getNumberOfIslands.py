## The below Code takes 2d binary Matrix as input and returns the number of Islands
## 
## Input:
##
## [ [0,    1,    0,    1,    0],
##    [0,    0,    1,    1,    1],
##     [1,    0,    0,    1,    0],
##      [0,    1,    1,    0,    0],
##       [1,    0,    1,    0,    1] ]
##
## Output:
##
## 6

def getNumberOfIslands(binaryMatrix):
    count = 0
    for i in range(0,len(binaryMatrix)):
        for j in range(0,len(binaryMatrix[0])):
            if binaryMatrix[i][j] == 1:
                dfs(binaryMatrix,i,j)
                count+=1
    return count

def dfs(binaryMatrix,i,j):
    if i<0 or j <0 or i > len(binaryMatrix)-1 or j > len(binaryMatrix)-1:
        return
    elif binaryMatrix[i][j] != 1:
        return
    else:
        binaryMatrix[i][j] = -1
        dfs(binaryMatrix,i-1,j)
        dfs(binaryMatrix,i,j-1)
        dfs(binaryMatrix,i+1,j)
        dfs(binaryMatrix,i,j+1)

binaryMatrix = [ [0,    1,    0,    1,    0],
                         [0,    0,    1,    1,    1],
                         [1,    0,    0,    1,    0],
                         [0,    1,    1,    0,    0],
                         [1,    0,    1,    0,    1] ]

print(getNumberOfIslands(binaryMatrix))
