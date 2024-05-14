"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
  
"""

nums = [1, 2, 3, 1, 2, 3]


def remove_duplicates_II(nums,k):
    dictt = {}
    for i in range(len(nums)):
        # print(dictt)
        if nums[i] in dictt and abs(i - dictt[nums[i]]) <= k:
            return True
        else:
            dictt[nums[i]] = i
    return False

res = remove_duplicates_II(nums,2)
print(res)