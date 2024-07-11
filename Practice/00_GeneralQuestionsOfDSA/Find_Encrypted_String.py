"""
3210. Find the Encrypted String
Easy
https://leetcode.com/contest/weekly-contest-405/problems/find-the-encrypted-string/description/

"""


def encryptedString(s, k):
    n = len(s)
    newEncryptedString = ""
    for i in range(n):
        newPosition = (i + k) % n
        newEncryptedString += s[newPosition]
    return newEncryptedString


res1 = encryptedString("dart", 3)  # tdar
print(res1)
res2 = encryptedString("rishabh", 2)  # shabhri
print(res2)

