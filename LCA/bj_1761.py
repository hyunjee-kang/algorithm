'''
문제: 백준 1761 정점들의 거리
유형: Lowest Common Ancestor
노트: -
'''
from collections import deque
from sys import stdin
input = stdin.readline

def bfs():
    dq = deque()
    dq.append(1)
    depth[1] = 1
    
    while len(dq) > 0:
        node = dq.popleft()
        for i in tree[node].keys():
            if depth[i] != 0: continue
            dq.append(i)
            dp[0][i] = node
            depth[i] = depth[node] + 1
            distance[i] = distance[node] + tree[node][i]
        

def setDp():
    for i in range(1, max_depth + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][dp[i - 1][j]]


def lca(a, b):
    if depth[a] < depth[b]: a, b = b, a
    
    for i in range(max_depth, -1 , -1):
        if depth[a] - depth[b] >= (1 << i):
            a = dp[i][a]
    
    if a == b: return a
    
    for i in range(max_depth, -1, -1):
        if dp[i][a] != dp[i][b]:
            a = dp[i][a]
            b = dp[i][b]
            
    return dp[0][a]


'''main'''
n = int(input())
tree = {i : {} for i in range(1, n + 1)}
for _ in range(n - 1):
    a, b, dist = map(int, input().split())
    tree[a][b] = dist
    tree[b][a] = dist

max_depth = 20
depth = [0 for _ in range(n + 1)]
dp = [[0 for _ in range(n + 1)] for _ in range(max_depth + 1)]
distance = [0 for _ in range(n + 1)]
   
bfs()
setDp()

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(distance[a] + distance[b] - 2 * distance[lca(a, b)])
