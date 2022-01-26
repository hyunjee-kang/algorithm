'''
문제: 백준 5719 거의 최단 경로
유형: dijkstra
노트: 최단 경로를 제거하는 로직 주의
'''

import heapq
from collections import deque
import math
from sys import stdin
input = stdin.readline

def dijkstra(N, S, road):
    distance = [math.inf for _ in range(N)]
    distance[S] = 0
    hq = []    
    heapq.heappush(hq, (distance[S], S))
    
    while len(hq) > 0:
        d, now = heapq.heappop(hq)
        if distance[now] < d: continue
        for i in road[now]:
            new_d = d + road[now][i]
            if distance[i] > new_d:
                distance[i] = new_d
                heapq.heappush(hq, (new_d, i))

    return distance

def bfs(S, D, r_road, distance):
    del_road = []
    q = deque()
    q.append(D)
    while q:
        v = q.popleft()
        if v == S: continue 
        for i in r_road[v]:
            if distance[i] + road[i][v] == distance[v]:
                if (i, v) not in del_road:
                    del_road.append((i, v))
                    q.append(i)
                    
    return del_road


def removeRoad(del_road, road):
    for i in del_road:
        del road[i[0]][i[1]]


'''main'''
while True:
    # input
    N, M = map(int, input().split())
    if N == 0 and M == 0: break
    S, D = map(int, input().split())
    road = [dict() for _ in range(N)]
    r_road = [dict() for _ in range(N)]
    for _ in range(M):
        U, V, P = map(int, input().split())
        road[U][V] = P
        r_road[V][U] = P

    # solution
    shortest = dijkstra(N, S, road)
    if shortest[D] == math.inf: 
        print(-1)
        continue
    
    del_road = bfs(S, D, r_road, shortest)
    removeRoad(del_road, road)
    
    almost = dijkstra(N, S, road)
    if almost[D] == math.inf: print(-1)
    else: print(almost[D])
 