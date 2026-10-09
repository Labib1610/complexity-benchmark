import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort adjacency lists to iterate neighbors in order.
    # This ensures we find the lexicographically smallest triangle.
    sorted_adj = [sorted(s) for s in adj]
    
    # Iterate through all possible triangles (a, b, c) with a < b < c.
    # We check if (a,b), (a,c), (b,c) are all edges.
    # Since we iterate a from 1 to n, b from a+1 to n, etc.,
    # the first valid triangle found is the lexicographically smallest.
    
    for a in range(1, n + 1):
        # For each neighbor b of a such that b > a
        for b in sorted_adj[a]:
            if b <= a:
                continue
            # For each neighbor c of a such that c > b
            for c in sorted_adj[a]:
                if c <= b:
                    continue
                # Check if edge (b, c) exists
                if c in adj[b]:
                    print(a, b, c)
                    return

if __name__ == '__main__':
    solve()