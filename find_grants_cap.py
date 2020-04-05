## The awards committee of your alma mater (i.e. your college/university) asked for your 
## assistance with a budget allocation problem they’re facing. Originally, the committee 
## planned to give N research grants this year. However, due to spending cutbacks, 
## the budget was reduced to newBudget dollars and now they need to reallocate the grants. 
## The committee made a decision that they’d like to impact as few grant recipients as 
## possible by applying a maximum cap on all grants. Every grant initially planned to be 
## higher than cap will now be exactly cap dollars. Grants less or equal to cap, obviously, 
## won’t be impacted.

## Given an array grantsArray of the original grants and the reduced budget newBudget, 
## write a function findGrantsCap that finds in the most efficient manner a cap such that 
## the least number of recipients is impacted and that the new budget constraint is met 
## (i.e. sum of the N reallocated grants equals to newBudget).

## Input:
##
## [2,100,50,120,167], 400
##
## Output:
##
## 128

def find_grants_cap(grantsArray, newBudget):
  grantsArray.sort()
  l = len(grantsArray)
  cap = newBudget*1.0/l
  for i in range(0,len(grantsArray)):
    l = l-1
    if grantsArray[i] < cap:
      newBudget -= grantsArray[i]
      last_cap = cap
      cap = ((newBudget)*1.0)/l
    else:
      return cap
  return last_cap

print(find_grants_cap([2,100,50,120,167], 400))
