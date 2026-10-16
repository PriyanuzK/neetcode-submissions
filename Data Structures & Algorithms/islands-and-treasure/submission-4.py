class Solution:
    def islandsAndTreasure(self, rooms: List[List[int]]) -> None:
        ROWS,COLS= len(rooms),len(rooms[0])
        INF=2147483647
        q=deque()
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c]==0:
                    q.append((r,c))
        directions = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        while q:
            r,c=q.popleft()
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc 
                  # 4. Skip out-of-bounds cells and walls
                if (nr < 0 or nr >= ROWS or
                    nc < 0 or nc >= COLS or
                    rooms[nr][nc] == -1):
                   continue           
                if rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[r][c] + 1
                    q.append((nr, nc))



            


