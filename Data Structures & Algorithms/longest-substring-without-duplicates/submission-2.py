class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <=1:
            return len(s)
        lstChar = {}
        maxLen = 0
        largestSubstring = "" 
        for i in range(len(s)):
            if s[i] not in lstChar or lstChar[s[i]]==0:
                lstChar[s[i]]=1
                largestSubstring+=s[i]
            else:
                while s[i] in largestSubstring: 
                        char = largestSubstring[0]
                        lstChar[char] = 0
                        largestSubstring=largestSubstring[1:]
                largestSubstring+=s[i]
                lstChar[s[i]]=1
            maxLen = max(maxLen,len(largestSubstring))
        return maxLen



        