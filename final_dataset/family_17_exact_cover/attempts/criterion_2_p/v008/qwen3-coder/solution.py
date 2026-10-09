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
            
        # Build bipartite graph
        # Left side: controllers 1 to q
        # Right side: platforms q+1 to 2q
        graph = defaultdict(list)
        adj = defaultdict(list)
        
        for _ in range(t):
            a, b = map(int, sys.stdin.readline().split())
            adj[a].append(b)
            adj[b].append(a)
        
        # Hopcroft-Karp implementation for maximum matching
        pair_u = {}
        pair_v = {}
        dist = {}
        
        def bfs():
            queue = deque()
            for u in range(1, q + 1):
                if pair_u.get(u) is None:
                    dist[u] = 0
                    queue.append(u)
                else:
                    dist[u] = float('inf')
            dist[None] = float('inf')
            
            while queue:
                u = queue.popleft()
                if dist[u] < dist[None]:
                    for v in adj[u]:
                        if dist.get(pair_v.get(v)) == float('inf'):
                            dist[pair_v.get(v)] = dist[u] + 1
                            queue.append(pair_v.get(v))
            return dist[None] != float('inf')
        
        def dfs(u):
            if u is not None:
                for v in adj[u]:
                    if dist.get(pair_v.get(v)) == dist[u] + 1:
                        if dfs(pair_v.get(v)):
                            pair_v[v] = u
                            pair_u[u] = v
                            return True
                dist[u] = float('inf')
                return False
            return True
        
        # Initialize
        for u in range(1, q + 1):
            pair_u[u] = None
        for v in range(q + 1, 2 * q + 1):
            pair_v[v] = None
        
        matching = 0
        while bfs():
            for u in range(1, q + 1):
                if pair_u.get(u) is None:
                    if dfs(u):
                        matching += 1
        
        if matching == q:
            print("YES")
            for u in range(1, q + 1):
                if u in pair_u and pair_u[u] is not None:
                    print(u, pair_u[u])
        else:
            print("NO")
    
    threading.Thread(target=main).start()

solve()