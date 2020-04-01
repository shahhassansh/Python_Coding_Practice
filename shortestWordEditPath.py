## Given two words source and target, and a list of words words, 
## find the length of the shortest series of edits that transforms source to target.
##
## Each edit must change exactly one letter at a time, 
## and each intermediate word (and the final target word) must exist in words.
##
## Input:
##
## source = "bit"
## target = "dog"
## words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
##
## Output:
##
## 5
##
## because of the path
##
## bit -> but -> put -> pot -> pog -> dog has 5 transitions.

def shortestWordEditPath(A, B, arr):
    visited = set()
    queue = []
    queue.append(A)
    count = 0
    while queue:
        n = len(queue)    
        for i in range(0,n):
            x = queue.pop(0)
            if x not in visited:
                visited.add(x)
                if x == B:
                    return count   
            temp = findWord(x, arr)
            if queue:
                queue = queue + temp
            else:
                queue = temp
            if len(arr) == len(visited):
                if B not in queue:
                    return -1
        count = count + 1  
    return -1
    
def findWord(A, arr):
    out = []
    for a in arr:
        cnt = 0
        for i in range(0,len(a)):
            if a[i] != A[i]:
                cnt += 1
        if cnt == 1:
            out.append(a)
    return out

source = "bit"
target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]

print(shortestWordEditPath(source, target, words))
