
def bubble(N,arr):
    
    for i in range(1,N):
        for j in range(N-i):
            if arr[j] > arr[j+1]:
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp
                print(arr)
        print()
    print(arr);
    
bubble(6,[9,7,4,2,8,1])