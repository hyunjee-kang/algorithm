'''
문제: 백준 5676 음주 코딩
유형: 자료구조, 세그먼트 트리, 인덱스 트리
노트: -
'''
import sys

def executeC(tree, target, value):
    # update
    tree[target] = value
    target //= 2
    while target > 0:
        tree[target] = tree[target * 2] * tree[target * 2 + 1]
        target //= 2

def executeP(tree, start, end):
    # multiply
    mul = 1
    while start <= end:
        if start % 2 == 1: mul *= tree[start]
        if end % 2 == 0: mul *= tree[end]
        start = (start + 1) // 2
        end = (end - 1) // 2 
    
    if mul == 0: return '0'
    elif mul > 0 : return '+'
    else: return '-'


def init(n, x):
    base = 1
    while base < n: base *= 2
    
    tree = [0 for _ in range(base)]
    for i in x:
        if i == 0: tree.append(0)
        elif i > 0: tree.append(1)
        else: tree.append(-1)
    for i in range(base - n): tree.append(0)
    for i in range(base - 1, 0, -1):
        tree[i] = tree[i * 2] * tree[i * 2 + 1]
        
    return base, tree  


''' main '''
lines = sys.stdin.readlines()
for line in lines:
    # input
    n, k = map(int, line.split())
    x = list(map(int, line.split()))
    # solution
    base, tree = init(n, x)
    answer = ''
    for _ in range(k):
        order, i, j = input().split()
        if order == 'C': 
            executeC(tree, base + int(i) - 1, int(j))
        elif order == 'P': 
            answer += executeP(tree, base + int(i) - 1, base + int(j) - 1)
            
    print(answer)