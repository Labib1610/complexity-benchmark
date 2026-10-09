import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)
    
    # Greedy approach: repeatedly remove the vertex with highest degree
    remaining = set(range(1, n + 1))
    
    while len(remaining) > k:
        # Find vertex with maximum degree in remaining subgraph
        max_deg = -1
        max_v = -1
        for v in remaining:
            deg = len(adj[v] & remaining)
            if deg > max_deg:
                max_deg = deg
                max_v = v
        remaining.remove(max_v)
    
    # Check if remaining set is an independent set
    for v in remaining:
        if adj[v] & remaining:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, sorted(remaining))))

if __name__ == "__main__":
    solve()