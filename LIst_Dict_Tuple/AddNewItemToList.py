"""
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

Expected output:

[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
"""

aList = [10,20,[300,400,[5000,6000],500],30,40];
aList[2][2].append(7000)
print(aList)