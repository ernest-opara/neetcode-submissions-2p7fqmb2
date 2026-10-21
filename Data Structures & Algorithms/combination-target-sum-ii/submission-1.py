class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def helper(idx, currSet, total):
            if total == target:
                res.append(currSet[:])
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if total + candidates[i] > target:
                    break

                currSet.append(candidates[i])
                helper(i + 1, currSet, total + candidates[i])
                currSet.pop()
        
        helper(0, [], 0)
        return res