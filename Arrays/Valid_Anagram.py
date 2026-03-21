# Problem: Valid Anagram
# Time complexity: O(n)
# Space Complexity: O(n)
# Pattern: Hash Map

class Solution:
    def isAnagram(self, s, t):
        map_s = {}
        map_t = {}

        if len(s) != len(t):
            return False
        
        for char in s:
            map_s[char] = map_s.get(char, 0) + 1
        for char in t:
            map_t[char] = map_t.get(char, 0) + 1

        if map_s == map_t:
            return True
        else:
            return False
