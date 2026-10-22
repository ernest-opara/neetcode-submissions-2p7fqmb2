class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        currSet = []
        visit = set()
        res = []

        def helper(i):
            if i == len(nums):
                tupe = tuple(currSet)
                if tupe not in visit:
                    res.append(list(currSet))
                    visit.add(tupe)
                return

            currSet.append(nums[i])
            helper(i + 1)
            currSet.pop()
            helper(i + 1)

        helper(0)
        return res