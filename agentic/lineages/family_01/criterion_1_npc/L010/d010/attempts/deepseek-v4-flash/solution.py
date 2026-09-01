import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * n  # 0 = uncolored, colors 1,2,3
    
    # Precompute adjacency sets for fast checking
    adj_set = [set(adj[i]) for i in range(n)]
    
    # Sort vertices by degree descending for better pruning
    order = sorted(range(n), key=lambda x: -len(adj[x]))
    pos = [0] * n
    for idx, v in enumerate(order):
        pos[v] = idx
    
    def backtrack(idx):
        if idx == n:
            return True
        v = order[idx]
        used = set()
        for nb in adj_set[v]:
            if color[nb] != 0:
                used.add(color[nb])
        for c in (1, 2, 3):
            if c not in used:
                color[v] = c
                if backtrack(idx + 1):
                    return True
                color[v] = 0
        return False
    
    # Try to get lexicographically smallest by assigning from 1..n
    # But backtracking order above is not lexicographic; we do a custom DFS
    # Let's instead do DFS by variable index 0..n-1 for lexicographic order.

    def dfs_lex(i):
        if i == n:
            return True
        for c in (1, 2, 3):
            # check neighbors
            ok = True
            for nb in adj_set[i]:
                if color[nb] == c:
                    ok = False
                    break
            if ok:
                color[i] = c
                if dfs_lex(i + 1):
                    return True
                color[i] = 0
        return False
    
    if dfs_lex(0):
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()