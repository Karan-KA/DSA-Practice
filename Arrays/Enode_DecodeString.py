# problem : Enocde - Decode a string
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def encoding(self, strs):
        encodedstr = ""
        for word in strs:
            encodedstr += str(len(word))+'#'+word

        return encodedstr
    def decoding(self, s):
        ans, i = [], 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])

            ans.append(s[j+1:j+1+length])

            i = j+1+length
        
        return ans





