n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

color = [0] * n
found = False

def dfs(idx):
    global found
    if idx == n:
        return True
    for c in (1, 2, 3):
        ok = True
        for nb in adj[idx]:
            if color[nb] == c:
                ok = False
                break
        if ok:
            color[idx] = c
            if dfs(idx + 1):
                return True
            color[idx] = 0
    return False

if dfs(0):
    print("YES")
    print(" ".join(map(str, color)))
else:
    print("NO")