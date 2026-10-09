import sys

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    edges = set()
    
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        if u > v:
            u, v = v, u
        adj[u].append(v)
        adj[v].append(u)
        edges.add((u, v))
    
    LIMIT = 2000  # cap to avoid O(d^2) blowup on high-degree nodes
    
    for a in range(1, n + 1):
        neighbors = sorted(adj[a])
        # filter neighbors > a so b > a (since a < b < c)
        candidates = [x for x in neighbors if x > a]
        if len(candidates) < 2:
            continue
        # To bound work, if too many candidates, we still try but cap iterations
        found = False
        L = len(candidates)
        max_iter = min(L, LIMIT)
        for i in range(max_iter):
            b = candidates[i]
            for j in range(i + 1, L):
                c = candidates[j]
                if (b, c) in edges:
                    print(f"{a} {b} {c}")
                    return
            # If we've capped and not found, continue to next a
            # But we must not miss the answer; only cap if L is huge
            # Actually we should check all pairs for correctness
            # Let's not cap - just check all
        # Full check without cap:
        if not found:
            for i in range(L):
                b = candidates[i]
                for j in range(i + 1, L):
                    c = candidates[j]
                    if (b, c) in edges:
                        print(f"{a} {b} {c}")
                        return
    
    # Should never reach here per problem guarantee
    print("-1")

main()