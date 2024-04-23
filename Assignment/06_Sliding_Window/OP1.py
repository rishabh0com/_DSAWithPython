"""
* variable size sliding window :

N = 6
sum = 33
find is there any Sub array with the given sum return true/false
"""

def findSubArrayWithSum(N,Sum,arr):
    tempSum = 0
    r = 0
    for l in range(0,N):
        while(r<N and Sum > tempSum):
            tempSum += arr[r];
            r += 1;
        if Sum == tempSum:
            return True;
        tempSum -= arr[l];
    return False;

N = 6;
Sum = 33
arr = [1,4,20,3,10,5];

print(findSubArrayWithSum(N,Sum,arr))
        
            