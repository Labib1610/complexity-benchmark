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
possible = True

for i in range(n):
    if color[i] == -1:
        color[i] = 0
        q = deque([i])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    possible = False
                    break
            if not possible:
                break
    if not possible:
        break

if not possible:
    print("NO")
else:
    # Now assign values: color 0 -> 1, color 1 -> 2
    # But tie-breaking: process in order, if both possible, choose 1.
    # Since bipartite coloring is unique per component up to swap,
    # we need to choose orientation that gives smallest lexicographic result.
    # We can try both orientations for each component and pick lexicographically smaller.
    
    comp_id = [-1] * n
    comps = []
    cid = 0
    for i in range(n):
        if comp_id[i] == -1:
            comp_id[i] = cid
            comps.append([i])
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if comp_id[v] == -1:
                        comp_id[v] = cid
                        comps[-1].append(v)
                        q.append(v)
            cid += 1

    # For each component, try both color flips and pick lexicographically smaller
    result = [0] * n
    for comp in comps:
        # orientation 0: color as originally assigned
        # orientation 1: flip
        # We'll build both and compare
        arr0 = [0] * n
        arr1 = [0] * n
        for node in comp:
            c = color[node]
            arr0[node] = 1 if c == 0 else 2
            arr1[node] = 2 if c == 0 else 1
        # Compare lexicographically
        if arr0 < arr1:
            for node in comp:
                result[node] = arr0[node]
        else:
            for node in comp:
                result[node] = arr1[node]

    print("YES")
    print(" ".join(map(str, result)))