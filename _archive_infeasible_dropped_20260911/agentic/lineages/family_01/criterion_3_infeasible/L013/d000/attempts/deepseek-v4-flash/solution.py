n, m = map(int, input().split())
edges = set()
for _ in range(m):
    u, v = map(int, input().split())
    edges.add((u, v))
    edges.add((v, u))

for a in range(1, n+1):
    for b in range(a+1, n+1):
        if (a, b) not in edges:
            continue
        for c in range(b+1, n+1):
            if (a, c) in edges and (b, c) in edges:
                print(a, b, c)
                exit()