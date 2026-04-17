class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        currSet = []
        res = []

        def helper(i):
            if i == len(nums):
                res.append(currSet[:])
                return

            
            currSet.append(nums[i])
            helper(i + 1)
            currSet.pop()
            helper(i + 1)

        helper(0)
        return res