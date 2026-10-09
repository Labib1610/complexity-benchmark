import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
has_self_loop = False

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if u == v:
        has_self_loop = True
    adj[u].append(v)
    adj[v].append(u)

if has_self_loop:
    print("NO")
    sys.exit()

color = [-1] * n

for start in range(n):
    if color[start] != -1:
        continue
    # Try to color start as 1
    color[start] = 1
    q = deque([start])
    ok = True
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                q.append(v)
            elif color[v] == color[u]:
                ok = False
                break
        if not ok:
            break
    if not ok:
        print("NO")
        sys.exit()

# Now we have a valid 2-coloring, but we need lexicographically smallest.
# For each component, we can flip colors if it makes the sequence smaller.
# We'll do BFS again to find components and decide orientation.

visited = [False] * n
res = [0] * n

for start in range(n):
    if visited[start]:
        continue
    # BFS to collect component
    comp = []
    q = deque([start])
    visited[start] = True
    while q:
        u = q.popleft()
        comp.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    # comp is a list of vertices in this component
    # We have two possible assignments: keep color as is, or flip
    # Build both options
    opt1 = [0] * n
    opt2 = [0] * n
    for u in comp:
        if color[u] == 1:
            opt1[u] = 1
            opt2[u] = 2
        else:
            opt1[u] = 2
            opt2[u] = 1
    # Compare lexicographically for this component
    # We'll fill res with the smaller option
    for u in comp:
        if opt1[u] < opt2[u]:
            res[u] = opt1[u]
        elif opt2[u] < opt1[u]:
            res[u] = opt2[u]
        else:
            res[u] = opt1[u]  # equal, doesn't matter

# But we need to ensure the whole sequence is lexicographically smallest.
# The above per-component choice is not enough globally.
# We need to process components in order of their smallest vertex index,
# and choose orientation that makes the overall sequence smallest.

# Let's redo properly:
visited = [False] * n
res = [0] * n

for start in range(n):
    if visited[start]:
        continue
    # BFS to collect component
    comp = []
    q = deque([start])
    visited[start] = True
    while q:
        u = q.popleft()
        comp.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    # comp is sorted by BFS order, but we need sorted by index for lexicographic
    comp.sort()
    # Try both orientations
    # Orientation A: keep color as is
    # Orientation B: flip
    # We'll assign to res and compare
    tempA = [0] * n
    tempB = [0] * n
    for u in comp:
        if color[u] == 1:
            tempA[u] = 1
            tempB[u] = 2
        else:
            tempA[u] = 2
            tempB[u] = 1
    # Compare lexicographically on comp indices
    chooseA = True
    for u in comp:
        if tempA[u] < tempB[u]:
            chooseA = True
            break
        elif tempB[u] < tempA[u]:
            chooseA = False
            break
    for u in comp:
        res[u] = tempA[u] if chooseA else tempB[u]

print("YES")
print(" ".join(map(str, res)))