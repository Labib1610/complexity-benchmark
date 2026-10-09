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

    colors = [0] * n

    def valid(v, c):
        for u in adj[v]:
            if colors[u] == c:
                return False
        return True

    def backtrack(v):
        if v == n:
            return True
        for c in range(1, 4):
            if valid(v, c):
                colors[v] = c
                if backtrack(v + 1):
                    return True
                colors[v] = 0
        return False

    if backtrack(0):
        print("YES")
        print(" ".join(map(str, colors)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()