import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Adjacency list using sets for O(1) average lookup
    adj = [set() for _ in range(n + 1)]
    # Adjacency list using sorted lists for lexicographical iteration
    adj_list = [[] for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
        
    for i in range(1, n + 1):
        adj_list[i] = sorted(list(adj[i]))

    # To find the lexicographically smallest triple (a, b, c) with a < b < c:
    # We iterate a from 1 to n, then b from adj_list[a] where b > a,
    # then check if any c in adj_list[b] where c > b is also in adj[a].
    # However, to optimize, we can check the smaller of the two neighborhoods.
    
    for a in range(1, n + 1):
        # We only care about neighbors b > a
        neighbors_a = [v for v in adj_list[a] if v > a]
        
        for b in neighbors_a:
            # We need to find c such that c > b and c is a neighbor of both a and b.
            # To keep it lexicographical, we check neighbors of b that are > b.
            # Since we want the smallest c, we iterate through adj_list[b].
            for c in adj_list[b]:
                if c <= b:
                    continue
                if c in adj[a]:
                    print(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()