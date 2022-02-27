'''
문제: 백준 1561 놀이 공원
유형:이분 탐색
노트: -
'''

from sys import stdin
input = stdin.readline

def isPossible(time):
    total = m + sum(time // i for i in play)
    if total >= n: return True
    return False

def binarySearch():
    l = 0
    r = 60000000000
    max_time = 0
    while l <= r:
        mid = (l + r) // 2
        if isPossible(mid): 
            r = mid - 1
            max_time = mid
        else: l = mid + 1
    
    return max_time
    

'''main'''
n, m = map(int, input().split())
play = list(map(int, input().split()))

if n <= m: print(n)
else: 
    max_time = binarySearch()
    answer = m + sum((max_time - 1) // i for i in play)
    for i, val in enumerate(play):
        if max_time % val == 0: answer += 1
        if answer == n: 
            print(i + 1)
            break
