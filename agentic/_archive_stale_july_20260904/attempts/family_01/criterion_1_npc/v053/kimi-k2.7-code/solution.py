import sys
from sys import setrecursionlimit
setrecursionlimit(1000000)

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

    # domains[v] : bitmask of still allowed colors (colors 0,1,2)
    FULL = 0b111

    # assign color c to v and propagate forced vertices
    def assign(v: int, c: int, domains: list, uncolored: int) -> bool:
        mask = 1 << c
        domains[v] = mask
        # neighbors that are still uncolored lose color c
        nb = adj[v] & uncolored
        while nb:
            lsb = nb & -nb
            u = (lsb.bit_length() - 1)
            nb ^= lsb
            if domains[u] & mask:
                domains[u] &= ~mask
                if domains[u] == 0:
                    return False
                if domains[u] & (domains[u] - 1) == 0:  # exactly one color left -> force
                    uc = domains[u].bit_length() - 1
                    if not assign(u, uc, domains, uncolored & ~(1 << u)):
                        return False
        return True

    # feasibility test for the remaining uncolored vertices
    def feasible(domains: list, uncolored: int) -> bool:
        if uncolored == 0:
            return True
        # choose uncolored vertex with smallest domain (MRV)
        best_v = -1
        best_d = 0
        best_size = 4
        mask = uncolored
        while mask:
            lsb = mask & -mask
            v = lsb.bit_length() - 1
            mask ^= lsb
            d = domains[v]
            sz = d.bit_count()
            if sz < best_size:
                best_size = sz
                best_v = v
                best_d = d
                if sz == 1:
                    break
        if best_size == 0:
            return False
        # try allowed colors
        colors = best_d
        while colors:
            lsb = colors & -colors
            c = lsb.bit_length() - 1
            colors ^= lsb
            dom2 = domains[:]
            if not assign(best_v, c, dom2, uncolored):
                continue
            if feasible(dom2, uncolored & ~(1 << best_v)):
                return True
        return False

    answer = [-1] * n
    domains = [FULL] * n
    uncolored = (1 << n) - 1

    # lexicographically smallest assignment by fixing vertices 0..n-1 in order
    def lex(pos: int, domains: list, uncolored: int) -> bool:
        if pos == n:
            return True
        # colors already forbidden by earlier assigned neighbours are removed from domains
        d = domains[pos]
        # try colors 0,1,2 in order
        for c in range(3):
            if not (d & (1 << c)):
                continue
            dom2 = domains[:]
            if not assign(pos, c, dom2, uncolored):
                continue
            u2 = uncolored & ~(1 << pos)
            if feasible(dom2, u2):
                answer[pos] = c
                if lex(pos + 1, dom2, u2):
                    return True
        return False

    if not lex(0, domains, uncolored):
        print("NO")
        return

    print("YES")
    print(' '.join(str(x + 1) for x in answer))

solve()