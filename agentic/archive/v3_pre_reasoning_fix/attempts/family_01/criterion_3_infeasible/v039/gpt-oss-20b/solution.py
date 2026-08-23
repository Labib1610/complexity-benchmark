import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    neighbors = [[] for _ in range(n)]
    masks = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        masks[u] |= 1 << v
        masks[v] |= 1 << u
        neighbors[u].append(v)
        neighbors[v].append(u)

    for lst in neighbors:
        lst.sort()

    for a in range(n):
        mask_a = masks[a]
        for b in neighbors[a]:
            if b <= a:
                continue
            common = mask_a & masks[b]
            # Remove bits <= b
            trimmed = common >> (b + 1)
            if trimmed == 0:
                continue
            low = trimmed & -trimmed
            tz = low.bit_length() - 1
            c = b + 1 + tz
            # c is guaranteed to be > b
            print(a + 1, b + 1, c + 1)
            return

if __name__ == "__main__":
    solve()