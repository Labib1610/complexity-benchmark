def _greedy_min_bins(n, C, w):
    """Minimum containers when at most two items fit per container (every item > C/3): two-pointer
    greedy, which is optimal for the pair-or-alone case."""
    ws = sorted(w)
    i, j = 0, n - 1
    bins = 0
    while i <= j:
        bins += 1
        if i == j:
            break
        if ws[i] + ws[j] <= C:
            i += 1; j -= 1
        else:
            j -= 1
    return bins


def validate(input_text: str, output_text: str):
    data = input_text.split()
    idx = 0
    n = int(data[idx]); idx += 1
    C = int(data[idx]); idx += 1
    w = [int(data[idx + i]) for i in range(n)]; idx += n

    if any(3 * wi <= C for wi in w):
        return False, "criterion-2 promise violated: every item must weigh more than C/3"
    optimal = _greedy_min_bins(n, C, w)

    toks = output_text.split()
    if not toks:
        return False, "empty output"
    try:
        claimed = int(toks[0])
    except ValueError:
        return False, f"first token must be the container count, got {toks[0]!r}"
    if claimed != optimal:
        return False, f"reported {claimed} containers but the minimum is {optimal}"

    try:
        assign = [int(t) for t in toks[1:]]
    except ValueError:
        return False, "non-integer container index"
    if len(assign) != n:
        return False, f"expected {n} container numbers, got {len(assign)}"
    load = {}
    for i, b in enumerate(assign):
        if b < 1:
            return False, f"container index {b} must be >= 1"
        load[b] = load.get(b, 0) + w[i]
        if load[b] > C:
            return False, f"container {b} exceeds capacity C={C}"
    if len(load) != claimed:
        return False, f"assignment uses {len(load)} containers but you reported {claimed}"
    return True, "valid minimum loading"
