import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort adjacency lists for each node
    adj_sorted = [sorted(s) for s in adj]
    
    # For each pair (a, b) with a < b, check if they are adjacent,
    # then find common neighbor c > b.
    # To find lexicographically smallest (a, b, c), iterate a from 1 to n,
    # b from a+1 to n, and find smallest c > b in both adj[a] and adj[b].
    
    for a in range(1, n + 1):
        adj_a = adj_sorted[a]
        # b must be > a and in adj_a
        for b in adj_a:
            if b <= a:
                continue
            # Find smallest c > b that is in both adj[a] and adj[b]
            adj_b = adj_sorted[b]
            # Merge-like intersection to find first c > b
            i, j = 0, 0
            la, lb = len(adj_a), len(adj_b)
            while i < la and j < lb:
                ca = adj_a[i]
                cb = adj_b[j]
                if ca == cb:
                    if ca > b:
                        print(a, b, ca)
                        return
                    i += 1
                    j += 1
                elif ca < cb:
                    i += 1
                else:
                    j += 1
    
    # Should not reach here per problem guarantee
    print(-1)

main()