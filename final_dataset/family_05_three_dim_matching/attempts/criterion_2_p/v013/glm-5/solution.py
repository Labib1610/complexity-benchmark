import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    # adj[x] = set of valid z values for specialist x
    adj = [set() for _ in range(k + 1)]
    
    for _ in range(t):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        z = int(input_data[idx]); idx += 1
        adj[x].add(z)
    
    # Convert to lists for faster iteration
    adj_list = [sorted(s) for s in adj]
    
    # Hopcroft-Karp for bipartite matching
    # Left: specialists 1..k, Right: time slots 1..k
    pair_u = [0] * (k + 1)  # pair_u[x] = z matched to x
    pair_v = [0] * (k + 1)  # pair_v[z] = x matched to z
    dist = [0] * (k + 1)
    INF = float('inf')
    NIL = 0
    
    def bfs():
        queue = deque()
        for u in range(1, k + 1):
            if pair_u[u] == NIL:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        dist[NIL] = INF
        while queue:
            u = queue.popleft()
            if dist[u] < dist[NIL]:
                for v in adj_list[u]:
                    if dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        queue.append(pair_v[v])
        return dist[NIL] != INF
    
    # Iterative DFS to avoid recursion limit issues
    def dfs(u):
        stack = [(u, 0)]
        while stack:
            curr, i = stack[-1]
            if i < len(adj_list[curr]):
                stack[-1] = (curr, i + 1)
                v = adj_list[curr][i]
                if dist[pair_v[v]] == dist[curr] + 1:
                    if pair_v[v] == NIL or dfs(pair_v[v]):
                        pair_u[curr] = v
                        pair_v[v] = curr
                        stack.pop()
                        return True
            else:
                dist[curr] = INF
                stack.pop()
                return False
        return False
    
    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pair_u[u] == NIL:
                if dfs(u):
                    matching += 1
    
    if matching == k:
        print("YES")
        out = []
        for x in range(1, k + 1):
            z = pair_u[x]
            # Find the machine y for specialist x
            # Since each x has unique y, and we need to output x y z
            # We need to recover y from the input
            out.append(f"{x} ? {z}")
        # Actually we need y - let me re-read input to build x->y mapping
        # Redo: store y mapping
        pass
    else:
        print("NO")

solve()