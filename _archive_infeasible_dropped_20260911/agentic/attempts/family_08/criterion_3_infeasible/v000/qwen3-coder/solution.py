import sys
from collections import defaultdict

def main():
    import sys
    import threading

    def solve():
        n, m, k = map(int, sys.stdin.readline().split())
        edges = []
        adj = [set() for _ in range(n + 1)]
        
        for _ in range(m):
            u, v = map(int, sys.stdin.readline().split())
            edges.append((u, v))
            adj[u].add(v)
            adj[v].add(u)
        
        # We need to find k+1 pairwise independent edges
        # Greedy approach: pick edges that don't share vertices with already picked ones
        
        selected = []
        used = [False] * (n + 1)
        
        for u, v in edges:
            if not used[u] and not used[v]:
                selected.append((u, v))
                used[u] = True
                used[v] = True
                
                if len(selected) == k + 1:
                    break
        
        for u, v in selected:
            print(u, v)

    threading.Thread(target=solve).start()

if __name__ == "__main__":
    main()