from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.rooms = rooms
        self.visited = set()
        self.visit(0)
        return self.visited == set(list(range(0, len(self.rooms))))

    def visit(self, room):
        if room in self.visited:
            return
        self.visited.add(room)
        for r in self.rooms[room]:
            self.visit(r)


print(Solution().canVisitAllRooms([[1], [2], [3], []]))
print(Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
