import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    needed = k + 1
    used = [False] * (n + 1)
    res = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if len(res) == needed:
            break
        if not used[u] and not used[v]:
            used[u] = used[v] = True
            res.append((u, v))
    out_lines = ['{} {}'.format(u, v) for u, v in res]
    sys.stdout.write('\n'.join(out_lines))

if __name__ == "__main__":
    solve()