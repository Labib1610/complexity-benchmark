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

    color = [-1] * n

    # Try to assign colors 0,1,2 (representing states 1,2,3)
    # Use backtracking with pruning
    def backtrack(idx):
        if idx == n:
            return True
        # Try colors 0,1,2
        for c in range(3):
            ok = True
            for nb in adj[idx]:
                if color[nb] == c:
                    ok = False
                    break
            if ok:
                color[idx] = c
                if backtrack(idx + 1):
                    return True
                color[idx] = -1
        return False

    if backtrack(0):
        print("YES")
        print(" ".join(str(c + 1) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    solve()