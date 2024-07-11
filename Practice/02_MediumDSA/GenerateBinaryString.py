""" 
3211. Generate Binary Strings Without Adjacent Zeros
Medium
https://leetcode.com/contest/weekly-contest-405/problems/generate-binary-strings-without-adjacent-zeros/description/
"""


def generateValidBinaryStrings(n):
    queue = ["0", "1"]
    if n == 1:
        return queue
    for _ in range(1, n):
        newQueue = []
        for s in queue:
            if s[-1] == "0":
                newQueue.append(s + "1")
            else:
                newQueue.append(s + "0")
                newQueue.append(s + "1")
        queue = newQueue
    return queue


res1 = generateValidBinaryStrings(3)
print(res1)
res2 = generateValidBinaryStrings(1)
print(res2)
res3 = generateValidBinaryStrings(2)
print(res3)
