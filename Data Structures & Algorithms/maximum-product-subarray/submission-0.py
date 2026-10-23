class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = mini = nums[0]
        res = maxi

        for i in range(1, len(nums)):
            curr = nums[i]
            temp = max(curr, curr * mini, curr * maxi)
            mini = min(curr, curr * mini, curr * maxi)

            maxi = temp

            res = max(res, maxi)
        return res

