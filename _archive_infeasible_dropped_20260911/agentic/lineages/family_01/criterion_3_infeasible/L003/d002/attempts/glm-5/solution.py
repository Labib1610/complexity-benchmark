import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
    
    best = None
    for a in range(1, n + 1):
        if best is not None and a >= best[0]:
            break
        neighbors = adj[a]
        # We want b < c, both > a, both in neighbors, and edge (b,c) exists.
        # To get lexicographically smallest (a,b,c), iterate b in increasing order.
        sorted_neighbors = sorted(neighbors)
        # For each b, check if any c > b in neighbors with edge (b,c).
        # Optimize: only consider b > a.
        for b in sorted_neighbors:
            if b <= a:
                continue
            if best is not None and b >= best[1]:
                # Since a is fixed and < best[0], any valid b,c will be lexicographically smaller
                # than best regardless of b? Actually if a < best[0], then (a, b, c) < (best[0], best[1], best[2])
                # for any b,c. So we can break early once we find the first valid b.
                pass
            # Find smallest c > b such that c in neighbors and (b,c) is an edge.
            # Since we want lexicographically smallest, the first b that has any valid c gives the answer.
            # Among those c, pick the smallest.
            # Check intersection of adj[b] and neighbors (with c > b).
            # To optimize, iterate over the smaller set.
            adj_b = adj[b]
            # We need c in neighbors and c in adj_b and c > b.
            # Since neighbors are sorted, we can iterate.
            # But adj_b might be large. Let's pick the smaller set to iterate.
            if len(neighbors) <= len(adj_b):
                for c in sorted_neighbors:
                    if c > b and c in adj_b:
                        print(a, b, c)
                        return
            else:
                # iterate over adj_b, but we want smallest c > b in neighbors.
                # We can iterate over sorted_neighbors anyway since it's sorted and we break at first.
                for c in sorted_neighbors:
                    if c > b and c in adj_b:
                        print(a, b, c)
                        return
            # If we reach here, no valid c for this b. Continue to next b.
            # But wait: if a < best[0], the first valid (b,c) is the answer. 
            # However if best is None, we still need to find the first valid b.
            # The loop continues.
        # If we found nothing for this a, continue to next a.
        # But if best is not None and a >= best[0], we break at the top.
    
    # Fallback (should not happen given problem guarantees)
    if best:
        print(best[0], best[1], best[2])

solve()