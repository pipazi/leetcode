class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        lookup = {}
        start_location = -1
        for index, char in enumerate(s):
            if char in lookup and lookup[char] > start_location:
                start_location = lookup[char]
                lookup[char] = index
            else:
                lookup[char] = index
                if index - start_location > l:
                    l = index - start_location
        return l
