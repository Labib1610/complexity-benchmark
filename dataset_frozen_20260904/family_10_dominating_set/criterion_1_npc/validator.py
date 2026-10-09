import sys


def validate(input_text: str, output_text: str):
    sys.setrecursionlimit(100000)
    data = input_text.split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1

    nb = [1 << v for v in range(n)]
    for _ in range(m):
        u = int(data[idx]) - 1; v = int(data[idx + 1]) - 1; idx += 2
        nb[u] |= (1 << v)
        nb[v] |= (1 << u)

    full = (1 << n) - 1

    # Re-derive ground truth: can k sensors cover every location?
    found = [False]

    def solve(covered, budget):
        if found[0]:
            return
        if covered == full:
            found[0] = True
            return
        if budget == 0:
            return
        rest = ~covered & full
        u = (rest & -rest).bit_length() - 1
        cand = nb[u]
        while cand and not found[0]:
            w = (cand & -cand).bit_length() - 1
            cand &= cand - 1
            solve(covered | nb[w], budget - 1)

    solve(0, k)
    feasible = found[0]

    toks = output_text.split()
    if not toks:
        return False, "empty output"

    head = toks[0].upper()
    if head == "NO":
        if feasible:
            return False, "reported NO but k sensors can cover every location"
        return True, "correctly reported that k sensors are not enough"

    if head != "YES":
        return False, f"first token must be YES or NO, got {toks[0]!r}"

    if not feasible:
        return False, "reported YES but k sensors cannot cover every location"

    try:
        verts = [int(t) for t in toks[1:]]
    except ValueError:
        return False, "non-integer sensor location"

    chosen = set()
    for w in verts:
        if w < 1 or w > n:
            return False, f"location {w} out of range 1..{n}"
        chosen.add(w)

    if len(chosen) > k:
        return False, f"placed {len(chosen)} sensors, budget is {k}"

    covered = 0
    for w in chosen:
        covered |= nb[w - 1]
    if covered != full:
        return False, "some location is not covered"

    return True, "valid sensor placement of at most k sensors"
