from sys import stdin
input = lambda: stdin.readline()[:-1]

def dfs(v, c):
    vis[v] = True
    color[v] = c
    for u in g[v]:
        if not vis[u]:
            dfs(u, 3 - c)
        elif color[u] == c:
            return False
    return True

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
vis = [False] * (n + 1)
color = [-1] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

ans = []
flag = True
for i in range(1, n + 1):
    if not vis[i]:
        t = dfs(i, 1)
        if not t:
            flag = False
            break

if not flag:
    print("NO")
else:
    for i in range(1, n + 1):
        ans.append(color[i])
    print("YES")
    print(*ans)