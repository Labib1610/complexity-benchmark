import sys
sys.setrecursionlimit(10000)

def main():
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

    colors = [0] * n  # 0 = unassigned, 1/2/3 = colors

    def dfs(idx):
        if idx == n:
            return True
        for c in (1, 2, 3):
            ok = True
            for nb in adj[idx]:
                if colors[nb] == c:
                    ok = False
                    break
            if ok:
                colors[idx] = c
                if dfs(idx + 1):
                    return True
                colors[idx] = 0
        return False

    if dfs(0):
        out = ['YES', ' '.join(map(str, colors))]
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    main()