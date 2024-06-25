""" 
#brutforce approche
Given a string s, find the length of the longest 
substring
 without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def duplicate(char,st):
    for i in range(len(st)):
        if st[i] == char:
            return True;
        
    return False

count = 1;
dictt = {};

# s = "abcabcbb"
s = "pwwkew"
# s = "bbbbb"
for i in range(len(s)):
    # print(dictt)
    if dictt != {}:
        # print(s[i],dictt[count])
        if duplicate(s[i],dictt[count]):
            count += 1

    if count in dictt:
        dictt[count] += s[i];
    else:
        dictt[count] = s[i];


print(dictt)

length = 0
ans = ""
for val in dictt.values():
    length = max(length,len(val));
    if length <= len(val):
        ans = val

print(ans)
