'''
문제: 백준 2042 구간 합 구하기
유형: 자료구조, 세그먼트 트리, 인덱스 트리
노트: -
'''

def init(n, numbers):
    base = 1
    while base < n: base *= 2

    tree = [0 for _ in range(base)]
    for i in numbers: tree.append(i)
    for _ in range(base - n): tree.append(0)
    for i in range(base - 1, 0, -1):
        tree[i] = tree[i * 2] + tree[i * 2 + 1]

    return base, tree


def update(tree, target, value):
    diff = value - tree[target]
    while target > 0:
        tree[target] += diff 
        target //= 2


def getSum(tree, left, right):
    total = 0
    while left <= right:
        if left % 2 == 1: total += tree[left]
        if right % 2 == 0: total += tree[right]
        left = (left + 1) // 2
        right = (right - 1) // 2

    return total

'''main'''
n, m, k = map(int, input().split())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

base, tree = init(n, numbers)

for _ in range(m + k):
    order, a, b = map(int, input().split())
    if order == 1: update(tree, base + a - 1, b)
    elif order == 2: print(getSum(tree, base + a - 1, base + b - 1))
