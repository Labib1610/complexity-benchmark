import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    edges = []
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # DP over subsets
    INF = 10**18
    dp = [[INF]*n for _ in range(1<<n)]
    parent = [[-1]*n for _ in range(1<<n)]
    
    # Precompute cost of adding a new node to a set
    # cost[mask][v] = sum of distances from v to nodes in mask if v placed at position len(mask)
    # But we need incremental cost when adding v at position k = popcount(mask)
    # We'll compute on the fly.
    
    for i in range(n):
        dp[1<<i][i] = 0
    
    for mask in range(1<<n):
        k = bin(mask).count('1')
        if k == 0:
            continue
        for last in range(n):
            if not (mask & (1<<last)):
                continue
            cur = dp[mask][last]
            if cur == INF:
                continue
            # try adding new node
            for nxt in range(n):
                if mask & (1<<nxt):
                    continue
                # cost of adding nxt at position k (0-indexed)
                add_cost = 0
                for u,v in edges:
                    if (u == nxt and (mask & (1<<v))) or (v == nxt and (mask & (1<<u))):
                        # distance = |pos(nxt) - pos(other)|
                        # pos(nxt) = k, pos(other) = position in mask
                        # We need positions of nodes in mask. We can store them? 
                        # Instead, we can compute distance as |k - pos_other|.
                        # But pos_other is not stored. We can store positions in dp state? 
                        # That would be too large.
                        # Alternative: compute cost incrementally using precomputed distances?
                        # We can precompute for each pair (a,b) the distance if we know their positions.
                        # But positions change.
                        # So we need to store positions in state -> too large.
                        pass
                # This approach is not feasible without storing positions.
    
    # Since DP over subsets with positions is too heavy, we use a different approach:
    # Use a greedy + local search heuristic.
    
    # Greedy: place highest-degree nodes in the middle.
    order = sorted(range(n), key=lambda x: -len(adj[x]))
    pos = [0]*n
    # Place them: first in middle, then expand outward
    left = n//2 - 1
    right = n//2
    # Actually simpler: place in order of degree, alternating sides from center
    placement = [0]*n
    l = n//2 - 1
    r = n//2
    turn = 0
    for node in order:
        if turn == 0:
            if r < n:
                placement[node] = r
                r += 1
            else:
                placement[node] = l
                l -= 1
        else:
            if l >= 0:
                placement[node] = l
                l -= 1
            else:
                placement[node] = r
                r += 1
        turn ^= 1
    
    # Compute cost
    def cost(place):
        total = 0
        for u,v in edges:
            total += abs(place[u] - place[v])
        return total
    
    cur_cost = cost(placement)
    
    # Local search: try swapping pairs to reduce cost
    improved = True
    while improved:
        improved = False
        for i in range(n):
            for j in range(i+1, n):
                # swap
                placement[i], placement[j] = placement[j], placement[i]
                new_cost = cost(placement)
                if new_cost < cur_cost:
                    cur_cost = new_cost
                    improved = True
                else:
                    placement[i], placement[j] = placement[j], placement[i]
    
    if cur_cost <= B:
        # output positions 1-indexed
        ans = [0]*n
        for mod in range(n):
            ans[mod] = placement[mod] + 1
        print("YES")
        print(" ".join(map(str, ans)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()