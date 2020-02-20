# The below code sets entire row and column to 0 if an element is 0
# 
# Input:
#
# [[1, 0, 1],
#  [1, 1, 1], 
#  [1, 1, 1]]
#
# Output:
#
# [[0, 0, 0],
#  [1, 0, 1], 
#  [1, 0, 1]]

def setMatrixZeros(A):
    rows = set()
    columns = set()
    for i in range(0,len(A)):
        for j in range(0,len(A[0])):
            if A[i][j] == 0:
                rows.add(i)
                columns.add(j)
    for i in rows:
        for j in range(0,len(A)):
            A[i][j] = 0
    for i in range(0,len(A)):
        for j in columns:
            A[i][j] = 0

    return A

A = [   [1, 0, 1],
        [1, 1, 1], 
        [1, 1, 1]   ]
print(setMatrixZeros(A)) 