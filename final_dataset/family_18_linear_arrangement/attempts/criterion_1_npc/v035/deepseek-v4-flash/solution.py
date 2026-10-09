import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    visited = [False] * n
    components = []
    for i in range(n):
        if not visited[i]:
            q = deque([i])
            visited[i] = True
            comp = []
            while q:
                u = q.popleft()
                comp.append(u)
                for w in adj[u]:
                    if not visited[w]:
                        visited[w] = True
                        q.append(w)
            components.append(comp)
    
    pos = [0] * n
    current_pos = 1
    for comp in components:
        # BFS from vertex with highest degree in comp
        start = max(comp, key=lambda x: len(adj[x]))
        q = deque([start])
        visited_comp = {start}
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for w in adj[u]:
                if w not in visited_comp:
                    visited_comp.add(w)
                    q.append(w)
        # Assign positions
        for u in order:
            pos[u] = current_pos
            current_pos += 1
    
    # Compute total length
    total = 0
    for u, v in edges:
        total += abs(pos[u] - pos[v])
    
    if total <= B:
        print("YES")
        print(" ".join(str(pos[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()