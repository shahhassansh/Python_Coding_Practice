## Given an n-by-3 list, where 0th element represents timestamp, 1st element represents number
## of visitors and 2nd element represents where visitors enter (1) or exit (0). 
## 
## The below code returns the timestamp where the venue has highest number of visitors. 
##
## Input:
##
## [[1487799425,14,1],[1487799425,4,0],[1487799425,2,0],[1487800378,10,1],
# [1487801478,18,0],[1487801478,19,1],[1487801478,1,0],[1487801478,1,1],
# [1487901013,1,0],[1487901211,7,1],[1487901211,8,0]]
##
## Output:
##
## 1487800378

def find_busiest_period(data):
  pre_t = data[0][0]
  if data[0][2] == 1:
    pre_v = data[0][1]
  else:
    pre_v = -1*data[0][1]
  no_visitor = float('-inf')
  out_t = 0
  for i in range(1,len(data)):
    if data[i][0] == pre_t:
      if data[i][2] == 1:
        pre_v += data[i][1]
      else:
        pre_v -= data[i][1]
    else:
      if pre_v > no_visitor:
        no_visitor = pre_v
        out_t = data[i-1][0]
        if data[i][2] == 1:
          pre_v = data[i][1]
        else:
          pre_v = -1*data[i][1]
        pre_t = data[i][0]
  if pre_v > no_visitor:
    no_visitor = pre_v
    out_t = data[len(data)-1][0]
  return out_t

print(find_busiest_period([[1487799425,14,1],[1487799425,4,0],[1487799425,2,0],[1487800378,10,1],[1487801478,18,0],[1487801478,19,1],[1487801478,1,0],[1487801478,1,1],[1487901013,1,0],[1487901211,7,1],[1487901211,8,0]]))