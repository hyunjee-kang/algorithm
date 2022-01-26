'''
문제: 백준 11657 타임머신
유형: bellman-ford
노트: N-1 반복 후 음의 순환 확인
'''

import math

def updateRoute(distance):
    for i in range(1, N):
        for key, values in city.items():
            for v in values:
                distance[v[0]] = min(distance[v[0]], distance[key] + v[1])
                
def checkMinusCycle():
    for key, values in city.items():
            for v in values:
                if distance[v[0]] > distance[key] + v[1]:
                    return True
    return False
    

'''main'''
N, M = map(int, input().split())
distance = [math.inf for _ in range(N + 1)]
city = {i : [] for i in range(1, N + 1)}
for _ in range(M):
    start, end, weight = map(int, input().split())
    city[start].append((end, weight))

distance[1] = 0
updateRoute(distance)
if checkMinusCycle(): print(-1)
else:
    for i in range(2, N + 1):
        if distance[i] == math.inf: print(-1)
        else: print(distance[i])

