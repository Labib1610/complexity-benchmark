import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Adjacency list as sets for O(1) lookup
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
        
    # Convert sets to sorted lists to iterate in order
    adj_sorted = [sorted(list(adj[i])) for i in range(n + 1)]
    
    # We want the lexicographically smallest triple (a, b, c) with a < b < c
    # Iterate a from 1 to n
    for a in range(1, n + 1):
        neighbors_a = adj_sorted[a]
        # Iterate b in neighbors of a
        for b in neighbors_a:
            if b <= a:
                continue
            
            # We need to find c such that c is in adj[a] and adj[b] and c > b
            # Use intersection to find common neighbors
            # To optimize, iterate through the smaller adjacency list
            if len(adj[a]) < len(adj[b]):
                for c in adj[a]:
                    if c > b and c in adj[b]:
                        print(f"{a} {b} {c}")
                        return
            else:
                for c in adj[b]:
                    if c > b and c in adj[a]:
                        print(f"{a} {b} {c}")
                        return

if __name__ == '__main__':
    solve()