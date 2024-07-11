"""
3210. Find the Encrypted String
Easy
https://leetcode.com/contest/weekly-contest-405/problems/find-the-encrypted-string/description/

"""


def encryptedString(s, k):
    n = len(s)
    newEncryptedString = ""
    print("i , newPos = (i+k)%n ,  s[newPos] , newEncryptedString")
    for i in range(n):
        newPosition = (i + k) % n
        newEncryptedString += s[newPosition]
        print(
            f"{i} ,              {(i+k)%n} ,         {s[newPosition]} ,     {newEncryptedString}"
        )
    print(f"new Encryped String = {newEncryptedString}\n")
    return newEncryptedString


encryptedString("dart", 3)  # tdar
encryptedString("rishabh", 2) #shabhri
