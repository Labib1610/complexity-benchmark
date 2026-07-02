from bisect import bisect_right


def _optimal_value(items, B):
    # Meet-in-the-middle maximum achievable value with total cost <= B.
    n = len(items)
    half = n // 2
    A = items[:half]
    Bh = items[half:]

    def all_subsets(part):
        res = [(0, 0)]  # (cost, value)
        for (c, v) in part:
            res += [(c0 + c, v0 + v) for (c0, v0) in res]
        return res

    sa = all_subsets(A)
    sb = [x for x in all_subsets(Bh) if x[0] <= B]
    sb.sort(key=lambda x: (x[0], -x[1]))
    pref_cost = []
    pref_val = []
    bv = -1
    for cost, val in sb:
        if val > bv:
            bv = val
        pref_cost.append(cost)
        pref_val.append(bv)

    best = 0
    for costA, valA in sa:
        if costA > B:
            continue
        rem = B - costA
        j = bisect_right(pref_cost, rem) - 1
        if j >= 0:
            best = max(best, valA + pref_val[j])
    return best


def validate(input_text: str, output_text: str):
    data = input_text.split()
    idx = 0
    n = int(data[idx]); B = int(data[idx + 1]); idx += 2
    items = []
    for _ in range(n):
        c = int(data[idx]); v = int(data[idx + 1]); idx += 2
        items.append((c, v))

    optimal = _optimal_value(items, B)

    toks = output_text.split()
    if not toks:
        return False, "empty output"

    try:
        claimed = int(toks[0])
    except ValueError:
        return False, f"first token must be the maximum value, got {toks[0]!r}"

    if claimed != optimal:
        return False, f"reported value {claimed} but the optimum is {optimal}"

    try:
        picks = [int(t) for t in toks[1:]]
    except ValueError:
        return False, "non-integer investment index"

    chosen = set()
    for p in picks:
        if p < 1 or p > n:
            return False, f"investment index {p} out of range 1..{n}"
        if p in chosen:
            return False, f"investment {p} listed twice"
        chosen.add(p)

    total_cost = sum(items[p - 1][0] for p in chosen)
    total_val = sum(items[p - 1][1] for p in chosen)
    if total_cost > B:
        return False, f"selected cost {total_cost} exceeds budget {B}"
    if total_val != optimal:
        return False, f"selected value {total_val} does not match the optimum {optimal}"

    return True, "valid optimal selection"
