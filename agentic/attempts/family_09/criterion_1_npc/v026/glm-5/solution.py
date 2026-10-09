import sys
input = sys.stdin.readline

def solve():
    n, m, k = map(int, input().split())
    
    # Build adjacency list
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].add(v)
        adj[v].add(u)
    
    # Greedy selection: repeatedly pick vertex with minimum degree
    remaining = set(range(1, n + 1))
    
    while len(remaining) > k:
        # Find vertex with minimum degree in the induced subgraph
        min_deg = n + 1
        min_v = -1
        for v in remaining:
            deg = len(adj[v] & remaining)
            if deg < min_deg:
                min_deg = deg
                min_v = v
                if min_deg == 0:
                    break
        
        if min_deg >= k:
            # All remaining vertices have degree >= k
            # This means no independent set of size k exists
            print("NO")
            return
        
        remaining.remove(min_v)
    
    # Verify the remaining set is an independent set
    remaining_list = list(remaining)
    for i in range(len(remaining_list)):
        for j in range(i + 1, len(remaining_list)):
            u, v = remaining_list[i], remaining_list[j]
            if v in adj[u]:
                print("NO")
                return
    
    print("YES")
    print(' '.join(map(str, remaining_list)))

solve()