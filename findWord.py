## The below code takes a string and a list of strings as input and 
## return all strings from the list that is only one character different than 
## the given string. 
##
## Input:
##
## source = "bit"
## words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
## 
## Output:
## 
## ["but", "big"]

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
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
print(findWord(source, words))