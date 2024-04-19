# I am going to implement the brute force algorithm to solve the sliding window problem.
"""
Number of subarray of len K = formula : N - K + 1
it will give the answer how many subArray are possible of len K in Array

Time Complexity :
N-K+1 * K = N*K + K^2 + K
O(N*K)
"""


def subArraylenK(K, N, arr):
    print(f"len({K}) subArrays = {N-K+1}")
    for i in range(N - K + 1):
        temp = []
        for j in range(i, K + i):
            temp.append(arr[j])
        print(f"{i+1} : ", temp)


arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
N = len(arr)
K = 4

subArraylenK(K, N, arr)
