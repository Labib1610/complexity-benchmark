import sys
from bisect import bisect_right


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); B = int(data[idx + 1]); idx += 2
    items = []
    for _ in range(n):
        c = int(data[idx]); v = int(data[idx + 1]); idx += 2
        items.append((c, v))

    # Meet-in-the-middle: enumerate every subset of each half; for the right
    # half keep, by increasing cost, a prefix maximum of value (and the mask
    # achieving it). For each left subset within budget, binary-search the best
    # affordable right subset.
    half = n // 2
    A = items[:half]
    Bh = items[half:]

    def all_subsets(part):
        res = [(0, 0, 0)]  # (cost, value, mask over local indices)
        for i, (c, v) in enumerate(part):
            bit = 1 << i
            res += [(c0 + c, v0 + v, mk | bit) for (c0, v0, mk) in res]
        return res

    sa = all_subsets(A)
    sb = [x for x in all_subsets(Bh) if x[0] <= B]
    sb.sort(key=lambda x: (x[0], -x[1]))

    pref_cost = []
    pref_val = []
    pref_mask = []
    bv = -1
    bm = 0
    for cost, val, mask in sb:
        if val > bv:
            bv = val
            bm = mask
        pref_cost.append(cost)
        pref_val.append(bv)
        pref_mask.append(bm)

    best_total = -1
    best_amask = 0
    best_bmask = 0
    for costA, valA, maskA in sa:
        if costA > B:
            continue
        rem = B - costA
        j = bisect_right(pref_cost, rem) - 1
        if j >= 0:
            tot = valA + pref_val[j]
            if tot > best_total:
                best_total = tot
                best_amask = maskA
                best_bmask = pref_mask[j]

    chosen = []
    for i in range(half):
        if best_amask >> i & 1:
            chosen.append(i + 1)
    for i in range(len(Bh)):
        if best_bmask >> i & 1:
            chosen.append(half + i + 1)

    sys.stdout.write(f"{best_total}\n")
    sys.stdout.write(" ".join(map(str, chosen)) + "\n")


main()
