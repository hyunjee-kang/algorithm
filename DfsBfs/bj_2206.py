'''
문제: 백준 2206 벽부수고 이동하기
유형: bfs
노트: -
'''

from collections import deque
import math

def isOutOfIndex(x, y):
    if x < 0 or m < x or y < 0 or n < y: return True
    return False

def bfs(visit):
    dq = deque()
    dq.append((0, 0, 0))
    visit[0][0][0] = 1
    
    while len(dq) > 0:
        x, y, wall = dq.popleft()
        if x == m and y == n: break
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if isOutOfIndex(nx, ny): continue # index out of boud
            if board[ny][nx] and wall: continue # already break the wall
            if visit[ny][nx][wall]: continue # already visited
            
            if board[ny][nx] == 1:  
                visit[ny][nx][1] = visit[y][x][wall] + 1
                dq.append((nx, ny, 1))
            else:
                visit[ny][nx][wall] = visit[y][x][wall] + 1
                dq.append((nx, ny, wall))
    
    if visit[n][m][0] and visit[n][m][1]:
        return min(visit[n][m][0], visit[n][m][1])
    else:
        return max(visit[n][m][0], visit[n][m][1])


'''main'''
# input
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input())))

# solution
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visit = [[[0, 0] for _ in range(m)] for _ in range(n)]
n -= 1
m -= 1
    
ans = bfs(visit)
if ans == 0: print(-1)
else: print(ans)


'''
8 8
01000100
01010100
01010100
01010100
01010100
01010100
01010100
00010100
'''