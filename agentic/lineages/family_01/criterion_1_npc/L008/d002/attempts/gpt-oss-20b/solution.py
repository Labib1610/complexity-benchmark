import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * n  # 0 uncolored, 1..3 colors

    def dfs(idx):
        if idx == n:
            return True
        # try colors in order 1..3
        for c in (1, 2, 3):
            conflict = False
            for nb in adj[idx]:
                if nb < idx and color[nb] == c:
                    conflict = True
                    break
            if conflict:
                continue
            color[idx] = c
            if dfs(idx + 1):
                return True
            color[idx] = 0
        return False

    if dfs(0):
        out = ["YES", " ".join(str(x) for x in color)]
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()