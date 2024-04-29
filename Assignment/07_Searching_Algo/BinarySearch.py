"""
problem : Binary Search
"""

def binarySearch(arr,K):
    N = len(arr);
    l = 0;
    r = N-1;
    while(l<r):
        mid = (l+r)//2;
        if arr[mid] == K:
            return mid;
        if arr[mid] < K:
            l = mid;
        else:
            r = mid;
    return -1;

arr = [1,2,3,4,5,6];
element = 5
res = binarySearch(arr,element);
print(f"element is present at : {res} index");

            
            