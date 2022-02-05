'''
문제: 백준 11437 LCA
유형: Lowest Common Ancestor
노트: 노드가 많을 땐 bfs로 풀자!
'''

from collections import deque
from sys import stdin
input = stdin.readline
max_depth = 20

def bfs():
    depth[1] = 1
    dq = deque()
    dq.append(1)
    while len(dq) > 0:
        cur = dq.popleft()
        for i in tree[cur]:
            if depth[i] != 0: continue
            dq.append(i)
            depth[i] = depth[cur] + 1
            ancestor[0][i] = cur

def setAncestor():
    for i in range(1, max_depth + 1):
        for j in range(1, n + 1):
            ancestor[i][j] = ancestor[i - 1][ancestor[i - 1][j]]

def lca(a, b):
    if depth[a] < depth[b]: a, b = b, a
    
    for i in range(max_depth, -1, -1):
        if depth[a] - depth[b] >= (1 << i):
            a = ancestor[i][a]
            
    if a == b: return a
    
    for i in range(max_depth, -1, -1):
        if ancestor[i][a] != ancestor[i][b]:
            a = ancestor[i][a]
            b = ancestor[i][b]
            
    return ancestor[0][a]

'''main'''
n = int(input())
tree = {i: [] for i in range(n + 1)}
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

depth = [0 for _ in range(n + 1)]
ancestor = [[0 for _ in range(n + 1)] for _ in range(max_depth + 1)]
bfs()
setAncestor()

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))

