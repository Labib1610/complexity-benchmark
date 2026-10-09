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
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
    
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    pos = [-1] * n
    used = [False] * (n + 1)
    best_sol = None

    def dfs(idx, cost):
        nonlocal best_sol
        if best_sol is not None:
            return
        if cost > B:
            return
        if idx == n:
            best_sol = pos[:]
            return
        
        # choose next exhibit to place: pick one with most placed neighbors
        # simple heuristic: pick first unplaced
        for i in range(n):
            if pos[i] == -1:
                break
        
        # Try positions for exhibit i
        for p in range(1, n + 1):
            if used[p]:
                continue
            # compute additional cost
            add = 0
            ok = True
            for nb in adj[i]:
                if pos[nb] != -1:
                    add += abs(pos[nb] - p)
                    if cost + add > B:
                        ok = False
                        break
            if not ok:
                continue
            pos[i] = p
            used[p] = True
            dfs(idx + 1, cost + add)
            if best_sol is not None:
                return
            used[p] = False
            pos[i] = -1

    dfs(0, 0)
    if best_sol is not None:
        print("YES")
        print(" ".join(str(x) for x in best_sol))
    else:
        print("NO")

if __name__ == "__main__":
    solve()