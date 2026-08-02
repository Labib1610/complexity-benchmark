import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n  # bitmask of neighbors
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    color = [0] * n
    found = False

    def backtrack(idx: int):
        nonlocal found
        if found:
            return
        if idx == n:
            found = True
            return
        mask = adj[idx]
        # Try colors 1,2,3 in order
        for c in (1, 2, 3):
            conflict = False
            # check already colored neighbors
            msk = mask
            while msk:
                v = (msk & -msk).bit_length() - 1
                if color[v] == c:
                    conflict = True
                    break
                msk &= msk - 1
            if not conflict:
                color[idx] = c
                backtrack(idx + 1)
                if found:
                    return
                color[idx] = 0

    backtrack(0)
    out = sys.stdout
    if not found:
        out.write("NO\n")
    else:
        out.write("YES\n")
        out.write(' '.join(map(str, color)))
        out.write('\n')

if __name__ == "__main__":
    solve()