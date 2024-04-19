"""
find subArray of length K using optimize approche of sliding window
Time Complexity :
K + N
O(N)
"""

def findSubArrayOfLenK(N,K,arr):
    temp = [];
    for i in range(K):
        temp.append(arr[i]);
        
    print(temp)
    for j in range(K,N): # j = 4 , N = 9
        temp.remove(arr[j-K]);
        temp.append(arr[j])
        print(temp)

arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
N = len(arr)
K = 4

findSubArrayOfLenK(N,K,arr)
