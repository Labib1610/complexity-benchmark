import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].add(v)
        adj[v].add(u)

    color = [0] * n  # 0 unassigned, 1..3 colors

    sys.setrecursionlimit(10000)

    def dfs(idx):
        if idx == n:
            return True
        for c in (1, 2, 3):
            ok = True
            for nb in adj[idx]:
                if color[nb] == c:
                    ok = False
                    break
            if not ok:
                continue
            color[idx] = c
            if dfs(idx + 1):
                return True
            color[idx] = 0
        return False

    if dfs(0):
        out = ['YES', ' '.join(str(c) for c in color)]
    else:
        out = ['NO']
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()