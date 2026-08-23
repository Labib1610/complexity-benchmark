import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_mask = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            print("NO")
            return
        adj_mask[u] |= 1 << v
        adj_mask[v] |= 1 << u

    neigh = []
    for i in range(n):
        mask = adj_mask[i]
        lst = []
        while mask:
            lsb = mask & -mask
            lst.append(lsb.bit_length() - 1)
            mask ^= lsb
        neigh.append(lst)

    color = [0] * n          # 0 = uncolored, otherwise 1,2,3
    avail = [7] * n          # bitmask of available colors (bit0->color1, etc.)

    sys.setrecursionlimit(10000)

    def propagate(v: int, c: int, changes: list) -> bool:
        stack = [(v, c)]
        bit_c = 1 << (c - 1)
        while stack:
            x, col = stack.pop()
            if color[x]:
                if color[x] != col:
                    return False
                continue
            bit = 1 << (col - 1)
            if not (avail[x] & bit):
                return False
            changes.append((x, avail[x]))
            color[x] = col
            avail[x] = 0
            for u in neigh[x]:
                if color[u] == 0:
                    old = avail[u]
                    if old & bit:
                        new = old ^ bit
                        if new == 0:
                            return False
                        changes.append((u, old))
                        avail[u] = new
                        if new & (new - 1) == 0:
                            # forced to the single remaining color
                            stack.append((u, new.bit_length()))
        return True

    def undo(changes: list) -> None:
        for v, old in reversed(changes):
            avail[v] = old
            color[v] = 0

    def dfs() -> bool:
        i = 0
        while i < n and color[i]:
            i += 1
        if i == n:
            return True

        mask = avail[i]
        for col in (1, 2, 3):
            if mask & (1 << (col - 1)):
                changes = []
                if propagate(i, col, changes):
                    if dfs():
                        return True
                undo(changes)
        return False

    if dfs():
        out = sys.stdout
        out.write("YES\n")
        out.write(' '.join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()