import sys
from itertools import permutations

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    edges = []
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # Try brute force for small n
    if n <= 8:
        best_perm = None
        best_cost = float('inf')
        for perm in permutations(range(n)):
            pos = [0]*n
            for idx, node in enumerate(perm):
                pos[node] = idx+1
            cost = sum(abs(pos[u]-pos[v]) for u,v in edges)
            if cost <= k:
                print("YES")
                print(" ".join(str(pos[i]) for i in range(n)))
                return
        print("NO")
        return
    
    # Greedy: place high-degree nodes in middle
    deg = [len(adj[i]) for i in range(n)]
    order = sorted(range(n), key=lambda x: -deg[x])
    pos = [0]*n
    used = [False]*(n+1)
    # Place first node in middle
    mid = (n+1)//2
    pos[order[0]] = mid
    used[mid] = True
    left = mid-1
    right = mid+1
    for node in order[1:]:
        # place near already placed neighbors if possible
        placed = False
        for nb in adj[node]:
            if pos[nb] != 0:
                # try left or right of that neighbor
                for cand in (pos[nb]-1, pos[nb]+1):
                    if 1 <= cand <= n and not used[cand]:
                        pos[node] = cand
                        used[cand] = True
                        placed = True
                        break
                if placed:
                    break
        if not placed:
            # place at nearest free slot from middle
            for cand in range(mid, 0, -1):
                if not used[cand]:
                    pos[node] = cand
                    used[cand] = True
                    break
            else:
                for cand in range(mid+1, n+1):
                    if not used[cand]:
                        pos[node] = cand
                        used[cand] = True
                        break
    
    cost = sum(abs(pos[u]-pos[v]) for u,v in edges)
    if cost <= k:
        print("YES")
        print(" ".join(str(pos[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()