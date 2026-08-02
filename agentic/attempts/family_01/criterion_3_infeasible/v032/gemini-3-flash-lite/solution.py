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
        
    # To find the lexicographically smallest triple (a, b, c) with a < b < c,
    # we iterate through a from 1 to n-2, then b from a+1 to n-1, 
    # then check if there exists c > b such that c is in adj[a] and adj[b].
    
    # Pre-sort neighbors for faster intersection or just check existence
    # Since n <= 2000, O(n^2) or O(n^3/64) is fine.
    
    # Sort adjacency lists to potentially optimize
    adj_list = [sorted(list(adj[i])) for i in range(n + 1)]
    
    for a in range(1, n + 1):
        # Only consider neighbors b > a
        neighbors_a = [x for x in adj_list[a] if x > a]
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            # We need to find the smallest c > b such that c is in adj[a] and adj[b]
            # Since adj[a] and adj[b] are sorted, we can intersect them
            set_a = adj[a]
            set_b = adj[b]
            
            # Optimization: check the smaller adjacency list
            if len(set_a) < len(set_b):
                search_space = adj_list[a]
            else:
                search_space = adj_list[b]
                
            for c in search_space:
                if c > b:
                    if c in set_a and c in set_b:
                        print(f"{a} {b} {c}")
                        return

if __name__ == '__main__':
    solve()