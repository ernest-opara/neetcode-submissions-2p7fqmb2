class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen, resIndex = 0, 0

        def helper(l, r):
            nonlocal resLen, resIndex

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIndex = l
                    resLen = r - l + 1
            
                l -= 1
                r += 1

        for i in range(len(s)):
            helper(i,i)
            helper(i,i+1)
        return s[resIndex:resIndex + resLen]