from sys import stdin

def dfs(v):
    if v == n + 1:
        return True
    for i in range(1, 4):
        ok = True
        for x in e[v]:
            if c[x] == i:
                ok = False
                break
        if not ok:
            continue
        c[v] = i
        if dfs(v + 1):
            return True
    return False

n, m = map(int, stdin.readline().split())
e = [[] for _ in range(n + 1)]
c = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, stdin.readline().split())
    e[u].append(v)
    e[v].append(u)

if dfs(1):
    print("YES")
    for i in range(1, n + 1):
        print(c[i], end=" ")
else:
    print("NO")