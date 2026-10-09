import sys
from collections import deque

def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    it = iter(input)
    q = int(next(it))
    t = int(next(it))
    
    # Graph: nodes 1 to 2q, edges are calibrated pairs
    # Partition: Left = 1..q, Right = q+1..2q
    adj = [[] for _ in range(2*q + 1)]
    for _ in range(t):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    # Check degree condition first (necessary for Hall's theorem)
    for u in range(1, q+1):
        if not adj[u]:
            print("NO")
            return
    
    # Hopcroft-Karp for maximum matching in bipartite graph
    # Left: 1..q, Right: q+1..2q
    n_left = q
    n_right = q
    
    pair_U = [0] * (n_left + 1)  # pair_U[u] = v matched to u (left side)
    pair_V = [0] * (n_right + 1)  # pair_V[v] = u matched to v (right side, indexed v-q)
    dist = [0] * (n_left + 1)
    
    NIL = 0
    
    def bfs():
        queue = deque()
        for u in range(1, n_left + 1):
            if pair_U[u] == NIL:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        dist[NIL] = float('inf')
        
        while queue:
            u = queue.popleft()
            if dist[u] < dist[NIL]:
                for v in adj[u]:
                    v_idx = v - q  # Convert to 1-indexed right side
                    if pair_V[v_idx] != 0 and dist[pair_V[v_idx]] == float('inf'):
                        dist[pair_V[v_idx]] = dist[u] + 1
                        queue.append(pair_V[v_idx])
                    elif pair_V[v_idx] == 0:
                        dist[NIL] = dist[u] + 1
        return dist[NIL] != float('inf')
    
    def dfs(u):
        if u != NIL:
            for v in adj[u]:
                v_idx = v - q
                if pair_V[v_idx] == 0 or (dist[pair_V[v_idx]] == dist[u] + 1 and dfs(pair_V[v_idx])):
                    pair_U[u] = v
                    pair_V[v_idx] = u
                    return True
            dist[u] = float('inf')
            return False
        return True
    
    matching = 0
    while bfs():
        for u in range(1, n_left + 1):
            if pair_U[u] == NIL:
                if dfs(u):
                    matching += 1
    
    if matching != q:
        print("NO")
    else:
        print("YES")
        for u in range(1, q + 1):
            print(u, pair_U[u])

if __name__ == '__main__':
    solve()