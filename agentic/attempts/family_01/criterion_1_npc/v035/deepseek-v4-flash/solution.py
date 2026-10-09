import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)

    # Try to assign shifts 1,2,3
    assignment = [0] * n

    # Backtracking with pruning
    def dfs(idx):
        if idx == n:
            return True
        # Try colors 1,2,3
        for color in (1, 2, 3):
            ok = True
            # Check conflicts with already assigned neighbors
            for j in range(n):
                if (adj[idx] >> j) & 1 and assignment[j] == color:
                    ok = False
                    break
            if ok:
                assignment[idx] = color
                if dfs(idx + 1):
                    return True
                assignment[idx] = 0
        return False

    if dfs(0):
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()