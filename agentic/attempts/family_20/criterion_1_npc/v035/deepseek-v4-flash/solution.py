import sys
sys.setrecursionlimit(10000000)

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    adj = [[] for _ in range(n)]
    for idx in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append((v, idx))
        adj[v].append((u, idx))
    
    color = [-1] * m
    
    # For each vertex, track which colors are used on incident edges
    used_at_vertex = [set() for _ in range(n)]
    
    # MRV heuristic: pick uncolored edge with fewest available colors
    def get_candidates(eidx):
        u, v = edges[eidx]
        used = used_at_vertex[u] | used_at_vertex[v]
        return [c for c in (1,2,3) if c not in used]
    
    def dfs(count):
        if count == m:
            return True
        # Find edge with fewest candidates
        best_e = -1
        best_cands = None
        for i in range(m):
            if color[i] == -1:
                cands = get_candidates(i)
                if not cands:
                    return False
                if best_e == -1 or len(cands) < len(best_cands):
                    best_e = i
                    best_cands = cands
                    if len(cands) == 1:
                        break
        eidx = best_e
        u, v = edges[eidx]
        for c in best_cands:
            # assign
            color[eidx] = c
            used_at_vertex[u].add(c)
            used_at_vertex[v].add(c)
            if dfs(count + 1):
                return True
            # backtrack
            used_at_vertex[u].remove(c)
            used_at_vertex[v].remove(c)
            color[eidx] = -1
        return False
    
    if dfs(0):
        print("YES")
        print(" ".join(str(color[i]) for i in range(m)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()