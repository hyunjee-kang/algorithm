'''
문제: 백준 2233 사과나무
유형: Lowest Common Ancestor
노트: -
'''

from collections import deque
from sys import stdin
input = stdin.readline

max_depth = 20

def bfs(depth, dp):
    depth[1] = 1
    dq = deque([1])
    
    while len(dq) > 0:
        cur = dq.popleft()
        for i in tree[cur]:
            if depth[i] != 0: continue
            dq.append(i)
            depth[i] = depth[cur] + 1
            dp[0][i] = cur

def setDp():
    for i in range(1, max_depth + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][dp[i - 1][j]]
 
def lca(x, y):
    if depth[x] > depth[y]: x, y = y, x
    
    for i in range(max_depth, -1, -1):
        if depth[y] - depth[x] >= (1 << i):
            y = dp[i][y]
            
    if x == y: return x
    
    for i in range(max_depth, -1, -1):
        if dp[i][x] != dp[i][y]:
            x = dp[i][x]
            y = dp[i][y]
    
    return dp[0][x]
               

def makeTree(binary, tree, appleIdx):
    idx = deque([i for i in range(1, n + 1)])
    cur = 0
    prev = 0
    parent = [0 for _ in range(n + 1)]
    for i in binary:
        if int(i) == 0:
            prev = cur
            cur = idx.popleft()
            parent[cur] = prev
            tree[prev].append(cur)
            tree[cur].append(prev)
            appleIdx.append(cur)
        else:
            appleIdx.append(cur)
            cur = parent[cur]
            prev = parent[cur]


'''main'''
n = int(input())
binary = list(input().strip())
x, y = map(int, input().split())

tree = {i : [] for i in range(n + 1)}
appleIdx = []
makeTree(binary, tree, appleIdx)

depth = [0 for _ in range(n + 1)]
dp = [[0 for _ in range(n + 1)] for _ in range(max_depth + 1)]
bfs(depth, dp)
setDp()

ancestor = lca(appleIdx[x - 1], appleIdx[y - 1])
for i in range(len(appleIdx)):
    if appleIdx[i] == ancestor:
        print(i + 1, end = ' ')
    