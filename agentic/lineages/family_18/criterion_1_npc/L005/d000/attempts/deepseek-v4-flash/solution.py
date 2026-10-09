n, m, B = map(int, input().split())
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges.append((u, v))

# Try a greedy placement: assign in order 1..n
pos = list(range(1, n + 1))

# Check total wire length
total = 0
for u, v in edges:
    total += abs(pos[u] - pos[v])

if total <= B:
    print("YES")
    print(" ".join(map(str, pos)))
else:
    print("NO")