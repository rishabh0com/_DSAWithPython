"""
Problem : print Rhombus pattern :

                                  0
                               0  1  0
                            0  1  2  1  0
                         0  1  2  3  2  1  0
                      0  1  2  3  4  3  2  1  0
                    0 1  2  3  4  5  4  3  2  1 0
                      0  1  2  3  4  3  2  1  0
                         0  1  2  3  2  1  0
                            0  1  2  1  0
                               0  1  0
                                  0  

"""

def rhombus(n):
    n=n+1;
    for i in range(n):
        print("  " * (n - i - 1), end="")
        for j in range(i + 1):
            print(f"{j} ", end="")
        for k in range(i - 1, -1, -1):
            print(f"{k} ", end="")
        print()
    for i in range(n - 2, -1, -1):
        print("  " * (n - i - 1), end="")
        for j in range(i + 1):
            print(f"{j} ", end="")
        for k in range(i - 1, -1, -1):
            print(f"{k} ", end="")
        print()



rhombus(6)
