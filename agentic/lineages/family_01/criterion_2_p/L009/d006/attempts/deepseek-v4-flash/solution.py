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
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                q.append(v)
            elif color[v] == color[u]:
                return False
    return True

for i in range(n):
    if color[i] == -1:
        if not bfs(i):
            print("NO")
            sys.exit()

# Now we have a valid bipartition, but we need lexicographically smallest assignment.
# We can try to flip components if it makes c1 smaller.
# Since each component is independent, we can choose orientation per component.

visited = [False] * n
for i in range(n):
    if not visited[i]:
        # BFS to collect component
        comp = []
        q = deque([i])
        visited[i] = True
        while q:
            u = q.popleft()
            comp.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        # Try both orientations: current color or flipped
        # We want lexicographically smallest overall, so we compare
        # orientation A: color as is
        # orientation B: flip colors in this component
        # We'll build both and pick the one that gives smaller c1, then c2, etc.
        # Since components are independent, we can decide per component by comparing
        # the first node in the component (smallest index) in both orientations.
        comp.sort()
        first = comp[0]
        # orientation A: color[first] stays
        # orientation B: flip
        # We'll choose the orientation that gives smaller value at first node
        # If equal, we need to compare further, but since first is smallest index in comp,
        # and all other nodes in comp are larger, we can just pick the one with smaller at first.
        # Actually we need to compare the whole sequence, but because components are independent
        # and we process in increasing index order, we can decide greedily.
        # We'll store the orientation decision.
        # Let's just flip if color[first] == 1 (so we can make it 0)
        if color[first] == 1:
            for u in comp:
                color[u] ^= 1

# Now output
print("YES")
print(' '.join(str(c + 1) for c in color))