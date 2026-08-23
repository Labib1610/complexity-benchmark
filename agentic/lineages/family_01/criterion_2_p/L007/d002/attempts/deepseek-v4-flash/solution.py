import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

color = [-1] * n
res = [1] * n

for start in range(n):
    if color[start] != -1:
        continue
    # BFS to get component
    comp = []
    q = deque([start])
    color[start] = 0
    comp.append(start)
    ok = True
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                comp.append(v)
                q.append(v)
            elif color[v] == color[u]:
                ok = False
    if not ok:
        print("NO")
        sys.exit()
    # Try both colorings for this component
    # coloring A: start node = 1
    # coloring B: start node = 2
    # We'll build both and pick lexicographically smaller
    # Since color array currently has 0/1 for this comp, we can map
    # 0 -> 1, 1 -> 2 for A
    # 0 -> 2, 1 -> 1 for B
    comp_sorted = sorted(comp)
    seqA = [0] * n
    seqB = [0] * n
    for u in comp:
        seqA[u] = 1 if color[u] == 0 else 2
        seqB[u] = 2 if color[u] == 0 else 1
    # Compare lexicographically on the component indices
    # We only need to compare on comp_sorted
    chooseA = False
    for u in comp_sorted:
        if seqA[u] < seqB[u]:
            chooseA = True
            break
        elif seqA[u] > seqB[u]:
            break
    for u in comp:
        res[u] = seqA[u] if chooseA else seqB[u]

print("YES")
print(" ".join(map(str, res)))