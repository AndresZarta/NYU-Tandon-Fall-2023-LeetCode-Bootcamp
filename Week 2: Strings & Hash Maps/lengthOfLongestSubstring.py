class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left_pointer = 0
        max_length = 0

        for num in range (len(s)):
            while s[num] in charSet:
                charSet.remove(s[left_pointer])
                left_pointer += 1
            charSet.add(s[num])
            length = num - left_pointer + 1
            max_length = max(max_length, length)
        return max_length  
            
