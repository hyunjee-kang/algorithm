'''
문제: 백준 1038 감소하는 수
유형: brute force, 백트래킹
노트: -
'''

def addDigit(digit, num):    
    # 자리수에 따라 증가
    if digit == 1: decreasing.append(num)
    else:
        for i in range(num % 10):
            addDigit(digit - 1, num * 10 + i)

def backtracking(digit): 
    for i in range(digit - 1, 10):
        addDigit(digit, i)
 
'''main'''   
decreasing=[] # 감소하는 숫자 리스트
for i in range(1, 11):
    backtracking(i)

n = int(input())
if n >= len(decreasing): print(-1) # 감소하는 숫자가 없을 때
else: print(decreasing[n])