'''
문제: 백준 1759 암호 만들기
유형: 백트래킹
노트: -
'''

def isValidPassword(pw):
    aeiou = 0
    cond1 = False
    cond2 = False
    if 'a' in pw: 
        cond1 = True
        aeiou += 1
    if 'e' in pw: 
        cond1 = True
        aeiou += 1
    if 'i' in pw: 
        cond1 = True
        aeiou += 1
    if 'o' in pw: 
        cond1 = True
        aeiou += 1
    if 'u' in pw: 
        cond1 = True
        aeiou += 1
    if L - aeiou > 1: cond2 = True
    
    if cond1 and cond2: return True
    else: return False
    
def findPassword(idx, pw):
    if len(pw) == L:
        if ''.join(pw) not in pwList and isValidPassword(pw): 
            pwList.append(''.join(pw))
        return
    
    for i in range(idx, C):
        pw.append(alpha[i])
        findPassword(i + 1, pw)
        pw.pop()
        findPassword(i + 1, pw)


'''main'''
L, C = map(int, input().split())
alpha = list(input().split())
pwList = []

alpha.sort()
findPassword(0, [])
for i in pwList:
    print(i)