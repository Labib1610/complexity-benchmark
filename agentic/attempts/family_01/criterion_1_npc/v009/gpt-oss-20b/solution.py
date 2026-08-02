import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    color = [0] * n          # 0 uncolored, 1-3 colored
    color_masks = [0, 0, 0, 0]  # index 1..3
    answer = None
    sys.setrecursionlimit(10000)

    def dfs(idx: int) -> bool:
        nonlocal answer
        if idx == n:
            answer = color[:]
            return True
        i = idx
        for c in (1, 2, 3):
            if adj[i] & color_masks[c]:
                continue
            color[i] = c
            color_masks[c] |= 1 << i
            if dfs(idx + 1):
                return True
            color_masks[c] &= ~(1 << i)
            color[i] = 0
        return False

    if dfs(0):
        out = ['YES', ' '.join(str(x) for x in answer)]
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()