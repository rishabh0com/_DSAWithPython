"""
Problem : remove "nth" character from string.

"""

def removeNthCharacter(str,index):
    newStr = "";
    if index < 1 or index > len(str):
        return "'message : please enter index 1 to nth last character of string.'"
    for i in range(0,len(str)):
        if i == index-1:
            continue;
        newStr += str[i]
    return ("New word : "+ newStr)

print(removeNthCharacter(input("Enter Word : "), int(input("Enter index from 1-nth : "))))
