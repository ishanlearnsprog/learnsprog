n = 38 
m = [-1 for _ in range(n+1)]

def rec(n):
    if n == 0 or n == 1: return 1
    return rec(n-1) + rec(n-2)

def mem(n):
    if n == 0 or n == 1: return 1
    if m[n] != -1: return m[n]
    m[n] = mem(n-1) + mem(n-2)
    return m[n]

def tab(n):
    m[0], m[1] = 1, 1
    for i in range(2, n+1):
        m[i] = m[i-1] + m[i-2]
    return m[-1]

def sotab(n):
    p1 = 1
    p2 = 1
    cur = 0
    for i in range(2, n+1):
        cur = p1 + p2
        p2 = p1
        p1 = cur
    return p1

print(sotab(n))
