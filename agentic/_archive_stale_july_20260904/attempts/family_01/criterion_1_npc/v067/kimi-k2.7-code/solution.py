import sys

sys.setrecursionlimit(1000000)


def solve() -> None:
    data = sys.stdin.buffer.read().split()
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

    def is_colorable(colors, allowed):
        """Return True iff the current partial assignment can be extended to a full 3-coloring."""
        nloc = n
        adjloc = adj

        def dfs():
            v = -1
            best = 4
            for i in range(nloc):
                if colors[i] == 0:
                    cnt = allowed[i].bit_count()
                    if cnt == 0:
                        return False
                    if cnt < best:
                        best = cnt
                        v = i
                        if cnt == 1:
                            break
            if v == -1:
                return True

            mask = allowed[v]
            av = adjloc[v]

            # least-constraining-value order
            cands = []
            mm = mask
            while mm:
                lsb = mm & -mm
                cb = lsb.bit_length() - 1
                cnt = 0
                bits = av
                while bits:
                    lsb2 = bits & -bits
                    u = lsb2.bit_length() - 1
                    if colors[u] == 0 and (allowed[u] >> cb) & 1:
                        cnt += 1
                    bits ^= lsb2
                cands.append((cnt, cb))
                mm ^= lsb
            cands.sort()

            for _, cb in cands:
                c = cb + 1
                colors[v] = c
                changed = []
                ok = True
                bits = av
                while bits:
                    lsb2 = bits & -bits
                    u = lsb2.bit_length() - 1
                    if colors[u] == 0:
                        new_mask = allowed[u] & ~(1 << cb)
                        if new_mask != allowed[u]:
                            changed.append((u, allowed[u]))
                            allowed[u] = new_mask
                            if new_mask == 0:
                                ok = False
                                break
                    bits ^= lsb2
                if ok and dfs():
                    return True
                for u, old in changed:
                    allowed[u] = old
                colors[v] = 0
            return False

        return dfs()

    colors = [0] * n
    allowed = [7] * n
    answer = []

    for i in range(n):
        found = False
        mask_i = allowed[i]
        for c in (1, 2, 3):
            cb = c - 1
            if not ((mask_i >> cb) & 1):
                continue
            cols = colors[:]
            alws = allowed[:]
            cols[i] = c
            ok = True
            bits = adj[i]
            while bits:
                lsb = bits & -bits
                j = lsb.bit_length() - 1
                if cols[j] == 0:
                    alws[j] &= ~(1 << cb)
                    if alws[j] == 0:
                        ok = False
                        break
                bits ^= lsb
            if ok and is_colorable(cols, alws):
                colors[i] = c
                bits = adj[i]
                while bits:
                    lsb = bits & -bits
                    j = lsb.bit_length() - 1
                    if colors[j] == 0:
                        allowed[j] &= ~(1 << cb)
                    bits ^= lsb
                answer.append(str(c))
                found = True
                break
        if not found:
            sys.stdout.write("NO\n")
            return

    sys.stdout.write("YES\n" + " ".join(answer))


if __name__ == "__main__":
    solve()