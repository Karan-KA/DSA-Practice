# Problem: Group Anagrams

# I have implemented this in two ways 
# First implementation uses a time complexity of O(nlogn)
# Second implementation uses a time complexity of just O(n)

# First implementation
# Time Complexity: O(nlogn) logn time for sorting
# Space Complexity: O(n)


from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):

        strs_map = defaultdict(list)


        for word in strs:
            strs_map["".join(sorted(word))].append(word)
            
        return list(strs_map.values())
                

s = Solution()
result = s.groupAnagrams(["act","pots","tops","cat","stop","hat"])
print(result)
