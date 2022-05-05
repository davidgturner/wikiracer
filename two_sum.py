from typing import List

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

====================
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

====================
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

def twoSum(nums: List[int], target: int) -> List[int]:
    final = set()
    # tuple_res = ()
    # set1 = set()
    # for n in nums:
    #     set1.add(n)
    return_list = list()
    for i, s in enumerate(nums):
        element = nums.pop()
        print("s ", s)
        if (target - element) in nums: # and i != nums.index(target - s):
            return_list.append(nums.index(target - s))
            return_list.append(nums.index(s, nums.index(target - s)))

        if len(return_list) == 2:
            break

    return return_list # list(final)


# print(twoSum([2, 7, 11, 15], 9))

# print(twoSum([3, 2, 4], 6))

print(twoSum([3, 3], 6))