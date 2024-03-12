'''
Problem_1 : print following pattern
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
print("problem 1 : ")
def problem_1(num_of_row):
    for row in range(1,num_of_row + 1):
        for col in range(1,row + 1):
            print(col, end=" ")
        print("\n");

# function invoked problem_1:
problem_1(5)

"""
Problem_2 : print following pattern.

1
2 2
3 3 3
4 4 4 4 
"""

print("problem 2 :")


def problem_2(num_of_row):
    pattern = ""
    for row in range(1, num_of_row + 1):
        for col in range(1, row + 1):
            pattern += str(row) + " "
        print(pattern + "\n")
        pattern = ""


# function invoked problem_2 :
problem_2(5);

