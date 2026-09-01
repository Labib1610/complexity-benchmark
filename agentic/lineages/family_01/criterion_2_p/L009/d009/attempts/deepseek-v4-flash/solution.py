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

def bfs(start):
    q = deque([start])
    color[start] = 0
    comp = [start]
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                q.append(v)
                comp.append(v)
            elif color[v] == color[u]:
                return False, comp
    return True, comp

# Check bipartiteness and collect components
components = []
possible = True
for i in range(n):
    if color[i] == -1:
        ok, comp = bfs(i)
        if not ok:
            possible = False
            break
        components.append(comp)

if not possible:
    print("NO")
else:
    # Now we have a valid 2-coloring, but we want lexicographically smallest.
    # We'll try to flip components if it makes earlier nodes 1.
    # Since color[0] is 0 (meaning radius 1), we check each component:
    # If the component contains node 0, we keep as is.
    # For other components, we check if flipping gives smaller lexicographic order.
    
    # Build final assignment
    res = [0] * n
    for comp in components:
        # Determine if flipping is better
        # Count positions where color is 0 vs 1
        # We want smallest lexicographic: prefer 1 (radius 1) at smallest index.
        # So for each component, compare current vs flipped.
        flip = False
        # If first node in comp (smallest index) has color 1, flipping makes it 0 (radius 1) which is better.
        min_idx = min(comp)
        if color[min_idx] == 1:
            flip = True
        for u in comp:
            if flip:
                res[u] = 2 if color[u] == 0 else 1
            else:
                res[u] = 1 if color[u] == 0 else 2

    print("YES")
    print(" ".join(map(str, res)))