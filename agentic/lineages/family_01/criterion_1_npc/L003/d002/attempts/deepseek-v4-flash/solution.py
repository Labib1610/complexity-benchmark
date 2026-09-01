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
    
    color = [0] * n
    # Precompute conflict masks for each node
    conflict_mask = [0] * n
    for i in range(n):
        mask = 0
        for j in adj[i]:
            mask |= (1 << j)
        conflict_mask[i] = mask
    
    # Backtracking with pruning
    def dfs(idx):
        if idx == n:
            return True
        # Try colors 1,2,3 in order
        for c in (1, 2, 3):
            ok = True
            for nb in adj[idx]:
                if color[nb] == c:
                    ok = False
                    break
            if ok:
                color[idx] = c
                if dfs(idx + 1):
                    return True
                color[idx] = 0
        return False
    
    if dfs(0):
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()