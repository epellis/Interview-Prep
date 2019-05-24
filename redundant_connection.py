from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ut = UpTree(len(edges))

        bad_edges = []

        for edge in edges:
            u, v = (v-1 for v in edge)
            # print(f"(u, v): ({u}, {v})")

            up = ut.get_parent(u)
            vp = ut.get_parent(v)
            # print(f"(up, vp): ({up}, {vp})")

            if up == vp:
                bad_edges.append(edge)

            ut.merge(up, vp)


        # print(f"Bad Edges: {bad_edges}")
        return bad_edges[-1]

class UpTree:
    def __init__(self, n):
        self.elements = [-1] * n

    def get_parent(self, i):
        # print(i, self.elements)
        if self.elements[i] != -1:
            parent = self.get_parent(self.elements[i])
            self.elements[i] = parent
            return parent
        # print(f"Returing {i}")
        return i

    def merge(self, i, j):
        # print(f"(i, j): ({i}, {j})")
        if i != j:
            self.elements[j] = i



print(Solution().findRedundantConnection([[1,2], [1,3], [2,3]]))
print(Solution().findRedundantConnection([[1,4],[3,4],[1,3],[1,2],[4,5]]))
print(Solution().findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))
