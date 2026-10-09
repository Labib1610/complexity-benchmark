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
    # try starting with color 0 (type 1)
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

# Now we have a valid bipartite coloring, but we need lexicographically smallest.
# We can try flipping colors in each connected component if it improves lexicographic order.
visited = [False] * n
for i in range(n):
    if not visited[i]:
        # collect component
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
        # count how many would be type 1 if we keep current coloring
        cnt1 = sum(1 for u in comp if color[u] == 0)
        cnt2 = len(comp) - cnt1
        # If flipping gives more type 1s at smaller indices, flip
        # Actually we want lexicographically smallest, so we compare sequences.
        # We can just try flipping and see if it's better.
        # Since components are independent, we can decide per component.
        # For lexicographic smallest, we want earliest index to be 1 if possible.
        # So if the smallest index in comp currently has color 1, flip.
        min_idx = min(comp)
        if color[min_idx] == 1:
            for u in comp:
                color[u] ^= 1

print("YES")
print(' '.join(str(c + 1) for c in color))