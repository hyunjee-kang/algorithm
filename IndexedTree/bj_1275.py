'''
문제: 백준 1275 커피숍2
유형: 자료구조, 세그먼트 트리, 인덱스 트리
노트: getSumByRange() 의 조건 주의
'''

def update(idx, val):
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
    # get base value
    global N, B
    while (B <= N): B *= 2

    # set input values
    tree = [0 for _ in range(B)]
    for i in range(N):
        tree.append(numbers[i])
    for i in range(B - N):
        tree.append(0)
    
    # sum leaf nodes
    for i in range(B - 1, 0, -1):
        tree[i] = tree[i * 2] + tree[i * 2 + 1]
    
    return tree
    
    
    
'''main'''
N, Q = map(int, input().split())
numbers = list(map(int, input().split()))
B = 1
tree = initNode()

for _ in range(Q, 0, -1):
    x, y, a, b = map(int, input().split())
    if x > y: x, y = y, x
    print(getSumByRange(x + B - 1, y + B - 1))
    update(a + B - 1, b)
    