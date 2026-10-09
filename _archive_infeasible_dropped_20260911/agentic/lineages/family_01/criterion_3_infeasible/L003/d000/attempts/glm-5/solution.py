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
    
    # To find lexicographically smallest triple, iterate a from 1 to n
    for a in range(1, n + 1):
        neighbors_a = adj[a]
        # We need b and c in neighbors_a such that b < c and edge (b, c) exists
        # To get smallest (b, c), iterate b from a+1 to n
        for b in range(a + 1, n + 1):
            if b in neighbors_a:
                # Check for c in neighbors_a such that c > b and edge (b, c) exists
                # Iterate c from b+1 to n
                for c in range(b + 1, n + 1):
                    if c in neighbors_a and c in adj[b]:
                        print(a, b, c)
                        return

if __name__ == '__main__':
    solve()