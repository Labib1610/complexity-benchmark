import sys

def solve():
    # Use fast I/O
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
        v = int(input_data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
        
    # To find the lexicographically smallest (a, b, c) with a < b < c
    # We iterate through all possible 'a' from 1 to n
    # Then iterate through neighbors 'b' of 'a' where b > a
    # Check if there exists 'c' such that c > b and (c in adj[a] and c in adj[b])
    
    # Sort neighbors for each node to ensure we check in lexicographical order
    adj_sorted = [sorted(list(s)) for s in adj]
    
    for a in range(1, n + 1):
        neighbors_a = adj_sorted[a]
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            if b <= a:
                continue
            
            # We want to find smallest c > b such that c is in adj[a] and c in adj[b]
            # Since both adj lists are sorted, we can intersect them
            # or just iterate through smaller list
            
            # Optimization: check intersection of neighbors_a[i+1:] and neighbors_b
            # Since we need the smallest c, we iterate through neighbors_a
            for j in range(i + 1, len(neighbors_a)):
                c = neighbors_a[j]
                if c > b and c in adj[b]:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()