import sys
from itertools import combinations

def main():
    sys.setrecursionlimit(1000000)
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj_mask = [0] * n
    self_loop = False
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            self_loop = True
            continue
        adj_mask[u] |= 1 << v
        adj_mask[v] |= 1 << u

    if self_loop:
        sys.stdout.write("NO\n")
        return

    # A 4-clique makes 3-coloring impossible.
    for a, b, c, d in combinations(range(n), 4):
        mask = (1 << a) | (1 << b) | (1 << c) | (1 << d)
        if ((adj_mask[a] & mask) == mask ^ (1 << a) and
            (adj_mask[b] & mask) == mask ^ (1 << b) and
            (adj_mask[c] & mask) == mask ^ (1 << c) and
            (adj_mask[d] & mask) == mask ^ (1 << d)):
            sys.stdout.write("NO\n")
            return

    adj = [[] for _ in range(n)]
    for v in range(n):
        mask = adj_mask[v]
        lst = adj[v]
        while mask:
            lsb = mask & -mask
            u = lsb.bit_length() - 1
            lst.append(u)
            mask ^= lsb

    color = [-1] * n
    forb = [0] * n
    FULL = 7
    stk = []

    def revert(sp):
        while len(stk) > sp:
            typ, a, b = stk.pop()
            if typ:
                forb[a] ^= 1 << b
            else:
                color[a] = -1
                forb[a] = b

    def force(v, c, sp):
        if color[v] != -1:
            return sp if color[v] == c else -1
        bit = 1 << c
        if forb[v] & bit:
            return -1
        color[v] = c
        stk.append((0, v, forb[v]))
        sp += 1
        for u in adj[v]:
            if color[u] == -1:
                if not (forb[u] & bit):
                    forb[u] |= bit
                    stk.append((1, u, c))
                    sp += 1
                    if forb[u] == FULL:
                        return -1
                    if forb[u].bit_count() == 2:
                        abit = FULL ^ forb[u]
                        ac = abit.bit_length() - 1
                        sp = force(u, ac, sp)
                        if sp < 0:
                            return -1
        return sp

    def dfs(pos):
        while pos < n and color[pos] != -1:
            pos += 1
        if pos == n:
            return True
        v = pos
        fv = forb[v]
        sp = len(stk)
        for c in (0, 1, 2):
            if fv & (1 << c):
                continue
            new_sp = force(v, c, sp)
            if new_sp >= 0 and dfs(pos + 1):
                return True
            revert(sp)
        return False

    if dfs(0):
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(str(x + 1) for x in color))
        sys.stdout.write("\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == "__main__":
    main()