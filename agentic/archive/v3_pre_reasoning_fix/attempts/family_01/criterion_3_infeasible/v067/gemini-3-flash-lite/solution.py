import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [set() for _ in range(n + 1)]
    edges = []
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].add(v)
        adj[v].add(u)
        edges.append((min(u, v), max(u, v)))
        idx += 2
        
    # To find the lexicographically smallest (a, b, c) with a < b < c,
    # we can iterate through all possible 'a' from 1 to n,
    # then iterate through all neighbors 'b' of 'a' such that b > a,
    # and check if there exists a 'c' such that c > b, 
    # c is in adj[a], and c is in adj[b].
    
    # Sort neighbors to ensure we find the lexicographically smallest (a, b, c)
    for i in range(1, n + 1):
        adj[i] = sorted(list(adj[i]))
        
    for a in range(1, n + 1):
        neighbors_a = adj[a]
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            if b <= a:
                continue
            
            # Now we need to find the smallest c > b such that c in adj[a] and c in adj[b]
            # Since both adj[a] and adj[b] are sorted, we can use two pointers 
            # or set intersection.
            # However, since we want the smallest c, we can iterate through 
            # the smaller neighbor list.
            
            set_b = set(adj[b])
            for c in neighbors_a:
                if c <= b:
                    continue
                if c in set_b:
                    print(f"{a} {b} {c}")
                    return

solve()