'''
문제: 백준 1981 배열에서 이동
유형:이분 탐색
노트: -
'''
from collections import deque
from sys import stdin
input = stdin.readline

def bfs(left, right):
    visit = [[0 for _ in range(n)] for _ in range(n)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    dq = deque()
    dq.append((0, 0))
    while len(dq) > 0:
        prev_x, prev_y = dq.popleft()
        if prev_x == n - 1 and prev_y == n - 1: return True
        for i in range(4):
            x = prev_x + dx[i]
            y = prev_y + dy[i]
            if 0 > x or x >= n or 0 > y or y >= n: continue
            if visit[y][x] != 0: continue
            if board[y][x] < left or right < board[y][x]: continue
            visit[y][x] = 1
            dq.append((x, y))

    return False    
            
def binarySearch(min_val, max_val):
    l = 0
    r = max_val
    answer = 0
    while l <= r:
        mid = (r + l) // 2
        for i in range(min_val, max_val):
            if board[0][0] < i or i + mid < board[0][0]: continue
            if bfs(i, i + mid):
                r = mid - 1
                answer = mid
                break
        if r >= mid:    
            l = mid + 1

    return answer
                  

'''main'''
n = int(input())
board = []
max_val = 0
min_val = 200
for i in range(n):
    tmp = list(map(int, input().split()))
    max_val = max(max_val, max(tmp))
    min_val = min(min_val, min(tmp))
    board.append(tmp)
    
print(binarySearch(min_val, max_val))
