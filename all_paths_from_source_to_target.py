from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.outgoing = graph
        self.paths = []
        self.discover_path(0, [])
        return self.paths

    def discover_path(self, idx, prevpath):
        if idx == len(self.outgoing) - 1:
            self.paths.append(prevpath + [idx])
        for o in self.outgoing[idx]:
            self.discover_path(o, prevpath + [idx])


print(Solution().allPathsSourceTarget([[1, 2], [3], [3], []]))
print(Solution().allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]))
