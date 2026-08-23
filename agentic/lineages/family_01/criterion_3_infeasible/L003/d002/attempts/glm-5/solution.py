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
    
    # Find lexicographically smallest triangle
    for a in range(1, n - 1):
        # Convert to list for iteration, but we need to check membership
        # We iterate through neighbors b > a
        neighbors_a = adj[a]
        # Create sorted list of neighbors greater than a
        neighbors_greater = [b for b in neighbors_a if b > a]
        neighbors_greater.sort()
        
        for b in neighbors_greater:
            # For each c > b, check if c is neighbor of both a and b
            neighbors_b = adj[b]
            # Check intersection of neighbors_a and neighbors_b for c > b
            # We iterate through the smaller set for efficiency
            if len(neighbors_a) < len(neighbors_b):
                smaller = neighbors_a
            else:
                smaller = neighbors_b
            
            for c in smaller:
                if c > b and c in neighbors_a and c in neighbors_b:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()