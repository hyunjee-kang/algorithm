'''
문제: 백준 16118 달빛 여우
유형: dijkstra
노트: -
'''

import math
import heapq
from sys import stdin
input = stdin.readline

def fox():
    distance = [math.inf for _ in range(n + 1)]
    distance[1] = 0
    hq = []
    heapq.heappush(hq, (distance[1], 1))
    
    while len(hq) > 0:
        d, cur = heapq.heappop(hq)
        if distance[cur] < d: continue
        for post, cost in road[cur].items():
            if distance[post] > distance[cur] + cost:
                distance[post] = distance[cur] + cost 
                heapq.heappush(hq, (distance[post], post))
        
    return distance

def wolf():
    fast = [math.inf for _ in range(n + 1)]
    slow = [math.inf for _ in range(n + 1)]
    slow[1] = 0
    hq = []
    heapq.heappush(hq, (slow[1], 1, False))
    
    while len(hq) > 0:
        d, cur, is_fast = heapq.heappop(hq)
        for post, cost in road[cur].items():
            if is_fast: # 이전에 빠르게 달렸음
                new_cost = d + (cost * 2)
                if slow[post] > new_cost:
                    slow[post] = new_cost
                    heapq.heappush(hq, (new_cost, post, not is_fast))
            else: # 이전에 천천히 왔음
                new_cost = d + (cost // 2)
                if fast[post] > new_cost:
                    fast[post] = new_cost
                    heapq.heappush(hq, (new_cost, post, not is_fast))      
    
    distance = [math.inf]
    for i in range(1, n + 1):
        distance.append(min(fast[i], slow[i]))
        
    return distance

'''main'''
n, m = map(int, input().split())
road = [{} for _ in range(n + 1)]
for _ in range(m):
    a, b, d = map(int, input().split())
    if b in road[a]: 
        road[a][b] = min(road[a][b], d * 2)
        road[b][a] = road[a][b]
    else: 
        road[a][b] = d * 2
        road[b][a] = d * 2

fox_cost = fox()
wolf_cost = wolf()
# print(fox_cost)
# print(wolf_cost)
answer = 0
for i in range(1, n + 1):
    if fox_cost[i] < wolf_cost[i]: answer += 1
print(answer)
