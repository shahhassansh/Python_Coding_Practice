## The below input takes a sentence and returns word count ignoring special character. 
##
## Input:
##
## 
## "Every book is a quotation; and every house is a quotation out of all forests, and mines, and stone quarries; and every man is a quotation from all his ancestors. "
##
## Output:
##
## [["and","4"],["every","3"],["is","3"],["a","3"],["quotation","3"],["all","2"],["book","1"],["house","1"],["out","1"],["of","1"],["forests","1"],["mines","1"],["stone","1"],["quarries","1"],["man","1"],["from","1"],["his","1"],["ancestors","1"]]

def word_count_engine(document):
  document = document.lower()
  document = list(document)
  document2 =[]
  for i in range(0,len(document)):
    if document[i] in "abcdefghijklmnopqrstuvwxyz ":
        document2.append(document[i])
  document = ''.join(document2)
  document = document.split(" ")
  d = {}
  for a in document:
    if a not in d:
      d[a] = 1
    else:
      d[a] += 1
  out = []
  for a in document:
    print(a)
    if d[a] != -1 and a != '':
      out.append([a,str(d[a])])
      d[a] = -1
  #for a,b in d.items():
    #out.append([a,b])
  
  out.sort(key = lambda i: i[1], reverse = True)
  
  return out