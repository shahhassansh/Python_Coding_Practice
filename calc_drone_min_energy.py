## Given an array route of 3D points, the below code implements a function calcDroneMinEnergy that computes and returns 
## the minimal amount of energy the drone would need to complete its route. 
## The code assumes that the drone starts its flight at the first point in route. 
## That is, no energy was expended to place the drone at the starting point.

## The drone burns 1 kWh (kilowatt-hour is an energy unit) for every mile it ascends, 
## and it gains 1 kWh for every mile it descends. 
## Flying sideways neither burns nor adds any energy.

## Input:
##
## [ [0,   2, 10],
##   [3,   5,  0],
##   [9,  20,  6],
##   [10, 12, 15],
##   [10, 10,  8] ]
##
## Output:
##
## 5

def calc_drone_min_energy(route):
  ans = 0
  diff_z = 0
  z = route[0][2]
  for i in range(1,len(route)):
    diff_z = diff_z + (z - route[i][2])
    z = route[i][2]
    ans = min(ans,diff_z)
  return -1*ans
 
route = [ [0,   2, 10],
                  [3,   5,  0],
                  [9,  20,  6],
                  [10, 12, 15],
                  [10, 10,  8] ]


print(calc_drone_min_energy(route))