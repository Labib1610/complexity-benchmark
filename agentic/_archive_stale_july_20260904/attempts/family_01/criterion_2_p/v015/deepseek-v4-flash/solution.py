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
    color[start] = 1
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 3 - color[u]  # alternate 1 <-> 2
                q.append(v)
            elif color[v] == color[u]:
                return False
    return True

for i in range(n):
    if color[i] == -1:
        if not bfs(i):
            print("NO")
            sys.exit()

# Now we have a valid bipartite coloring, but we need lexicographically smallest.
# We can try to flip components if it makes the sequence smaller.
# We'll do a BFS/DFS that tries to assign 1 whenever possible.

color = [-1] * n
for i in range(n):
    if color[i] == -1:
        # Try to color this component with i = 1
        color[i] = 1
        q = deque([i])
        comp = [i]
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 3 - color[u]
                    q.append(v)
                    comp.append(v)
        # Check if flipping this component gives a smaller lexicographic result
        # We compare current vs flipped for this component
        flip = []
        for u in comp:
            flip.append(3 - color[u])
        # If flipping makes the sequence smaller, apply it
        # We compare only positions in this component
        change = False
        for u in sorted(comp):
            if flip[u] < color[u]:
                change = True
                break
            elif flip[u] > color[u]:
                break
        if change:
            for u in comp:
                color[u] = 3 - color[u]

print("YES")
print(" ".join(str(color[i]) for i in range(n)))