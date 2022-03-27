'''
문제: 백준 1800 인터넷 설치
유형: 이분탐색
노트: 이분탐색 + 다익스트라 
      여기서 다익스트라는 1과 n이 연결되어 있는지 판단용
'''
import heapq
import math
from sys import stdin
input = stdin.readline

def dijkstra(start, limit):
    # distance: limit보다 큰 연결 개수를 저장
    distance = [math.inf for _ in range(n + 1)]
    distance[start] = 0
    hq = []
    heapq.heappush(hq, (start, distance[start]))
    
    while len(hq) > 0:
        cur, cur_d = heapq.heappop(hq)
        if distance[cur] < cur_d: continue
        for nxt, nxt_d in conn[cur].items():
            if nxt_d > limit:
                if distance[nxt] <= cur_d + 1: continue
                distance[nxt] = cur_d + 1
            else:
                if distance[nxt] <= cur_d: continue
                distance[nxt] = cur_d
            heapq.heappush(hq, (nxt, distance[nxt]))

    if distance[n] > k: return False
    else: return True
    
    
'''main'''
n, p, k = map(int, input().split())
conn = [dict() for _ in range(n + 1)]
for _ in range(p):
    a, b, c = map(int, input().split())
    conn[a][b] = c
    conn[b][a] = c

left = 0
right = 1000000
ans = -1
while left <= right:
    mid = (left + right) // 2
    if dijkstra(1, mid):
        right = mid - 1
        ans = mid
    else:
        left = mid + 1

print(ans)
