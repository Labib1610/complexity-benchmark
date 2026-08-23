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
    
    # We need to find the lexicographically smallest triangle (a, b, c)
    # Iterate a from 1 to n, then b from a+1 to n, then c from b+1 to n
    # Check if (a,b), (a,c), (b,c) all exist
    
    # To speed up checking, we can iterate a, then for each neighbor b of a where b > a,
    # check if b has a neighbor c where c > b and c is also a neighbor of a
    
    for a in range(1, n + 1):
        neighbors_a = adj_lists[a]
        # We want b > a
        # Find index of first neighbor > a
        # Since neighbors_a is sorted, we can iterate
        for b in neighbors_a:
            if b <= a:
                continue
            # Now check if there exists c > b such that c is neighbor of both a and b
            neighbors_b = adj_lists[b]
            # Iterate through neighbors of b that are > b
            for c in neighbors_b:
                if c <= b:
                    continue
                if c in adj[a]:  # c is also neighbor of a
                    print(a, b, c)
                    return
    
    # Should never reach here given problem guarantees
    print(-1, -1, -1)

if __name__ == "__main__":
    solve()