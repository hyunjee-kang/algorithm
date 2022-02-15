'''
문제: 백준 11779 최소비용 구하기2
유형: dijkstra
노트: -
'''
import math
import heapq
from sys import stdin
input = stdin.readline

def dijkstra(start, end, bus):
    cost = [math.inf for _ in range(n + 1)]
    hq = []
    
    cost[start] = 0 
    heapq.heappush(hq, (cost[start], start, [start]))
    while len(hq) > 0:
        c, v, path = heapq.heappop(hq)
        if v == end: 
            print(cost[v])
            print(len(path))
            print(' '.join(map(str, path)))
            break
        if cost[v] < c: continue
        for nxt_v, nxt_c in bus[v].items():
            if cost[nxt_v] > cost[v] + nxt_c:
                cost[nxt_v] = cost[v] + nxt_c
                nxt_path = path[:]
                nxt_path.append(nxt_v)
                heapq.heappush(hq, (cost[nxt_v], nxt_v, nxt_path))
                
    return

'''main'''
n = int(input())
m = int(input())
bus = {i : {} for i in range(n + 1)}
for _ in range(m):
    u, v, d = map(int, input().split())
    if v in bus[u]: bus[u][v] = min(bus[u][v], d)
    else: bus[u][v] = d
    
start, end = map(int, input().split())
dijkstra(start, end, bus)
    
