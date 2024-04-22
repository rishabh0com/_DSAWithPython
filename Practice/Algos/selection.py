# selection sort

def selectionSort(arr,N):
    
    for i in range(N):
        min_index = i;
        for j in range(i+1,N):
            if arr[j] < arr[min_index]:
                min_index = j
        
        temp = arr[min_index]
        arr[min_index] = arr[i];
        arr[i] = temp;
        
    return arr
arr = [9,1,4,7,3,5];
N = 6
result  = selectionSort(arr,N);
print(result)
        
        
    