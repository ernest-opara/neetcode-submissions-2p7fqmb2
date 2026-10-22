class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque([(amount, 0)])
        seen = set()

        while q:
            remAmount, numCoins = q.popleft()

            if remAmount == 0:
                return numCoins

            for coin in coins:
                subAmount = remAmount - coin

                while subAmount >= 0 and subAmount not in seen:
                    q.append((subAmount, numCoins + 1))
                    seen.add(subAmount)

        return -1