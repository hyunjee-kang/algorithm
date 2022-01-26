'''
문제: 백준 2805 나무 자르기
유형: 이분 탐색
노트: 입력이 아래와 같을 경우 무한루프에 빠지지 않도록 주의 (21번 라인)
      2 3
      2 2   (답: 0)
'''

def binarySearch():
    l = -1
    r = trees[-1]
    
    while (l < r):
        tot = 0
        mid = (l + r) // 2
        for i in trees:
            tot += (i - mid) if i - mid > 0 else 0 
        
        if tot == M: return mid
        elif tot < M: 
            r = mid
        elif tot > M: 
            if (mid + r) // 2 == mid: return mid
            l = mid

'''main'''
N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

print(binarySearch())