def validate(input_text: str, output_text: str):
    data = input_text.split()
    idx = 0
    u = int(data[idx]); s = int(data[idx + 1]); k = int(data[idx + 2]); idx += 3

    set_masks = []
    for _ in range(s):
        cnt = int(data[idx]); idx += 1
        mk = 0
        for _ in range(cnt):
            sk = int(data[idx]); idx += 1
            mk |= 1 << (sk - 1)
        set_masks.append(mk)

    full = (1 << u) - 1
    INF = float("inf")

    # Re-derive ground truth minimum cover via the same bitmask DP.
    best = [INF] * (1 << u)
    best[0] = 0
    for mask in range(1 << u):
        b = best[mask]
        if b == INF or mask == full:
            continue
        low = (~mask) & full
        low_bit = low & -low
        for sm in set_masks:
            if sm & low_bit:
                nm = mask | sm
                if b + 1 < best[nm]:
                    best[nm] = b + 1
    feasible = best[full] <= k

    toks = output_text.split()
    if not toks:
        return False, "empty output"

    head = toks[0].upper()
    if head == "NO":
        if feasible:
            return False, "reported NO but k hires can cover every skill"
        return True, "correctly reported that k hires are not enough"

    if head != "YES":
        return False, f"first token must be YES or NO, got {toks[0]!r}"

    if not feasible:
        return False, "reported YES but k hires cannot cover every skill"

    try:
        picks = [int(t) for t in toks[1:]]
    except ValueError:
        return False, "non-integer consultant index"

    chosen = set()
    for p in picks:
        if p < 1 or p > s:
            return False, f"consultant index {p} out of range 1..{s}"
        chosen.add(p)

    if len(chosen) > k:
        return False, f"hired {len(chosen)} consultants, budget is {k}"

    covered = 0
    for p in chosen:
        covered |= set_masks[p - 1]
    if covered != full:
        return False, "some required skill is not covered"

    return True, "valid selection of at most k consultants covering all skills"
