'''
문제: 백준 13460 구슬 탈출 2
유형: bfs
노트: -
'''

from collections import deque
import math
        
def move(moveY, moveX, pos):
    y = pos[0]
    x = pos[1]
    while True:
        y += moveY
        x += moveX
        if board[y][x] == '#': return [y - moveY, x - moveX]
        if board[y][x] == 'O': return -1

def relocation(r, b, r_next, b_next, y, x):
    if r_next == b_next:
        if y == -1:
            if r[0] < b[0]: b_next[0] += 1
            else: r_next[0] += 1
        elif y == 1:
            if r[0] < b[0]: r_next[0] -= 1
            else: b_next[0] -= 1
        elif x == -1:
            if r[1] < b[1]: b_next[1] += 1
            else: r_next[1] += 1
        elif x == 1:
            if r[1] < b[1]: r_next[1] -= 1
            else: b_next[1] -= 1
        
    return r_next, b_next
    
def bfs():
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    dq = deque()
    dq.append([red, blue, 1])
    min_step = math.inf
    
    while len(dq) > 0:
        r, b, step = dq.popleft()
        if step > 10: break
        for i in range(4):
            r_next = move(dy[i], dx[i], r)
            b_next = move(dy[i], dx[i], b)
            if b_next == -1: continue
            if r_next == -1: 
                min_step = min(min_step, step)
                continue
            if r == r_next and b == b_next: continue
            r_next, b_next = relocation(r, b, r_next, b_next, dy[i], dx[i])
            if r != r_next or b != b_next: 
                dq.append([r_next, b_next, step + 1])
    
    if min_step != math.inf: return min_step
    else: return -1

'''main'''
# input
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(input()))

blue = [0, 0]
red = [0, 0]
for i in range(n):
    for j in range(m):
        if board[i][j] == 'B': blue = [i, j]
        elif board[i][j] == 'R': red = [i, j]

# solution
print(bfs())
