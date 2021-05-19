# 841. Keys and Rooms
from collections import deque


def canVisitAllRooms(rooms):
    if not rooms:
        return False
    q = deque()
    q.append(0)
    visited = [False, False, False, False]
    visited[0]=True
    print(visited)
    
    while q:
        node = q.popleft()
        for adj in rooms[node]:
            if not visited[adj]:
                visited[adj]=True
                q.append(adj)
    for i in visited:
        if not i:
            return False
    return True


print(canVisitAllRooms([[[1, 3], [3, 0, 1], [2], [0]]]))
