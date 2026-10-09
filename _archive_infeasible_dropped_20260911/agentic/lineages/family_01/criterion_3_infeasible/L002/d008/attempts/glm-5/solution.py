import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj_set = [set() for _ in range(n+1)]
    adj_list = [[] for _ in range(n+1)]
    
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj_set[u].add(v)
        adj_set[v].add(u)
    
    for u in range(1, n+1):
        adj_list[u] = sorted(x for x in adj_set[u] if x > u)
    
    best = None
    # For each u, for each v in adj_list[u], find smallest w in adj_list[u] with w > v and w in adj_set[v]
    for u in range(1, n+1):
        nu = adj_list[u]
        for i in range(len(nu)):
            v = nu[i]
            for j in range(i+1, len(nu)):
                w = nu[j]
                if w in adj_set[v]:
                    if best is None or (u, v, w) < best:
                        best = (u, v, w)
                        # Since we iterate in order, first found for this u,v is smallest w
                        # and we iterate u ascending, v ascending
                        # So first found overall is lex smallest
                        print(u, v, w)
                        return
    
    # Should not reach here per problem guarantee
    if best:
        print(best[0], best[1], best[2])

solve()