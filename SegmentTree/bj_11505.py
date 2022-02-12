'''
문제: 백준 11505 구간 곱 구하기
유형: 자료구조, 세그먼트 트리, 인덱스 트리
노트: update함수 잘봐
'''
import math
from sys import stdin
input = stdin.readline
    
def getMultiple(tree, idx, start, end, l, r):
    # 범위가 벗어남
    if r < start or end < l: return 1
    # 구하려는 범위가 노드의 범위를 완전히 포함
    if l <= start and end <= r: return tree[idx]
    # 일부만 포함
    left = getMultiple(tree, idx * 2, start, (start + end) // 2, l, r)
    right = getMultiple(tree, idx * 2 + 1, (start + end) // 2 + 1, end, l, r)
    return left * right % div

def update(tree, arr, node, val, idx, start, end):
    # 바꾸려는 노드가 범위를 넘어갔을 경우
    if node < start or end < node: return
    # 리프인 경우 값 바로 대입
    if start == end:
        tree[idx] = val
        return
    # 범위 내에 있을 경우 값 변경
    update(tree, arr, node, val, idx * 2, start, (start + end) // 2)
    update(tree, arr, node, val, idx * 2 + 1, (start + end) // 2 + 1, end)
    tree[idx] = tree[idx * 2] * tree[idx * 2 + 1] % div
    
def initTree(tree, arr, idx, start, end):
    if start == end: 
        tree[idx] = arr[start]
        return tree[idx]

    left = initTree(tree, arr, idx * 2, start, (start + end) // 2)
    right = initTree(tree, arr, idx * 2 + 1, (start + end) // 2 + 1, end)
    tree[idx] = left * right % div
    return tree[idx]
    
def makeTree(n, arr):
    # 트리의 높이 = 올림(밑이 2인 로그 N)
    # 트리의 크기 = 2^(높이+1)
    tree_size = 1 << (math.ceil(math.log(n, 2)) + 1)
    tree = [1 for _ in range(tree_size)]
    initTree(tree, arr, 1, 1, n)
    return tree

'''main'''
div = 1000000007
n, m, k = map(int, input().split())
arr = [1]
for _ in range(n):
    arr.append(int(input()))

tree = makeTree(n, arr)

for _ in range(m + k):
    order, a, b = map(int, input().split())
    if order == 1:
        update(tree, arr, a, b, 1, 1, n)
        arr[a] = b
    elif order == 2:
        print(getMultiple(tree, 1, 1, n, a, b))
    