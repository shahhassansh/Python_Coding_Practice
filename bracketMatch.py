## The below code takes input as string of small brackets.
## and returns the number of brackets to add to make it correctly matched.
##
## Input:
##
## "()))("
##
## Output:
##
## 3

def bracketMatch(A):
    st = 0
    end = 0
    for a in A:
        if a == '(':
            st +=1
        elif a == ')' and st ==0:
            end+=1
        else:
            st -=1
    return st+end

A = "()))("
print(bracketMatch(A))