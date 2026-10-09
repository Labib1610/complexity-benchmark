import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    triples = []               # masks
    triples_xyz = []           # original triples for output
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        mask = (1 << x) | (1 << (k + y)) | (1 << (2 * k + z))
        triples.append(mask)
        triples_xyz.append((x + 1, y + 1, z + 1))

    total_items = 3 * k
    FULL = (1 << total_items) - 1

    # element -> list of triple indices containing it
    elem_to_triples = [[] for _ in range(total_items)]
    for idx, mask in enumerate(triples):
        # extract three bits
        m = mask
        while m:
            lsb = m & -m
            e = (lsb.bit_length() - 1)
            elem_to_triples[e].append(idx)
            m ^= lsb

    # recursive search
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def search(used_mask):
        if used_mask == FULL:
            return ()                     # empty tuple, success

        # choose uncovered element with fewest usable triples
        best_elem = -1
        best_len = 10**9
        # iterate over bits not set
        remaining = (~used_mask) & FULL
        while remaining:
            lsb = remaining & -remaining
            e = lsb.bit_length() - 1
            remaining ^= lsb

            cnt = 0
            for idx in elem_to_triples[e]:
                if triples[idx] & used_mask == 0:
                    cnt += 1
            if cnt == 0:
                return None               # dead end
            if cnt < best_len:
                best_len = cnt
                best_elem = e
                if cnt == 1:
                    break

        # try all usable triples containing best_elem
        for idx in elem_to_triples[best_elem]:
            m = triples[idx]
            if m & used_mask:
                continue
            res = search(used_mask | m)
            if res is not None:
                return (idx,) + res
        return None

    ans = search(0)
    out = []
    if ans is None:
        out.append("NO")
    else:
        out.append("YES")
        for idx in ans:
            x, y, z = triples_xyz[idx]
            out.append(f"{x} {y} {z}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()