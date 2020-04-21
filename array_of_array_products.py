## The below code takes input an array and return another array of same size where each element is
## the product of all elements except the element on the same index.
##
## Input:
##
## [8,10,2]
##
## Output:
##
## [20,16,80]

def array_of_array_products(arr):
    if len(arr) <= 1:
      return []
    productArr = [0]*len(arr)
    temp =1
    for i in range(0,len(arr)):
        productArr[i] = temp
        temp *= arr[i]

    temp = 1
    for i in range(len(arr)-1,-1,-1):
        productArr[i] *= temp
        temp *=arr[i]
    return productArr


print(array_of_array_products([8,10,2]))