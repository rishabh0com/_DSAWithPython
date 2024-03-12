"""
Problem : Print natural numbers from 1 to nth user number  using while loop
"""

nFrom = 1;
nTo = int(input("Enter Number (number > 1) : "));

while(nFrom <= nTo):
    print(nFrom, end=" ");
    nFrom += 1;

