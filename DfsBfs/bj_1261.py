'''
문제: 백준 1261 알고스팟
유형: 0-1 bfs
노트: deque를 사용, 앞/뒤 넣는 방법 주의
'''

from collections import deque

def bfs(x, y, sum):
    dq = deque()
    dq.append((x, y, sum))
    
    while len(dq) != 0:
        vertex = dq.popleft()
        if (vertex[0] == M - 1) and (vertex[1] == N - 1): return vertex[2]
        for i in range(4):
            vx = dx[i] + vertex[0]
            vy = dy[i] + vertex[1]
            
            if vx < 0 or vx >= M or vy < 0 or vy >= N: continue
            
            if visit[vy][vx] == 1: continue
            else: visit[vy][vx] = 1

            if maze[vy][vx] == 1: dq.append((vx, vy, vertex[2] + 1))
            else: dq.appendleft((vx, vy, vertex[2]))

    return


'''main'''
M, N = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visit = [[0 for _ in range(M)] for _ in range(N)]

visit[0][0] = 1
print(bfs(0, 0, 0))