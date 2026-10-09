n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

colors = [0] * n

def backtrack(idx):
    if idx == n:
        return True
    for c in (1, 2, 3):
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
    print(" ".join(map(str, colors)))
else:
    print("NO")