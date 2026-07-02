import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].add(v)
        adj[v].add(u)

    color = [0] * (n + 1)

    def backtrack(v):
        if v > n:
            return True
        for c in (1, 2, 3):
            if all(color[u] != c for u in adj[v]):
                color[v] = c
                if backtrack(v + 1):
                    return True
                color[v] = 0
        return False

    if backtrack(1):
        print("YES")
        print(*color[1:n + 1])
    else:
        print("NO")

solve()
