class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visit = set()

        def helper(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for i in range(len(nums)):
                if i not in visit:
                    visit.add(i)
                    helper(curr + [nums[i]])
                    visit.remove(i)
        
        helper([])
        return res
        