import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj_mask = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj_mask[u] |= 1 << v
        adj_mask[v] |= 1 << u

    # Quick impossible check: clique of size >3
    # O(n^4) for n<=40
    nodes = list(range(n))
    clique3 = False
    for i in range(n):
        for j in range(i+1, n):
            if not (adj_mask[i] >> j) & 1: continue
            for k in range(j+1, n):
                if not ((adj_mask[i] >> k) & 1 and (adj_mask[j] >> k) & 1):
                    continue
                # triangle found
                for l in range(k+1, n):
                    if (adj_mask[i] >> l) & 1 and (adj_mask[j] >> l) & 1 and (adj_mask[k] >> l) & 1:
                        print("NO")
                        return
    # If no K4 found, proceed with backtracking
    colors = [0] * n
    color_mask = [0, 0, 0, 0]  # index 1..3

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        u = idx
        for c in (1, 2, 3):
            if (adj_mask[u] & color_mask[c]) == 0:
                colors[u] = c
                color_mask[c] |= 1 << u
                if dfs(idx + 1):
                    return True
                color_mask[c] &= ~(1 << u)
                colors[u] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(colors[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()