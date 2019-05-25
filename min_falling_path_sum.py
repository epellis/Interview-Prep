from typing import List


class Solution:
    def minFallingPathSum(self, a: List[List[int]]) -> int:
        prev, *rest = a
        while rest:
            curr, *rest = rest

            for i, c in enumerate(curr):
                candidates = []
                if i - 1 >= 0:
                    candidates.append(prev[i - 1] + c)
                if i + 1 < len(curr):
                    candidates.append(prev[i + 1] + c)
                candidates.append(prev[i] + c)
                curr[i] = min(candidates)

            prev = curr

        return min(prev)


print(Solution().minFallingPathSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
