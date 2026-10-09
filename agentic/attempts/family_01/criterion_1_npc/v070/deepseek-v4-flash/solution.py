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

    def backtrack(node):
        if node == n:
            return True
        used = [False] * 4
        for nei in adj[node]:
            if colors[nei] != 0:
                used[colors[nei]] = True
        for c in range(1, 4):
            if not used[c]:
                colors[node] = c
                if backtrack(node + 1):
                    return True
                colors[node] = 0
        return False

    if backtrack(0):
        print("YES")
        print(" ".join(map(str, colors)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()