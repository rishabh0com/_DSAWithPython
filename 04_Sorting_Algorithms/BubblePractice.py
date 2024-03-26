def bubbleSort(arr):
    N = len(arr);
    
    for i in range(1,N):
        for j in range(0,N-i):
            if(arr[j] < arr[j+1]):
                continue;
            else:
                #swaping elements
                temp = arr[j];
                arr[j] =  arr[j+1];
                arr[j+1] = temp;
    
    return arr;

print(bubbleSort([9,6,2,7,4,1,5,3,8])) # [1,2,3,4,5,6,7,8,9]
        
    