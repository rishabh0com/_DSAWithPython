
def print_subArray(arr,N):
    for i in range(N):
        for j in range(i,N):
            temp = []
            for k in range(i,j+1):
                temp.append(arr[k]);
            print(temp);
        print();
        
print_subArray([1,2,3,4,5],5)