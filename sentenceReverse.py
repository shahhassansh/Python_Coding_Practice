## The below code reverses the order of the words in the array.
##
## Input:
##
## ['p', 'r', 'a', 'c', 't', 'i', 'c', 'e', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'e', 'r', 'f', 'e', 'c', 't']
##
## Output:
##
## ['p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e']

def word_reverse(arr):
  start = 0
  end = len(arr)-1
  while start < end:
    arr[start],arr[end] = arr[end],arr[start]
    start +=1
    end -=1
  return arr

def sentenceReverse(arr):
  arr = word_reverse(arr)
  i = 0
  while i < len(arr):
    start = i
    end = i
    while arr[end] != ' ' and end <len(arr):
      end+=1
      if end>=len(arr):
        break
    i=end+1
    end -=1
    while start < end:
      arr[start],arr[end] = arr[end],arr[start]
      start += 1
      end -= 1
  return arr
    
arr = 'practice makes perfect'
print(list(arr))
print(sentenceReverse(list(arr)))
