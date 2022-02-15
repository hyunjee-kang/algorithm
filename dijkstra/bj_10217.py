'''
문제: 백준 10217 kcm travel
유형: dijkstra
노트: dp가 사용된 다익스트라 
     (근데 python은 dp로 풀어야 메모리 초과 안남;;)
'''
import math
import heapq
from sys import stdin
input = stdin.readline

def dijkstra(n, m, airline):
    dp = [[math.inf for _ in range(10001)] for _ in range(n + 1)]
    hq = []
    
    dp[1][0] = 0
    heapq.heappush(hq, (dp[1][0], 1, 0))
    while len(hq) > 0:
        d, cur, c = heapq.heappop(hq)
        if cur == n: return d
        if dp[cur][c] < d: continue
        for nxt, nxt_c, nxt_d in airline[cur]:
            if m >= c + nxt_c and dp[nxt][c + nxt_c] > d + nxt_d:
                dp[nxt][c + nxt_c] = d + nxt_d
                heapq.heappush(hq, (dp[nxt][c + nxt_c], nxt, c + nxt_c))

    return math.inf

def dynamic(n, m, airline):
    dp = [[math.inf for _ in range(m + 1)] for _ in range(n + 1)]
    dp[1][0] = 0
    
    for c in range(m + 1):
        for cur in range(1, n + 1):
            if dp[cur][c] == math.inf: continue
            for nxt, nxt_c, nxt_d in airline[cur]:
                if m < c + nxt_c: continue
                dp[nxt][c + nxt_c] = min(dp[nxt][c + nxt_c], dp[cur][c] + nxt_d)
    
    return min(dp[n])

'''main'''
t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    airline = {i : [] for i in range(1, n + 1)}
    for _ in range(k):
        u, v, c, d = map(int, input().split())
        airline[u].append((v, c, d))
    
    # distance = dijkstra(n, m, airline)
    distance = dynamic(n, m, airline)
    if distance == math.inf: print('Poor KCM')
    else: print(distance)