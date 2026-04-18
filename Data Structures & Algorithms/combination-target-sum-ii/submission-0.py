class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def helper(idx, path, curr):
            if curr == target:
                res.append(path.copy())
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if curr + candidates[i] > target:
                    break

                path.append(candidates[i])
                helper(i + 1, path, curr + candidates[i])
                path.pop()

        helper(0, [], 0)
        return res