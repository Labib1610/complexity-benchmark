import sys
from collections import defaultdict, deque

def solve():
    import sys
    import threading
    
    def main():
        import sys
        from collections import defaultdict, deque
        
        sys.setrecursionlimit(1 << 25)
        
        try:
            line = sys.stdin.readline()
            if not line:
                return
            q, t = map(int, line.split())
        except:
            return
            
        # Controllers: 1 to q
        # Platforms: q+1 to 2*q
        
        # Build bipartite graph
        # Left side: controllers (1 to q)
        # Right side: platforms (q+1 to 2*q) => map to 1 to q for easier handling
        graph = defaultdict(list)
        adj = defaultdict(list)
        
        for _ in range(t):
            line = sys.stdin.readline()
            if not line:
                continue
            a, b = map(int, line.split())
            adj[a].append(b)
            adj[b].append(a)
        
        # We need a maximum matching in bipartite graph
        # Use Hopcroft-Karp or similar. But since q can be 100000, we need efficiency.
        # Use optimized version of Hopcroft-Karp or use network flow with scaling.
        # For simplicity and correctness, use Hopcroft-Karp implementation.
        
        # Map platforms from [q+1, 2q] to [1, q] for matching purposes
        # So controller i (1 <= i <= q) can be matched with platform j (1 <= j <= q)
        # where original platform was j + q
        
        # Build graph for matching
        # Left = controllers (1 to q)
        # Right = platforms (1 to q) 
        left_adj = defaultdict(list)
        
        for u in range(1, q+1):
            for v in adj[u]:
                if v > q:  # It's a platform
                    right_index = v - q
                    left_adj[u].append(right_index)
        
        # Hopcroft-Karp implementation
        def bfs():
            queue = deque()
            for u in range(1, q+1):
                if pair_u[u] == 0:
                    dist[u] = 0
                    queue.append(u)
                else:
                    dist[u] = float('inf')
            dist[0] = float('inf')
            
            while queue:
                u = queue.popleft()
                if dist[u] < dist[0]:
                    for v in left_adj[u]:
                        if dist[pair_v[v]] == float('inf'):
                            dist[pair_v[v]] = dist[u] + 1
                            queue.append(pair_v[v])
            return dist[0] != float('inf')
        
        def dfs(u):
            if u != 0:
                for v in left_adj[u]:
                    if dist[pair_v[v]] == dist[u] + 1:
                        if dfs(pair_v[v]):
                            pair_v[v] = u
                            pair_u[u] = v
                            return True
                dist[u] = float('inf')
                return False
            return True
        
        # Initialize
        pair_u = [0] * (q + 1)  # pair_u[u] = v means u is matched to v
        pair_v = [0] * (q + 1)  # pair_v[v] = u means v is matched to u
        dist = [float('inf')] * (q + 1)
        
        matching = 0
        while bfs():
            for u in range(1, q+1):
                if pair_u[u] == 0:
                    if dfs(u):
                        matching += 1
        
        if matching == q:
            print("YES")
            for u in range(1, q+1):
                v_original = pair_u[u] + q
                print(u, v_original)
        else:
            print("NO")
    
    threading.Thread(target=main).start()

solve()