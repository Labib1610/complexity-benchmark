import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))

    # Build adjacency list for cores (1 to q)
    adj = [[] for _ in range(q + 1)]
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)

    # We use Hopcroft-Karp algorithm for maximum bipartite matching
    # Cores: 1..q, Dissipators: q+1..2q
    # We map dissipators to 0..q-1 for array indexing
    
    pair_u = [0] * (q + 1)  # pair_u[u] = v matched with u
    pair_v = [0] * (q + 1)  # pair_v[v] = u matched with v (v is mapped index)
    dist = [0] * (q + 1)
    
    def bfs():
        queue = deque()
        for u in range(1, q + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        dist[0] = float('inf')
        
        while queue:
            u = queue.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    # v is actual dissipator index, mapped is v - q
                    mapped_v = v - q
                    u_pair = pair_v[mapped_v]
                    if dist[u_pair] == float('inf'):
                        dist[u_pair] = dist[u] + 1
                        queue.append(u_pair)
        return dist[0] != float('inf')

    def dfs(u):
        if u != 0:
            for v in adj[u]:
                mapped_v = v - q
                if dist[pair_v[mapped_v]] == dist[u] + 1:
                    if dfs(pair_v[mapped_v]):
                        pair_v[mapped_v] = u
                        pair_u[u] = v
                        return True
            dist[u] = float('inf')
            return False
        return True

    matching = 0
    while bfs():
        for u in range(1, q + 1):
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching == q:
        sys.stdout.write("YES\n")
        for u in range(1, q + 1):
            sys.stdout.write(f"{u} {pair_u[u]}\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == '__main__':
    solve()