'''
문제: 백준 2268 수들의 합 7
유형: 자료구조, 세그먼트 트리, 인덱스 트리
노트: -
'''
from sys import stdin
input = stdin.readline

def getSum(tree, l, r, idx, start, end):
    # 범위에 해당하지 않는 경우
    if r < start or end < l: return 0
    # 범위를 완전히 포함하는 경우
    if l <= start and end <= r: return tree[idx]
    # 일부 포함된 경우
    mid = (start + end) // 2
    left = getSum(tree, l, r, idx * 2, start, mid)
    right = getSum(tree, l, r, idx * 2 + 1, mid + 1, end)
    return left + right

def modify(tree, node, value, idx, start, end):
    # 범위에 해당하지 않는 경우
    if node < start or end < node: return
    # leaf
    if start == end: 
        tree[idx] += value
        return
    # 범위 내에 있을 경우
    tree[idx] += value
    mid = (start + end) // 2
    modify(tree, node, value, idx * 2, start, mid)
    modify(tree, node, value, idx * 2 + 1, mid + 1, end)

def init():
    # 트리 노드 수의 범위: 2n <= 노드 < 4n
    tree = [0 for _ in range(n * 4)]
    return tree

'''main'''
n, m = map(int, input().split())
numbers = [0 for _ in range(n + 1)]
tree = init()
for _ in range(m):
    order, x, y = map(int, input().split())
    if order == 0: 
        print(getSum(tree, x, y, 1, 1, n))
    else:
        diff = y - numbers[x]
        numbers[x] = y 
        modify(tree, x, diff, 1, 1, n)
