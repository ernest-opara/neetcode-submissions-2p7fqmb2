class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        currSet = []
        res = []
        total = 0

        def helper(i, currSet, total):
            if total == target:
                res.append(currSet.copy())
                return

            if i >= len(nums) or total > target:
                return

            currSet.append(nums[i])
            helper(i, currSet, total + nums[i])
            currSet.pop()
            helper(i+1, currSet, total)

        helper(0, currSet, total)
        return res