import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    # allowed colors mask: bit 0 -> color 1, bit1 -> color2, bit2 -> color3
    ALL_MASK = 0b111
    allowed = [ALL_MASK]*(n+1)
    color = [0]*(n+1)
    found = False
    result = [0]*(n+1)

    def backtrack(i):
        nonlocal found
        if found:
            return
        if i > n:
            # all assigned
            found = True
            result[:] = color[:]
            return
        # try colors 1..3
        for c in (1,2,3):
            bit = 1 << (c-1)
            if allowed[i] & bit:
                # assign
                color[i] = c
                mods = []
                ok = True
                for nb in adj[i]:
                    if color[nb]==0:
                        old = allowed[nb]
                        new = old & ~bit
                        if new != old:
                            mods.append((nb, old))
                            allowed[nb] = new
                            if new == 0:
                                ok = False
                                break
                if ok:
                    backtrack(i+1)
                # revert
                for nb, old in mods:
                    allowed[nb] = old
                color[i] = 0
                if found:
                    return
        # no color worked, backtrack
    backtrack(1)
    out = []
    if not found:
        out.append("NO")
    else:
        out.append("YES")
        out.append(' '.join(str(result[i]) for i in range(1,n+1)))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()