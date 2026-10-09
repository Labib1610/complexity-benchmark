n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

colors = [0] * n

def backtrack(idx):
    if idx == n:
        return True
    for c in range(1, 4):
        ok = True
        for nb in graph[idx]:
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