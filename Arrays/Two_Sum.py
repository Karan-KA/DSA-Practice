# problem: Two Sum
# Time Complexity : O(n)
# Space Complexity: O(n)
# Pattern: hashmap

class Solution:
    def twoSum(nums, target):

        target_map = {}

        for num_idx in range(len(nums)):
            complement = target - nums[num_idx]

            if complement in target_map.keys():
                return complement[nums[num_idx]], num_idx 
            complement[nums[num_idx]] = num_idx