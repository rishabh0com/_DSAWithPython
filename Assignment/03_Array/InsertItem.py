def insertItem(arr,item):
    newArr = []
    for i in range(len(arr)+1):
        if i <len(arr) :
            newArr.append(arr[i]);
        else:
            newArr.append(item);

    return newArr;

print(insertItem([1,2,3],7)); # inset only integer value
