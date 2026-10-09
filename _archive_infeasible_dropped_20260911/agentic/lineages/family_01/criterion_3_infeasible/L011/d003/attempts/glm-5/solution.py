import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort adjacency lists for deterministic iteration order
    adj_lists = [sorted(s) for s in adj]
    
    # Iterate through all triples a < b < c
    for a in range(1, n - 1):
        for b in adj_lists[a]:
            if b <= a:
                continue
            # Check if a and b are connected (they are, since b is in adj[a])
            # Now iterate c > b
            # We can iterate over intersection of adj[a] and adj[b] where c > b
            # But simpler: iterate c from b+1 to n
            # To optimize, iterate over the smaller set
            set_a = adj[a]
            set_b = adj[b]
            
            # Iterate over potential c in adj[a] (since c must be connected to a)
            for c in adj_lists[a]:
                if c <= b:
                    continue
                if c in set_b:
                    print(a, b, c)
                    return
    
    # Fallback (should not reach due to guarantee)
    print("")

if __name__ == "__main__":
    solve()