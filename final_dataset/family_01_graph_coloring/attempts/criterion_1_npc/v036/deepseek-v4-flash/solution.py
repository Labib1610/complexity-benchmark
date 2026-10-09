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
    
    color = [0] * n  # 0 = unassigned, 1,2,3 = rotations
    
    def backtrack(idx):
        if idx == n:
            return True
        # Try colors 1,2,3
        for c in (1, 2, 3):
            ok = True
            for nb in adj[idx]:
                if color[nb] == c:
                    ok = False
                    break
            if ok:
                color[idx] = c
                if backtrack(idx + 1):
                    return True
                color[idx] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(str(c) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    solve()