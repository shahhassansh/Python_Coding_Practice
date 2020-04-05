## The below code implements a function meeting_Planner that given the availability, slotsA and slotsB, 
## of two people and a meeting duration dur, returns the earliest time slot that works for both of them 
## and is of duration dur. If there is no common time slot that satisfies the duration 
## requirement, return an empty array.
##
## Input:
##
## [[1,10]], [[2,3],[5,7]], 2
##
## Output:
##
## [5,7]

def meeting_planner(slotsA, slotsB, dur):
  ia = ib = 0
  while ia < len(slotsA) and ib < len(slotsB):
    start = max(slotsA[ia][0],slotsB[ib][0])
    end = min(slotsA[ia][1],slotsB[ib][1])
    if (end - start) >= dur:
      return [start,start+dur]
    elif slotsA[ia][1] < slotsB[ib][1]:
      ia += 1
    else:
      ib += 1
  return []

