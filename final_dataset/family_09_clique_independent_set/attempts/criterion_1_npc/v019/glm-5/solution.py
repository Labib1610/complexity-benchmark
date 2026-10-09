import sys

def solve():
    data = sys.read().split()
    if not data:
        return
    n = int(data[0]); m = int(data[1]); k = int(data[2])
    adj = [0]*(n+1)
    idx = 3
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        adj[u] |= 1<<v
        adj[v] |= 1<<u
    
    if k == 0:
        print("YES")
        print()
        return
    
    # Greedy: pick vertex with minimum degree in remaining graph
    chosen = []
    chosen_mask = 0
    remaining = [True]*(n+1)
    remaining_count = n
    
    for _ in range(k):
        best_v = -1
        best_deg = n+1
        for v in range(1, n+1):
            if not remaining[v]:
                continue
            deg = bin(adj[v] & chosen_mask).count('1')
            if deg > 0:
                continue
            # degree in remaining graph
            rem_deg = 0
            for u in range(1, n+1):
                if remaining[u] and u != v and (adj[v]>>u)&1:
                    rem_deg += 1
            if rem_deg < best_deg:
                best_deg = rem_deg
                best_v = v
        if best_v == -1:
            print("NO")
            return
        chosen.append(best_v)
        chosen_mask |= 1<<best_v
        remaining[best_v] = False
        remaining_count -= 1
    
    print("YES")
    print(' '.join(map(str, chosen)))

solve()