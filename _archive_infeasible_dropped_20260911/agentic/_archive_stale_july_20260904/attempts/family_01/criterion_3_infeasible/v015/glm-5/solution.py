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
    
    # Iterate to find the lexicographically smallest triad
    for a in range(1, n + 1):
        neighbors_a = adj[a]
        # We need to find b and c in neighbors_a such that b < c and c is in adj[b]
        # To find the lexicographically smallest (a, b, c), we iterate b in increasing order.
        # We can convert the set to a sorted list to iterate in order.
        # However, sorting takes O(d log d) where d is degree.
        # Sum of degrees is 2m. Total sorting time is O(sum(d log d)).
        # In worst case (dense graph), d ~ n, so O(n * n log n) which might be slow for n=2000.
        # But n=2000, n^2 log n is roughly 2000^2 * 11 ~ 44,000,000 ops, acceptable in Python.
        
        sorted_neighbors = sorted(neighbors_a)
        for b in sorted_neighbors:
            if b < a:
                continue
            # Check if any c exists such that c > b and c in adj[b]
            for c in sorted_neighbors:
                if c > b:
                    # Check if edge exists between b and c
                    if c in adj[b]:
                        print(a, b, c)
                        return

if __name__ == '__main__':
    solve()