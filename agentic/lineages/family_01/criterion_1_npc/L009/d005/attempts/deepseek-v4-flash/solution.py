n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

adj = [[] for _ in range(n)]
for u, v in edges:
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

colors = [0] * n

for i in range(n):
    used = set()
    for nb in adj[i]:
        if colors[nb] != 0:
            used.add(colors[nb])
    for c in (1, 2, 3):
        if c not in used:
            colors[i] = c
            break
    else:
        print("NO")
        break
else:
    print("YES")
    print(" ".join(map(str, colors)))