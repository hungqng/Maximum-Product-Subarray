# 152. Maximum Product Subarray

# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# A subarray is a contiguous subsequence of the array.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 1:
            return 0
        dp_max = [0] * N
        dp_min = [0] * N
        
        dp_max[0] = dp_min[0] = nums[0]
        
        for i in range(1, N):
            if nums[i] > 0:
                dp_max[i] = max(dp_max[i-1] * nums[i], nums[i])
                dp_min[i] = min(dp_min[i-1] * nums[i], nums[i])
            else:
                dp_max[i] = max(dp_min[i-1] * nums[i], nums[i])
                dp_min[i] = min(dp_max[i-1] * nums[i], nums[i])
        return max(dp_max)