# Problem: Group Anagrams

# I have implemented this in two ways 
# First implementation uses a time complexity of O(nlogn)
# Second implementation uses a time complexity of just O(n)

# First implementation
# Time Complexity: O(nlogn) logn time for sorting
# Space Complexity: O(n)


from collections import defaultdict
class ImplementationOne:
    def groupAnagrams(self, strs):

        strs_map = defaultdict(list)


        for word in strs:
            strs_map["".join(sorted(word))].append(word)
            
        return list(strs_map.values())
                

# Second implementation
# Time complexity: O(n)
# Space complexity: O(n)

class ImplementationTwo:
    def goupAnagram(self, strs):

        strs_map = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')]+=1

            strs_map[tuple(count)].append(word)

        return list(strs_map.values())
