import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
        
    # To find lexicographically smallest triplet (a, b, c) with a < b < c:
    # Iterate a from 1 to n-2
    # Iterate b in sorted(adj[a]) such that b > a
    # Check if there exists c in adj[a] and adj[b] such that c > b
    
    # Pre-sort adjacency lists for efficient iteration and checking
    sorted_adj = [sorted(list(adj[i])) for i in range(n + 1)]
    
    for a in range(1, n + 1):
        neighbors_a = sorted_adj[a]
        # Optimization: only consider b > a
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            if b <= a:
                continue
            
            # Find common neighbors of a and b that are > b
            # Since both lists are sorted, we can use intersection
            # or just iterate through neighbors_a to find c > b
            # and check if c is in adj[b]
            
            # For efficiency, iterate over the smaller adjacency list
            if len(adj[a]) < len(adj[b]):
                for c in neighbors_a:
                    if c > b and c in adj[b]:
                        print(f"{a} {b} {c}")
                        return
            else:
                for c in sorted_adj[b]:
                    if c > b and c in adj[a]:
                        print(f"{a} {b} {c}")
                        return

solve()