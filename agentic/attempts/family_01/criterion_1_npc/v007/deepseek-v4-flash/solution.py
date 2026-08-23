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
    
    color = [0] * n  # 0 = unassigned, 1,2,3
    
    # Precompute neighbors for speed
    adj_set = [set(adj[i]) for i in range(n)]
    
    def backtrack(idx):
        if idx == n:
            return True
        # Try colors in order 1,2,3
        for c in (1,2,3):
            # Check conflict: if c == 1, no neighbor can be 1
            ok = True
            if c == 1:
                for nb in adj[idx]:
                    if color[nb] == 1:
                        ok = False
                        break
            # Also if neighbor is 1, we cannot be 1 (already covered)
            # No other restrictions
            if ok:
                color[idx] = c
                if backtrack(idx + 1):
                    return True
                color[idx] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()