'''
문제: 백준 1865 원홀
유형: bellman-ford
노트: math.inf 사용시 inf 값 갱신이 안됨 주의
'''

inf = 2100000000

def updateDistance(n, world):
    distance = [inf for _ in range(n + 1)]
    for _ in range(1, n):
        for node, roads in world.items():
            for r in roads:
                distance[r[0]] = min(distance[r[0]], distance[node] + r[1])
                
    return distance

def checkMinusCycle(distance, world):
    for node, roads in world.items():
        for r in roads:
            if distance[r[0]] > distance[node] + r[1]:
                return True
    
    return False
    

''' main '''
tc = int(input())
for _ in range(tc):
    # input
    n, m, w = map(int, input().split())
    world = {i : [] for i in range(n + 1)}
    for _ in range(m):
        s, e, t = map(int, input().split())
        world[s].append([e, t])
        world[e].append([s, t])
    for _ in range(w):
        s, e, t = map(int, input().split())
        world[s].append([e, (t * -1)])
        
    # solution    
    distance = updateDistance(n, world)
    if checkMinusCycle(distance, world): print('YES')
    else: print('NO')
