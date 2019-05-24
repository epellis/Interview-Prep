from typing import List, Set


class Solution:
    def findCircleNum(self, m: List[List[int]]) -> int:
        people = set(range(len(m)))
        considered = set()

        return count


print(Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(Solution().findCircleNum([[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(Solution().findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
