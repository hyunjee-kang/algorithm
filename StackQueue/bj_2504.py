'''
문제: 백준 2504 괄호의 값
유형: 스택, 자료구조, 재귀
노트: -
'''
def getNumber(code):
    if code == '(' or code == ')': return 2
    if code == '[' or code == ']': return 3

def getSign(a, b):
    if (a == ')' or a == ']') and (b == '(' or b == '['): return '+'
    else: return '*'
    
def calc(expression):
    if len(expression) == 0: return
    
    val = expression.pop()
    while len(expression) > 0:
        order = expression.pop()
        if order == '*':
            val *= expression.pop()
        else:
            val += expression.pop()
    
    global total
    total += val
    
def isPartner(a, b):
    if a == '(' and b == ')': return True
    if a == '[' and b == ']': return True
    return False

hz = ''


inputLine = input()
stack = []
exp = []
total = 0

cursor = ''
for i in inputLine:
    if len(stack) == 0:
        stack.append(i)
        if i == ')' or i == ']': break
        calc(exp)
        exp = []
        exp.append(getNumber(i))
        hz += '||||' + str(getNumber(i))
    else:
        if isPartner(stack[-1], i):
            stack.pop()
        else:
            stack.append(i)
            exp.append(getSign(cursor, i))
            exp.append(getNumber(i))
            hz += getSign(cursor, i) + str(getNumber(i))
    
    cursor = i

print(hz)

if len(stack) != 0:
    print(0)
else:
    calc(exp)
    print(total)