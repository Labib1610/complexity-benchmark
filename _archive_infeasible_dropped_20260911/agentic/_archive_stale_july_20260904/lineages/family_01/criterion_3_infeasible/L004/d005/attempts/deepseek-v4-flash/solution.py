n, m = map(int, input().split())
adj = [set() for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].add(v)
    adj[v].add(u)

for i in range(n):
    for j in adj[i]:
        if j > i:
            for k in adj[j]:
                if k > j and k in adj[i]:
                    print(i + 1, j + 1, k + 1)
                    exit()