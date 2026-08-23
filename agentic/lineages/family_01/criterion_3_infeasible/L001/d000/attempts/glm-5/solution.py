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
    
    # Find lexicographically smallest critical triad
    for a in range(1, n + 1):
        neighbors_a = adj[a]
        # Convert to sorted list for ordered iteration
        neighbors_list = sorted(neighbors_a)
        for b in neighbors_list:
            if b <= a:
                continue
            neighbors_b = adj[b]
            for c in neighbors_list:
                if c <= b:
                    continue
                if c in neighbors_b:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()