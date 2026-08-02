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
        
    # To find the lexicographically smallest (a, b, c) with a < b < c:
    # Iterate a from 1 to n-2
    #   Iterate b from a+1 to n-1
    #     If b is connected to a:
    #       Find common neighbors c of a and b such that c > b
    #       If found, the smallest such c will give the lexicographically smallest (a, b, c)
    
    # Pre-sort neighbors for faster intersection or just use set intersection
    for a in range(1, n + 1):
        # We need to find b > a such that a and b are connected
        # and there exists c > b such that c is connected to a and b.
        # To ensure lexicographical order, we must check 'a' then 'b' then 'c'.
        
        # Sort neighbors to iterate in order
        neighbors_a = sorted(list(adj[a]))
        for b in neighbors_a:
            if b <= a:
                continue
            
            # Find common neighbors of a and b that are > b
            # Intersection of adj[a] and adj[b]
            common = adj[a].intersection(adj[b])
            
            c_found = None
            for c in common:
                if c > b:
                    if c_found is None or c < c_found:
                        c_found = c
            
            if c_found is not None:
                print(f"{a} {b} {c_found}")
                return

if __name__ == '__main__':
    solve()