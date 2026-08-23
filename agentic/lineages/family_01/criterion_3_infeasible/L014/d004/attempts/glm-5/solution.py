import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)
    
    # Iterate to find lexicographically smallest triangle
    for a in range(1, n - 1):
        neighbors_a = adj[a]
        # We need b > a and c > b
        # Convert to list to iterate in order? 
        # Iterating over the set is fine, we just need to check existence.
        # To ensure we find the lex smallest, we can iterate b from a+1 to n
        # and check if b is in neighbors_a.
        for b in range(a + 1, n):
            if b in neighbors_a:
                neighbors_b = adj[b]
                # Check for c > b such that c is connected to both a and b
                for c in range(b + 1, n + 1):
                    if c in neighbors_a and c in neighbors_b:
                        print(a, b, c)
                        return

if __name__ == '__main__':
    solve()