n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Build adjacency list
adj = [[] for _ in range(n)]
for u, v in edges:
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

best = None
best_metric = None

# Try all 3^n colorings
for mask in range(3**n):
    colors = []
    tmp = mask
    for _ in range(n):
        colors.append(tmp % 3)
        tmp //= 3
    
    # Check if valid
    valid = True
    for u in range(n):
        for v in adj[u]:
            if colors[u] == colors[v]:
                valid = False
                break
        if not valid:
            break
    if not valid:
        continue
    
    # Compute metric
    metric = 0
    for subset in range(1, 1 << n):
        # find smallest index in subset
        k = (subset & -subset).bit_length() - 1
        size = bin(subset).count("1")
        metric += (colors[k] + 1) * (3 ** (size - 1))
    
    if best_metric is None or metric < best_metric:
        best_metric = metric
        best = colors

if best is None:
    print("NO")
else:
    print("YES")
    print(" ".join(str(c+1) for c in best))