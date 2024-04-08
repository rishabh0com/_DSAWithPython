# there is arr -> Array , n -> arr's length
def subArray(arr, n):
    for i in range(0, n):
        print(f"\narray of {n-i} length :")
        for j in range(i, n):
            for k in range(i, j + 1):
                print(arr[k], end=" ")
            print("")


subArray([1, 2, 3, 4], 4)
