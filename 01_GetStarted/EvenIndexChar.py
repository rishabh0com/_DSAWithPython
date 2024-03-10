"""
Problem :
Write a program to accept a string from the user and display characters that are present at an even index number.

"""
# lengthOfString = len(_string_) # returns the length of the string

def evenIndexCharacter(str):
    for i in range(0, len(str)  , 2):
        print("str[",i,"] :",str[i])

# take user input :
evenIndexCharacter(input("Enter string : "));

