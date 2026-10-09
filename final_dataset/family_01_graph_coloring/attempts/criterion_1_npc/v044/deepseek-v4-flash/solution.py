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

    def backtrack(node):
        if node == n:
            return True
        # Try colors 1, 2, 3
        for c in (1, 2, 3):
            ok = True
            for nb in adj[node]:
                if color[nb] == c:
                    ok = False
                    break
            if ok:
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = -1
        return False

    if backtrack(0):
        print("YES")
        print(" ".join(str(color[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()