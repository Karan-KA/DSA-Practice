# Problem: Product of Array Exccept self
# Time complexity: O(n)
# Space Complexit: O(n)

class Solution:
    def productExceptSelf(self, nums):

        ans = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans

