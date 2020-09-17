def linearSearch(arr, x): 
    for i in range(len(arr)): 
        if arr[i] == x: 
            return i 

def binary_search(arr, x): 
    low = 0
    high = len(arr) - 1
    mid = 0
  
    while low <= high: 
        mid = (high + low) // 2
        if arr[mid] < x: 
            low = mid + 1

        elif arr[mid] > x: 
            high = mid - 1
  
        else: 
            return mid 
  
  
arr = [ 4, 6, 9, 20, 70 ] 
x = 20
  

opt = input("enter l or B  for searching")
if opt == "B":
    result= binary_search(arr,x)
    print("Binary search")
    print(result)
    
elif opt == "l":
    result= linearSearch(arr,x)
    print("Linear search")
    print(result)
