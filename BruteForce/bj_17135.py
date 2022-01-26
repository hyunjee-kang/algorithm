'''
문제: 백준 17135 캐슬 디펜스
유형: brute force, 시뮬레이션
노트: -
'''

from collections import deque
from itertools import combinations
import copy

def attack():
    kill_idx = []
    for i in archer:
        if board[N - 1][i] == 1:
            kill_idx.append((N - 1, i, 0))
            continue
        res = findEnemy((N - 1, i, 2))
        if res != -1:
            kill_idx.append(res)
    
    kill = 0
    while len(kill_idx) > 0:
        idx = kill_idx.pop()
        if board[idx[0]][idx[1]] == 1:
            kill += 1
            board[idx[0]][idx[1]] = 0
    
    return kill

def findEnemy(archer_pos):
    visit = [[0 for _ in range(M)] for _ in range(N)]
    dq = deque()
    dq.append(archer_pos)
    visit[archer_pos[0]][archer_pos[1]] = 1
    while len(dq) > 0:
        pos = dq.popleft()
        y = pos[0]
        x = pos[1]
        dist = pos[2]
        if dist > D: break
        
        if x - 1 >= 0: # left
            if board[y][x - 1] == 1: return (y, x - 1)
            elif visit[y][x - 1] == 0: 
                dq.append((y, x - 1, dist + 1))
                visit[y][x - 1] = 1
        if y - 1 >= 0: # up
            if board[y - 1][x] == 1: return (y - 1, x)
            elif visit[y - 1][x] == 0: 
                dq.append((y - 1, x, dist + 1))
                visit[y - 1][x] = 1
        if x + 1 < M: # right
            if board[y][x + 1] == 1: return (y, x + 1)
            elif visit[y][x + 1] == 0: 
                dq.append((y, x + 1, dist + 1))
                visit[y][x + 1] = 1

    return -1

def move(board):
    new_board = [[0 for _ in range(M)]]
    board.pop()
    for i in board:
        new_board.append(i)
    
    return new_board
    

'''main'''
N, M, D = map(int, input().split())
origin_board = []
for _ in range(N):
    origin_board.append(list(map(int, input().split())))

answer = 0
archer_position = list(combinations([i for i in range(M)], 3))
for archer in archer_position:
    board = copy.deepcopy(origin_board)
    kill = 0
    for _ in range(N):
        kill += attack()
        board = move(board)
    
    answer = max(answer, kill)

print(answer)
