import sys

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].add(v)
        adj[v].add(u)
    
    for a in range(1, n + 1):
        neighbors_a = sorted(x for x in adj[a] if x > a)
        for b in neighbors_a:
            adj_b = adj[b]
            min_c = n + 1
            for c in neighbors_a:
                if c > b and c in adj_b:
                    if c < min_c:
                        min_c = c
            if min_c <= n:
                print(f"{a} {b} {min_c}")
                return
    
    # Should not reach here per problem guarantee
    print("-1 -1 -1")

main()