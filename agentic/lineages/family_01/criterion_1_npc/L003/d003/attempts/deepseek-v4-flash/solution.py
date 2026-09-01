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
    
    # Precompute conflict masks for each worker
    conflict_mask = [0] * n
    for i in range(n):
        mask = 0
        for j in adj[i]:
            mask |= (1 << j)
        conflict_mask[i] = mask
    
    # We'll store assignment as list of ints 0,1,2 (shift-1)
    assignment = [-1] * n
    
    # DFS with backtracking
    def dfs(idx):
        if idx == n:
            return True
        # Try shifts 1,2,3 (0,1,2 internally)
        for shift in range(3):
            # Check conflicts with already assigned
            ok = True
            for j in adj[idx]:
                if assignment[j] == shift:
                    ok = False
                    break
            if ok:
                assignment[idx] = shift
                if dfs(idx + 1):
                    return True
                assignment[idx] = -1
        return False
    
    if dfs(0):
        print("YES")
        print(" ".join(str(x + 1) for x in assignment))
    else:
        print("NO")

if __name__ == "__main__":
    solve()