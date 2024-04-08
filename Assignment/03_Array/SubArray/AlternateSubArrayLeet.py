"""
100266. Count Alternating Subarrays
User Accepted:5496
User Tried:6448
Total Accepted:5589
Total Submissions:8821
Difficulty:Medium
You are given a binary array nums.

We call a subarray alternating if no two adjacent elements in the subarray have the same value.

Return the number of alternating subarrays in nums.

 

Example 1:

Input: nums = [0,1,1,1]

Output: 5

Explanation:

The following subarrays are alternating: [0], [1], [1], [1], and [0,1].

Example 2:

Input: nums = [1,0,1,0]

Output: 10

Explanation:

Every subarray of the array is alternating. There are 10 possible subarrays that we can choose.

 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""
def count_alternating_subarrays(nums):
    n = len(nums)
    count = 1  # Initialize count to 1 since a single element is also an alternating subarray
    result = 1  # Initialize result to 1 to account for single-element subarrays

    for i in range(1, n):
        if nums[i] != nums[i - 1]:
            count += 1
        else:
            count = 1
        result += count

    return result


# Example usage:
nums1 = [0, 1, 1, 1]
nums2 = [1, 0, 1, 0]

print(count_alternating_subarrays(nums1))  # Output: 5
print(count_alternating_subarrays(nums2))  # Output: 10
