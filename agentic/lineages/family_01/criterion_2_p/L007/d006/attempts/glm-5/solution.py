import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]); v = int(input_data[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    possible = True
    
    for start in range(1, n + 1):
        if color[start] == 0:
            color[start] = 1
            q = deque([start])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break
    
    if not possible:
        sys.stdout.write("NO\n")
        return
    
    # Check if any component is all isolated vertices (no edges)
    # For such components, we can assign all 1s (lexicographically smallest)
    # The BFS above already assigns 1 to the start, but if there are no edges,
    # all vertices in that component get color 1, which is correct.
    # However, if a component has edges, the coloring is forced (up to flip).
    # To get lexicographically smallest, we want to flip components where
    # the first vertex (smallest index) in the component has color 2.
    
    # But we need to identify components and their first vertex.
    # Rebuild component info
    comp_id = [0] * (n + 1)
    comp_first = []  # first (smallest) vertex in each component
    cid = 0
    visited = [False] * (n + 1)
    
    for i in range(1, n + 1):
        if not visited[i]:
            cid += 1
            comp_first.append(i)
            visited[i] = True
            q = deque([i])
            while q:
                u = q.popleft()
                comp_id[u] = cid
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
    
    # For each component, if the first vertex has color 2, flip the component
    flip = [False] * (cid + 1)
    for c in range(cid):
        first_v = comp_first[c]
        if color[first_v] == 2:
            flip[c + 1] = True
    
    result = []
    for i in range(1, n + 1):
        c = comp_id[i]
        val = color[i]
        if flip[c]:
            val = 3 - val
        result.append(str(val))
    
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(result) + "\n")

solve()