import sys

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Sort adjacency lists and create sets for fast lookup
    adj_set = [None] * (n + 1)
    for i in range(1, n + 1):
        adj[i].sort()
        adj_set[i] = set(adj[i])
    
    for a in range(1, n + 1):
        sa = adj_set[a]
        for b in adj[a]:
            if b <= a:
                continue
            sb = adj_set[b]
            # Find smallest c > b in both sa and sb
            # Iterate through adj[a] (sorted) for c > b
            for c in adj[a]:
                if c <= b:
                    continue
                if c in sb:
                    print(a, b, c)
                    return
    
    # Should never reach here per problem guarantee
    print(-1)

main()