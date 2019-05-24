from typing import List
from functools import lru_cache

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.days = days
        self.costs = costs
        return self.minDay(0)

    @lru_cache(None)
    def minDay(self, day) -> int:
        if day > self.days[-1]:
            return 0

        if not day in set(self.days):
            return self.minDay(day + 1)

        costs = [
            self.minDay(day + 1) + self.costs[0],
            self.minDay(day + 7) + self.costs[1],
            self.minDay(day + 30) + self.costs[2]
        ]

        return min(costs)

print(Solution().mincostTickets([1,4,6,7,8,20], [2, 7, 15]))

