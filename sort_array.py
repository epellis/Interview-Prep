from typing import List
import heapq


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        s = []
        while nums:
            s.append(heapq.heappop(nums))
        return s


print(Solution().sortArray([5, 2, 3, 1]))
print(Solution().sortArray([5, 1, 1, 2, 0, 0]))
