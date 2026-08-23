import sys

sys.setrecursionlimit(10000)


class Solver:
    __slots__ = ('n', 'neighbors')

    def __init__(self, n, neighbors):
        self.n = n
        self.neighbors = neighbors

    def is_colorable(self, fixed):
        n = self.n
        neighbors = self.neighbors
        avail = [7] * n
        stack = []
        for v in range(n):
            c = fixed[v]
            if c:
                bit = 1 << (c - 1)
                if not (avail[v] & bit):
                    return False
                if avail[v] != bit:
                    avail[v] = bit
                    stack.append(v)
        while stack:
            u = stack.pop()
            cu = avail[u]
            for w in neighbors[u]:
                if avail[w] & cu:
                    avail[w] &= ~cu
                    if avail[w] == 0:
                        return False
                    if avail[w].bit_count() == 1:
                        stack.append(w)
        return self._dfs(avail)

    def _dfs(self, avail):
        n = self.n
        neighbors = self.neighbors
        v = -1
        for i in range(n):
            bc = avail[i].bit_count()
            if bc == 2:
                v = i
                break
            if bc == 3 and v == -1:
                v = i
        if v == -1:
            return True

        bits = avail[v]
        cands = []
        if bits & 1:
            cnt = 0
            for w in neighbors[v]:
                if avail[w] & 1:
                    cnt += 1
            cands.append((cnt, 1))
        if bits & 2:
            cnt = 0
            for w in neighbors[v]:
                if avail[w] & 2:
                    cnt += 1
            cands.append((cnt, 2))
        if bits & 4:
            cnt = 0
            for w in neighbors[v]:
                if avail[w] & 4:
                    cnt += 1
            cands.append((cnt, 4))
        cands.sort(reverse=True)

        for _, bit in cands:
            changed = []
            if self._propagate(avail, v, bit, changed):
                if self._dfs(avail):
                    return True
            for x, old in changed:
                avail[x] = old
        return False

    def _propagate(self, avail, v, bit, changed):
        changed.append((v, avail[v]))
        avail[v] = bit
        stack = [v]
        neighbors = self.neighbors
        while stack:
            u = stack.pop()
            cu = avail[u]
            for w in neighbors[u]:
                if avail[w] & cu:
                    changed.append((w, avail[w]))
                    avail[w] &= ~cu
                    if avail[w] == 0:
                        return False
                    if avail[w].bit_count() == 1:
                        stack.append(w)
        return True


def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj_mask = [0] * n
    neighbors = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            sys.stdout.write("NO\n")
            return
        if not ((adj_mask[u] >> v) & 1):
            adj_mask[u] |= 1 << v
            adj_mask[v] |= 1 << u
            neighbors[u].append(v)
            neighbors[v].append(u)

    # Quick K4 detection
    for u in range(n):
        Au = adj_mask[u]
        vmask = Au & ~((1 << (u + 1)) - 1)
        while vmask:
            lsb = vmask & -vmask
            v = lsb.bit_length() - 1
            common = Au & adj_mask[v]
            wmask = common & ~((1 << (v + 1)) - 1)
            while wmask:
                lsb2 = wmask & -wmask
                w = lsb2.bit_length() - 1
                if (adj_mask[u] & adj_mask[v] & adj_mask[w]) & ~((1 << u) | (1 << v) | (1 << w)):
                    sys.stdout.write("NO\n")
                    return
                wmask ^= lsb2
            vmask ^= lsb

    solver = Solver(n, neighbors)
    colors = [0] * n
    for i in range(n):
        chosen = 0
        for c in (1, 2, 3):
            ok = True
            for nb in neighbors[i]:
                if colors[nb] == c:
                    ok = False
                    break
            if not ok:
                continue
            colors[i] = c
            if solver.is_colorable(colors):
                chosen = c
                break
            colors[i] = 0
        if chosen == 0:
            sys.stdout.write("NO\n")
            return

    sys.stdout.write("YES\n" + " ".join(str(c) for c in colors) + "\n")


if __name__ == "__main__":
    solve()