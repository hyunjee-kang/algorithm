'''
문제: 백준 2517 달리기
유형: 자료구조, 세그먼트 트리, 인덱스 트리
노트: -
'''

def setMaxRank(origin_rank, loser):
    global rank
    rank.append(origin_rank - loser)

def update(idx, val):
    global tree
    diff = val - tree[idx]
    while idx > 0:
        tree[idx] += diff
        idx //= 2

def getSumByRange(start, end):
    sum = 0
    while start <= end:
        if start % 2 == 1: sum += tree[start]
        if end % 2 == 0: sum += tree[end]
        start = (start + 1) // 2
        end = (end - 1) // 2
    
    return sum

def initNode():
    base = 1
    while (base < N): base *= 2
    tree = [0 for _ in range(base + N)]
    
    return base, tree


'''main'''
runner = []
rank = []
N = int(input())
for i in range(N):
    runner.append(int(input()))
    
sorted_runner = {k: i for i, k in enumerate(sorted(set(runner)))}
base, tree = initNode()
for i, val in enumerate(runner):
    tree_idx = base + sorted_runner[val]
    loser = getSumByRange(base, tree_idx)
    setMaxRank(i + 1, loser)
    update(tree_idx, 1)
    
for i in rank:
    print(i)
