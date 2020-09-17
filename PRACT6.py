def selectionSort(A):  
    for i in range(len(A)): 
        small = i 
        for j in range(i+1, len(A)): 
            if A[small] > A[j]: 
                small = j 
        A[i], A[small] = A[small], A[i] 
  

#insertion sort
def insertionSort(arr): 

    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  

#bubble sort
def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                

a = [68, 24, 13, 21, 10]   
opt = input("enter I,B or S for sorting")
if opt == 'I' :
    bubbleSort(a) 
    print("Insertion sort")
    print(a)
elif opt == 'B':
    insertionSort(a)
    print ("Bubblesort")
    print(a)
elif opt == 'S':
    selectionSort(a)
    print ("Selection sort") 
    print(a)
    


