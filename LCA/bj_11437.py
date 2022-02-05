'''
문제: 백준 11437 LCA
유형: Lowest Common Ancestor
노트: 기본 유형, 코드 그냥 외우면 됨
'''

def dfs(node, level):
    depth[node] = level # depth 저장
    if len(tree[node]) == 0: return
    for i in tree[node]:
        if depth[i] != 0: continue
        ancestor[0][i] = node # 바로 위의 부모 저장
        dfs(i, level + 1)


def setAncestor():
    for i in range(1, max_depth + 1):
        for j in range(1, n + 1):
            # 이해가 안가면 외우랬슴
            ancestor[i][j] = ancestor[i - 1][ancestor[i - 1][j]] 


def lca(a, b):
    # a의 depth가 더 크도록 조절
    if depth[a] < depth[b]: a, b = b, a
    
    # 둘의 depth를 맞춰 준다
    for i in range(max_depth, -1, -1):
        if depth[a] - depth[b] >= (1 << i):
            a = ancestor[i][a]

    # 둘이 같으면 자기 자신이 최소 공통 조상
    if a == b: return a
    
    # 부모가 달라지는 지점 찾기
    for i in range(max_depth, -1, -1):
        if ancestor[i][a] != ancestor[i][b]:
            a = ancestor[i][a]
            b = ancestor[i][b]

    # 위에서 찾은 값의 부모가 최소 공통 조상
    return ancestor[0][a]


'''main''' 
n = int(input())
tree = {i : [] for i in range(1, n + 1)}
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 보통 깊이가 최대 2^20
max_depth = 20
# 각 노드의 깊이를 저장할 공간
depth = [0 for _ in range(n + 1)]
# ancestor[i][node] == node의 2^i번째 부모의 값
ancestor = [[0 for _ in range(n + 1)] for _ in range(max_depth + 1)]

dfs(1, 1)
setAncestor()

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
