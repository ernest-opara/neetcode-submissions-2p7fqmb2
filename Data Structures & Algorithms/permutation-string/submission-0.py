class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)

        n = len(s1)
        for l in range(len(s2) - n + 1):
            if Counter(s2[l:l+n]) == need:
                return True
        return False