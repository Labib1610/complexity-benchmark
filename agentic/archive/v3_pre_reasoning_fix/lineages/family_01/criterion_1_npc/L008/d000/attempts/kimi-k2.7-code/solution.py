import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    bad = False
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            bad = True
        else:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    if bad:
        sys.stdout.write("NO")
        return

    full = (1 << n) - 1
    ALL_FORB = (1 << 1) | (1 << 2) | (1 << 3)  # bits 1,2,3 used for colors 1,2,3
    force = [-1] * 16
    for mask in range(16):
        if mask.bit_count() == 2:
            miss = ALL_FORB ^ mask
            force[mask] = miss.bit_length() - 1

    color = [0] * n
    seen = [0] * n
    assigned = [0]
    history = []

    def undo(snap: int) -> None:
        while len(history) > snap:
            kind, a, b = history.pop()
            if kind == 0:
                color[a] = b
                if b == 0:
                    assigned[0] &= ~(1 << a)
            else:
                seen[a] = b

    def set_color(v: int, c: int) -> bool:
        if color[v] != 0:
            return color[v] == c
        if (seen[v] >> c) & 1:
            return False
        history.append((0, v, 0))
        color[v] = c
        assigned[0] |= 1 << v
        stack = [v]
        while stack:
            x = stack.pop()
            cx = color[x]
            nb = adj[x] & ~assigned[0]
            while nb:
                lsb = nb & -nb
                u = lsb.bit_length() - 1
                nb ^= lsb
                if color[u] != 0:
                    continue
                if (seen[u] >> cx) & 1:
                    continue
                history.append((1, u, seen[u]))
                seen[u] |= 1 << cx
                su = seen[u]
                if su == ALL_FORB:
                    return False
                fc = force[su]
                if fc != -1:
                    if color[u] != 0:
                        if color[u] != fc:
                            return False
                    else:
                        if (seen[u] >> fc) & 1:
                            return False
                        history.append((0, u, 0))
                        color[u] = fc
                        assigned[0] |= 1 << u
                        stack.append(u)
        return True

    def dfs() -> bool:
        if assigned[0] == full:
            return True
        free = full & ~assigned[0]
        v = (free & -free).bit_length() - 1
        forb = seen[v]
        if (forb & (1 << 1)) == 0:
            snap = len(history)
            if set_color(v, 1) and dfs():
                return True
            undo(snap)
        if (forb & (1 << 2)) == 0:
            snap = len(history)
            if set_color(v, 2) and dfs():
                return True
            undo(snap)
        if (forb & (1 << 3)) == 0:
            snap = len(history)
            if set_color(v, 3) and dfs():
                return True
            undo(snap)
        return False

    if dfs():
        out = ["YES", " ".join(str(c) for c in color)]
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

solve()