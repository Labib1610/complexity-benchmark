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
        v = int(input_data[idx + 1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
        
    # To find the lexicographically smallest (a, b, c),
    # we iterate a from 1 to n, b from a+1 to n, c from b+1 to n.
    # To optimize:
    # 1. Iterate a from 1 to n.
    # 2. Iterate b in sorted(adj[a]) where b > a.
    # 3. Check if there exists c in adj[a] and adj[b] where c > b.
    
    # Pre-sort adjacency lists to ensure we find the lexicographical smallest first
    adj_list = [sorted(list(adj[i])) for i in range(n + 1)]
    
    for a in range(1, n + 1):
        neighbors_a = adj_list[a]
        for b in neighbors_a:
            if b <= a:
                continue
            
            # Find common neighbors c of a and b such that c > b
            # We can intersect the sets or just iterate
            # Since we want the smallest c, we iterate through sorted neighbors
            neighbors_b = adj[b]
            for c in neighbors_a:
                if c <= b:
                    continue
                if c in neighbors_b:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()