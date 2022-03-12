'''
문제: 백준 16975 수열과 쿼리 21
유형: lazy propagation - segment tree
노트: -
'''

import math
from sys import stdin
input = stdin.readline

def lazyUpdate(idx, start, end):
    # lazy 값 없으면 제껴
    if lazy[idx] == 0: return
    # lazy 값을 tree에 적용
    tree[idx] += lazy[idx] * (end - start + 1) 
    # leaf가 아닌 경우 자식한테 물려주기
    if start != end:
        lazy[idx * 2] += lazy[idx]
        lazy[idx * 2 + 1] += lazy[idx]
    # lazy 값 초기화
    lazy[idx] = 0
    return

def update(idx, start, end, left, right, value):
    # 일단 lazy 처리
    lazyUpdate(idx, start, end)
    # 범위 벗어나는 경우
    if end < left or right < start: return
    # 범위 완전히 포함되는 경우
    if left <= start and end <= right: 
        tree[idx] += value * (end - start + 1)
        if start != end: 
            lazy[idx * 2] += value
            lazy[idx * 2 + 1] += value
        return
    # 범위 일부만 포함되는 경우
    mid = (start + end) // 2
    update(idx * 2, start, mid, left, right, value)
    update(idx * 2 + 1, mid + 1, end, left, right, value)
    tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]
    return

def getValue(idx, start, end, left, right):
    # 일단 lazy 처리
    lazyUpdate(idx, start, end)
    # 범위 벗어나는 경우
    if end < left or right < start: return 0
    # 범위 완전히 포함되는 경우
    if left <= start and end <= right: return tree[idx]
    # 범위 일부만 포함하는 경우
    mid = (start + end) // 2
    l = getValue(idx * 2, start, mid, left, right)
    r = getValue(idx * 2 + 1, mid + 1, end, left, right) 
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
n = int(input())
numbers = [0] + list(map(int, input().split()))
tree = init()
lazy = [0 for _ in range(n * 4)]

m = int(input())
for _ in range(m):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1:
        update(1, 1, n, tmp[1], tmp[2], tmp[3])
    elif tmp[0] == 2:
        print(getValue(1, 1, n, tmp[1], tmp[1]))