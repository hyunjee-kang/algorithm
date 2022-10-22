***
백준 1701 Cubeditor
KMP
***

from sys import stdin
input = stdin.readline

src = list(input())

def makeTable(start):
    table = [0 for _ in range(len(src))]
    
    j = start
    for i in range(j + 1, len(src)):
        while (j > start and src[i] != src[j]):
            j = table[j - 1] + start
        if src[i] == src[j]:
            j += 1
            table[i] = 0 if (j - start) < 0 else j - start          

    return table

ans = -1
for i in range(len(src) - 1):
    ans = max(ans, max(makeTable(i)))

print(ans)