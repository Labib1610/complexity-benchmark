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

    color = [0] * n

    def dfs(node):
        if node == n:
            return True
        # Try colors 1, 2, 3
        for c in (1, 2, 3):
            ok = True
            for nei in range(n):
                if (adj[node] >> nei) & 1 and color[nei] == c:
                    ok = False
                    break
            if ok:
                color[node] = c
                if dfs(node + 1):
                    return True
                color[node] = 0
        return False

    if dfs(0):
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()