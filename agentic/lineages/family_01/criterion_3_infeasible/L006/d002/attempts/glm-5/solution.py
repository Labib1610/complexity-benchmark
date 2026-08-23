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
    
    # Iterate to find lexicographically smallest triangle
    for a in range(1, n + 1):
        neighbors = adj[a]
        # Convert to list to allow indexing, though iteration is fine
        # We need to check pairs (b, c) in neighbors such that b < c and b-c is an edge
        # To find lex smallest, we iterate b in increasing order
        sorted_neighbors = sorted(neighbors)
        len_neighbors = len(sorted_neighbors)
        
        for i in range(len_neighbors):
            b = sorted_neighbors[i]
            if b < a: 
                continue
            
            # For fixed a, b, we need smallest c > b such that c in neighbors and b-c is edge
            # Iterate c candidates from neighbors that are > b
            for j in range(i + 1, len_neighbors):
                c = sorted_neighbors[j]
                # c > b is guaranteed by sorted iteration
                if c in adj[b]:
                    print(a, b, c)
                    return

if __name__ == '__main__':
    solve()