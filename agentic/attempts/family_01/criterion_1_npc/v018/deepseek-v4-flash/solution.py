n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

color = [0] * n

def backtrack(idx):
    if idx == n:
        return True
    for c in range(1, 4):
        ok = True
        for nb in edges[idx]:
            if color[nb] == c:
                ok = False
                break
        if ok:
            color[idx] = c
            if backtrack(idx + 1):
                return True
            color[idx] = 0
    return False

if backtrack(0):
    print("YES")
    print(" ".join(map(str, color)))
else:
    print("NO")