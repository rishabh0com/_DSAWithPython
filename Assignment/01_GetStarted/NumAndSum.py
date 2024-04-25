"""
Problem : Write a program to iterate the first 10 numbers,  
and in each iteration, print the sum of the current and previous number.
"""


def iterationSum():
    sumOfCount = 0
    for i in range(0, 10):
        print(
            ("Current Number = "),
            (i),
            (", previous number = "),
            (0 if i == 0 else i - 1),
            (", sum = "),
            (i + (0 if i == 0 else i - 1)),
        )


iterationSum()  # invoked the function

# logic : I have written logic for privious number "0 if i == 0 else i - 1"
""" 
used ternary operator for logic 
//statement(condition_true) if <condition> else //statement(condition_false) 

"""
