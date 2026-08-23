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
    # Iterate b from a+1 to n-1
    # Check if b is connected to a
    # If so, find if there exists c > b such that c is in adj[a] and adj[b]
    
    # Sort adjacency lists to potentially speed up intersection
    sorted_adj = [sorted(list(adj[i])) for i in range(n + 1)]
    
    for a in range(1, n + 1):
        neighbors_a = sorted_adj[a]
        # Only consider b > a
        for b in neighbors_a:
            if b > a:
                # Find common neighbors c > b
                neighbors_b = adj[b]
                for c in neighbors_a:
                    if c > b and c in neighbors_b:
                        print(f"{a} {b} {c}")
                        return

if __name__ == '__main__':
    solve()