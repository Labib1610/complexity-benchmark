from sys import stdin

n, m = map(int, stdin.readline().split())
g = [[] for _ in range(n + 1)]
for i in range(m):
    u, v = map(int, stdin.readline().split())
    g[u].append(v)
    g[v].append(u)

a = [0] * (n + 1)
colors = [set() for _ in range(3)]

def dfs(u, c):
    if a[u]:
        return a[u] == c
    a[u] = c
    colors[c].add(u)
    for v in g[u]:
        if not dfs(v, 3 - c):
            return False
    return True

for i in range(1, n + 1):
    if not a[i] and not dfs(i, 1):
        print('NO')
        exit()

if len(colors[1]) > len(colors[2]):
    colors[1], colors[2] = colors[2], colors[1]

print('YES')
ans = []
for i in range(1, n + 1):
    if i in colors[1]:
        ans.append('1')
    else:
        ans.append('2')

print(' '.join(ans))