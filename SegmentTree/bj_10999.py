'''
문제: 백준 10999 구간 합 구하기 2
유형: lazy propagation - segment tree
노트: -
'''
from sys import stdin
input = stdin.readline

def lazyUpdate(start, end, idx):
    if lazy[idx] == 0: return
    
    tree[idx] += lazy[idx] * (end - start + 1)
    
    if start != end:
        lazy[idx * 2] += lazy[idx]
        lazy[idx * 2 + 1] += lazy[idx]
        
    lazy[idx] = 0
    return    
    
def update(left, right, val, idx, start, end):
    lazyUpdate(start, end, idx)
    
    if end < left or right < start: return
    
    if left <= start and end <= right: 
        tree[idx] += (end - start + 1) * val
        if start != end:
            lazy[idx * 2] += val
            lazy[idx * 2 + 1] += val
        return
        
    mid = (start + end) // 2
    update(left, right, val, idx * 2, start, mid)
    update(left, right, val, idx * 2 + 1, mid + 1, end)
    tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]    
    return 

def getSum(left, right, idx, start, end):
    lazyUpdate(start, end, idx)
    if end < left or right < start: return 0
    
    if left <= start and end <= right: return tree[idx]
    
    mid = (start + end) // 2
    l =  getSum(left, right, idx * 2, start, mid)
    r = getSum(left, right, idx * 2 + 1, mid + 1, end)
    return l + r

def setTreeNode(tree, idx, start, end):
    if start == end: 
        tree[idx] = numbers[start]
        return tree[idx]
    
    mid = (start + end) // 2
    left = setTreeNode(tree, idx * 2, start, mid)
    right = setTreeNode(tree, idx * 2 + 1, mid + 1, end)
    tree[idx] = left + right
    return tree[idx]

def init():
    tree = [0 for _ in range(n * 4)]
    setTreeNode(tree, 1, 1, n)
    return tree

'''main'''
n, m, k = map(int, input().split())
numbers = [0] + [int(input()) for _ in range(n)]
tree = init()
lazy = [0 for _ in range(n * 4)]

for _ in range(m + k):
    op = list(map(int, input().split()))
    if op[0] == 1: 
        update(op[1], op[2], op[3], 1, 1, n)
    elif op[0] == 2: 
        print(getSum(op[1], op[2], 1, 1, n))