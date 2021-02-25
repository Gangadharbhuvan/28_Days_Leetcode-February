'''
    Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

 

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0
 

Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105
 

Follow up: Can you solve it in O(n) time complexity?


'''

class Solution:
    def findUnsortedSubarray(self, nums):
        nums = [-float("inf")] + nums + [float("inf")]
        run_max = list(accumulate(nums, max))
        run_min = list(accumulate(nums[::-1], min))[::-1]
        
        end, beg = len(nums) - 1, 0

        while nums[end-1] <= nums[end] and run_max[end-1] <= nums[end - 1]:
            end -= 1
            
        if end == 0: return 0
            
        while nums[beg+1] >= nums[beg] and run_min[beg+1] >= nums[beg + 1]:
            beg += 1
            
        return end - beg - 1