"""
Problem : Input a matrix of size 3 * 3 and print it.
"""

def inputMatrix(rows):
    matrix = []
    for _ in range(rows):
        matrix.append(list(map(int,input(f"Enter {_+1} row of elements for 3 x 3 matrix : ").strip().split())));
    print(matrix);
    
    
inputMatrix(3);