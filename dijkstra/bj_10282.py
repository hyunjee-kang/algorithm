'''
문제: 백준 10282 해킹
유형: 다익스트라
노트: 다익스트라 함수에서 for문 전 if문 주의
'''

import heapq
import math
import sys

def dijkstra(cost, computer, start):
    heap = []
    heapq.heappush(heap, (cost[start], start))
    
    while len(heap) != 0:
        val = heapq.heappop(heap)
        if cost[val[1]] < val[0]: continue
        for i in computer[val[1]]:
            if cost[i[0]] > i[1] + cost[val[1]]:
                cost[i[0]] = i[1] + cost[val[1]]
                heapq.heappush(heap, (cost[i[0]], i[0]))


'''main'''
input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    n, d, c = map(int, input().split()) 
    cost = [math.inf for _ in range(n + 1)] 
    computer = {i : [] for i in range(n + 1)}
    for _ in range(d):
        a, b, s = map(int, input().split())
        computer[b].append([a, s])
    
    cost[c] = 0
    dijkstra(cost, computer, c)
    
    maxTime = 0
    cnt = 0
    for i in cost:
        if i < math.inf: 
            cnt += 1
            maxTime = max(maxTime, i)

    print(cnt, maxTime)
