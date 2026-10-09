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

for start in range(n):
    if color[start] != -1:
        continue
    # BFS to check bipartiteness and get component
    q = deque([start])
    color[start] = 0
    comp = [start]
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                comp.append(v)
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
    # Now we have a valid 2-coloring (0/1). We need to map to 1/2.
    # But we want lexicographically smallest: try flipping each component if it helps.
    # We'll do BFS again, but assign 1 to start if possible, else 2.
    final = [0] * n
    visited = [False] * n
    for start in range(n):
        if visited[start]:
            continue
        # Try assigning 1 to start
        temp1 = [0] * n
        q = deque([start])
        visited1 = [False] * n
        visited1[start] = True
        temp1[start] = 1
        ok1 = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited1[v]:
                    visited1[v] = True
                    temp1[v] = 3 - temp1[u]  # 1->2, 2->1
                    q.append(v)
                elif temp1[v] == temp1[u]:
                    ok1 = False
                    break
            if not ok1:
                break
        # Try assigning 2 to start
        temp2 = [0] * n
        q = deque([start])
        visited2 = [False] * n
        visited2[start] = True
        temp2[start] = 2
        ok2 = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited2[v]:
                    visited2[v] = True
                    temp2[v] = 3 - temp2[u]
                    q.append(v)
                elif temp2[v] == temp2[u]:
                    ok2 = False
                    break
            if not ok2:
                break
        # Choose lexicographically smaller valid one
        if ok1 and ok2:
            # Compare only within this component
            comp_nodes = [i for i in range(n) if visited1[i]]
            use1 = False
            for node in comp_nodes:
                if temp1[node] != temp2[node]:
                    use1 = temp1[node] < temp2[node]
                    break
            if use1:
                for node in comp_nodes:
                    final[node] = temp1[node]
                    visited[node] = True
            else:
                for node in comp_nodes:
                    final[node] = temp2[node]
                    visited[node] = True
        elif ok1:
            for node in range(n):
                if visited1[node]:
                    final[node] = temp1[node]
                    visited[node] = True
        else:
            for node in range(n):
                if visited2[node]:
                    final[node] = temp2[node]
                    visited[node] = True

    print("YES")
    print(" ".join(map(str, final)))