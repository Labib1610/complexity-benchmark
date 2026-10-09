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

    colors = [0] * n

    # Backtracking with pruning
    def dfs(node):
        if node == n:
            return True
        # Try colors 1,2,3
        for c in (1, 2, 3):
            ok = True
            # Check neighbors
            for v in range(n):
                if (adj[node] >> v) & 1:
                    if colors[v] == c:
                        ok = False
                        break
            if ok:
                colors[node] = c
                if dfs(node + 1):
                    return True
                colors[node] = 0
        return False

    if dfs(0):
        print("YES")
        print(" ".join(map(str, colors)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()