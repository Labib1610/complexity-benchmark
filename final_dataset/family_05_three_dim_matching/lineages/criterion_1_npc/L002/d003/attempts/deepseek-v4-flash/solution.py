import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    edges = []
    for _ in range(t):
        u, v, w = map(int, input().split())
        edges.append((u-1, v-1, w-1))
    
    # Group edges by u
    by_u = [[] for _ in range(k)]
    for idx, (u, v, w) in enumerate(edges):
        by_u[u].append((v, w, idx))
    
    # We'll do backtracking over u, tracking used v and w
    used_v = 0
    used_w = 0
    chosen = []
    
    # Precompute for each u, list of (v, w, edge_index)
    # Sort maybe not needed
    
    # Backtracking
    def dfs(u_idx, used_v, used_w, chosen):
        if u_idx == k:
            return len(chosen) == k
        # Try all edges from this u
        for v, w, idx in by_u[u_idx]:
            if (used_v >> v) & 1:
                continue
            if (used_w >> w) & 1:
                continue
            chosen.append(edges[idx])
            if dfs(u_idx + 1, used_v | (1 << v), used_w | (1 << w), chosen):
                return True
            chosen.pop()
        return False
    
    if dfs(0, 0, 0, []):
        print("YES")
        for u, v, w in chosen:
            print(u+1, v+1, w+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()