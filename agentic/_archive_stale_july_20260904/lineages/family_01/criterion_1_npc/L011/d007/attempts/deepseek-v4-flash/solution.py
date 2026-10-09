n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

colors = [0] * n
found = False

def backtrack(idx):
    global found
    if idx == n:
        found = True
        return True
    for c in range(1, 4):
        ok = True
        for nb in adj[idx]:
            if colors[nb] == c:
                ok = False
                break
        if ok:
            colors[idx] = c
            if backtrack(idx + 1):
                return True
            colors[idx] = 0
    return False

if backtrack(0):
    print("YES")
    print(" ".join(str(c) for c in colors))
else:
    print("NO")