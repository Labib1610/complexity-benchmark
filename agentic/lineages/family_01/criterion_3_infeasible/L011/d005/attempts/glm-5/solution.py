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
    
    best_a, best_b, best_c = n + 1, n + 1, n + 1
    
    # Iterate over all pairs (a, b) with a < b
    for a in range(1, n + 1):
        for b in adj[a]:
            if b <= a:
                continue
            # Find common neighbors c such that c > b
            # Iterate over the smaller set for efficiency
            if len(adj[a]) < len(adj[b]):
                common = adj[a]
            else:
                common = adj[b]
            
            for c in common:
                if c > b:
                    # Check if c is connected to both a and b
                    # Since c is in common, it's connected to both
                    # We found a triangle (a, b, c)
                    if c < best_c or (c == best_c and (a < best_a or (a == best_a and b < best_b))):
                        best_a, best_b, best_c = a, b, c
    
    print(best_a, best_b, best_c)

if __name__ == "__main__":
    solve()