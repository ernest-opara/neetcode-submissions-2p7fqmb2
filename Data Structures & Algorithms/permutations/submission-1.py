class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visit = set()

        def helper(currSet):
            if len(currSet) == len(nums):
                res.append(currSet[:])
                return

            for i in range(len(nums)):
                if i not in visit:
                    currSet.append(nums[i])
                    visit.add(i)
                    helper(currSet)
                    currSet.pop()
                    visit.remove(i)
                    
        helper([])
        return res