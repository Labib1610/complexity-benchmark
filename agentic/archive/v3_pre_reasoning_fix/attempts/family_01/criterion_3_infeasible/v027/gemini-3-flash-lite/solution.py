import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use an adjacency list and adjacency sets for O(1) lookup
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
        
    # Convert sets to sorted lists to optimize iteration
    adj_list = [sorted(list(s)) for s in adj]
    
    # We need the lexicographically smallest triple (a, b, c) with a < b < c
    # Iterate through a from 1 to n-2
    for a in range(1, n + 1):
        # Only consider neighbors b of a such that b > a
        neighbors_a = [b for b in adj_list[a] if b > a]
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            # Now we need c > b such that c is neighbor of a AND c is neighbor of b
            # Iterate through neighbors of b that are > b
            neighbors_b = adj_list[b]
            for c in neighbors_b:
                if c > b:
                    if c in adj[a]:
                        print(f"{a} {b} {c}")
                        return

if __name__ == '__main__':
    solve()