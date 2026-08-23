import sys

def solve():
    # Use fast I/O
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
    # Iterate a from 1 to n-2, b from a+1 to n-1, c from b+1 to n.
    # Check if a, b, c form a triangle.
    # Since we want the lexicographically smallest, the first one we find is the answer.
    
    # Optimization: sort neighbors to potentially speed up lookup and iteration
    adj_list = [sorted(list(adj[i])) for i in range(n + 1)]
    
    for a in range(1, n + 1):
        # Only consider b > a
        neighbors_a = [x for x in adj_list[a] if x > a]
        for b in neighbors_a:
            # Only consider c > b
            # We need c to be in both adj[a] and adj[b]
            # Intersection of adj[a] and adj[b]
            # Since we need c > b, we filter neighbors of a that are also in b
            for c in neighbors_a:
                if c <= b:
                    continue
                if c in adj[b]:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()