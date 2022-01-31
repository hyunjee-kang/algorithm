'''
문제: 백준 14621 나만 안되는 연애
유형: kruskal, mst
노트: 40째 줄 정렬 방법 유의
'''

def union(parent, a, b):
    a_parent = find(parent, a)
    b_parent = find(parent, b)
    if a_parent == b_parent: return -1
    parent[b_parent] = a_parent
    return 0

def find(parent, a):
    if parent[a] == a: return a
    return find(parent, parent[a])

def kruskal(conn):
    n_total = 1
    w_total = 0
    parent = [i for i in range(n + 1)]
    for i in conn:
        if union(parent, i[0], i[1]) < 0: continue
        n_total += 1
        w_total += i[2]
        if n_total == n: return w_total
        
    return -1


'''main'''
n, m = map(int, input().split())
sex = list(input().split())
conn = []
for _ in range(m):
    u, v, d = map(int, input().split())
    if sex[u - 1] == sex[v - 1]: continue
    conn.append((u, v, d))

conn.sort(key = lambda val : val[2])
print(kruskal(conn))
