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
        # Try to assign 0 (choice 1) to this node
        # But we must check if assigning 0 leads to conflict
        # We'll do a temporary BFS with color[i]=0
        # If conflict, try color[i]=1
        # Since we process in order, this gives lexicographically smallest
        tmp_color = color[:]
        tmp_color[i] = 0
        q = deque([i])
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if tmp_color[v] == -1:
                    tmp_color[v] = tmp_color[u] ^ 1
                    q.append(v)
                elif tmp_color[v] == tmp_color[u]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            color = tmp_color
        else:
            # assign 1
            color[i] = 1
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        sys.exit()

# If we reach here, graph is bipartite
print("YES")
print(' '.join(str(c + 1) for c in color))