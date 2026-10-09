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
        # BFS to color component
        color[i] = 0
        q = deque([i])
        comp_nodes = [i]
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                    comp_nodes.append(v)
                elif color[v] == color[u]:
                    possible = False
                    break
            if not possible:
                break
        if not possible:
            break

        # Now decide orientation for this component
        # comp_nodes sorted by index
        comp_nodes.sort()
        # Try both orientations: color[comp_nodes[0]] = 0 or 1
        # We'll compare the resulting assignments for this component
        # Orientation A: keep as is
        # Orientation B: flip all colors in this component
        # Choose lexicographically smaller for the whole array
        # Since components are independent, we can decide per component
        # But we need to compare only within this component's nodes
        # Because other components are not yet decided, but they will be decided later.
        # For lexicographic smallest overall, we should choose the orientation
        # that gives smaller value at the smallest index in this component.
        # If tie, move to next index, etc.
        # So we compare the two sequences for this component's sorted nodes.
        seqA = [color[x] for x in comp_nodes]
        seqB = [color[x] ^ 1 for x in comp_nodes]
        if seqB < seqA:
            for x in comp_nodes:
                color[x] ^= 1

if not possible:
    print("NO")
else:
    print("YES")
    print(' '.join(str(c + 1) for c in color))