class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        streak = longest = 0

        for num in numSet:
            if num - 1 not in numSet:
                streak = 1

                while num + 1 in numSet:
                    streak += 1
                    num += 1

                longest = max(longest, streak)
        return longest