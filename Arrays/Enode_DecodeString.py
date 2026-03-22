# problem : Enocde - Decode a string
# Time Complexity: 
# Space Complexity: 

class Solution:
    def encoding(self, strs):
        pass
    def decoding(self, str):
        pass




nums = [1,2,3,4,5]
n = len(nums)
prefix = [1] * n
suffix = [1] * n

for i in range(n):
    if i == 0:
        prefix[i] = nums[i]
    else:
        prefix[i] = prefix[i-1] * nums[i]


for i in range(n-1, -1, -1):
    if i == n-1:
        suffix[i] = nums[i]
    else:
        suffix[i] = suffix[i+1] * nums[i]

print(prefix)
print(suffix)

