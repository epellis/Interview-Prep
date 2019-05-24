from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        n = nums.pop()
        l = self.subsets(nums)
        l = l + [[n] + sl for sl in l]
        return l

print(Solution().subsets([1]))
print()
print(Solution().subsets([1, 2]))
print()
print(Solution().subsets([1, 2, 3]))
print()
print(Solution().subsets([1, 2, 3, 4, 5, 6, 7]))
