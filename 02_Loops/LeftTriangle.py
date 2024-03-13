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

"""
Problem_3 : print following pattern.

1
2  3
4  5  6
7  8  9  10
11 12 13 14 15
"""

print("problem 3 :")


def problem_3(num_of_row):
    pattern = 1
    for row in range(0, num_of_row):
        for col in range(1, row + 2):
            print(
                pattern,
                end=" ",
            )
            pattern += 1
        print("\n")


# function invoked problem 3 :
problem_3(5)

'''
Problem_3 : print following pattern :
*
*  *
*    *
*      *
*  *  *  *
'''

def problem_4(num_of_row):
    print("problem_4 : ")
    for row in range(0,num_of_row):
        for col in range(0,row):
            if col == 0 or col == row - 1 or row == num_of_row -1:
               print("*  ",end=" ");
            else:
                print("   ", end=" ")
            
        print("\n");
        
# function invoked
problem_4(6)