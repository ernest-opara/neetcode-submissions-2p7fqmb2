class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def helper(currSet, i):
            if len(currSet) == len(digits):
                res.append(currSet[:])
                return

            for char in digitToChar[digits[i]]:
                helper(currSet + char, i + 1)
        
        if digits:
            helper("", 0)
        return res