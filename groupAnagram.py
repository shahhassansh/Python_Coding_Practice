# The below return all group of strings that are anagrams where a group is represented as
# a list of integers representing index in the original list.
# 
# Iuput:
# 
# ['cat','dog','god','tca']
# 
# Output:
# 
# [[1,4],[2,3]] 

def anagram(A):
    h = {}
    for i, x in enumerate(A):
        sorted_word = ''.join(sorted(x))
        if sorted_word not in h:
            h[sorted_word] = [i+1]
        else:
            h[sorted_word] = h[sorted_word] + [i+1]
    
    return list(h.values())

A = ['cat','dog','god','tca']
print(anagram(A))
