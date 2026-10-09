import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        q = int(next(iterator))
        t = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(q + 1)]
    links = []
    for _ in range(t):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        links.append((u, v))

    # We need to find a perfect matching in a bipartite graph
    # Left side: controllers 1..q
    # Right side: platforms q+1..2q (remapped to 1..q)
    
    # Hopcroft-Karp algorithm
    pair_U = [0] * (q + 1)
    pair_V = [0] * (q + 1)
    dist = [0] * (q + 1)
    NIL = 0
    
    def bfs():
        queue = deque()
        for u in range(1, q + 1):
            if pair_U[u] == NIL:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        dist[NIL] = float('inf')
        
        while queue:
            u = queue.popleft()
            if dist[u] < dist[NIL]:
                for v_raw in adj[u]:
                    v = v_raw - q
                    if dist[pair_V[v]] == float('inf'):
                        dist[pair_V[v]] = dist[u] + 1
                        queue.append(pair_V[v])
        return dist[NIL] != float('inf')

    def dfs(u):
        if u != NIL:
            for v_raw in adj[u]:
                v = v_raw - q
                if dist[pair_V[v]] == dist[u] + 1:
                    if dfs(pair_V[v]):
                        pair_V[v] = u
                        pair_U[u] = v_raw
                        return True
            dist[u] = float('inf')
            return False
        return True

    matching = 0
    while bfs():
        for u in range(1, q + 1):
            if pair_U[u] == NIL:
                if dfs(u):
                    matching += 1
    
    if matching == q:
        print("YES")
        # Output the links corresponding to the matching
        # We iterate through the original links to find which ones were selected
        # pair_U[u] stores the platform v matched to controller u
        # We can construct a set of selected edges for efficient checking
        selected_edges = set()
        for u in range(1, q + 1):
            if pair_U[u] != 0:
                selected_edges.add((u, pair_U[u]))
        
        for u, v in links:
            if (u, v) in selected_edges:
                print(u, v)
    else:
        print("NO")

if __name__ == '__main__':
    solve()