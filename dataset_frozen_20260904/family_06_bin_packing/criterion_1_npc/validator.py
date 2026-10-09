import sys


def _min_bins(n, C, w):
    order = sorted(range(n), key=lambda i: -w[i])

    def fits(kk):
        load = [0] * kk

        def solve(pos):
            if pos == n:
                return True
            i = order[pos]; wi = w[i]
            for b in range(kk):
                if load[b] + wi <= C:
                    load[b] += wi
                    if solve(pos + 1):
                        return True
                    load[b] -= wi
                if load[b] == 0:
                    break
            return False

        return solve(0)

    total = sum(w)
    lb = max(1, (total + C - 1) // C)
    for kk in range(lb, n + 1):
        if fits(kk):
            return kk
    return n


def _check_assignment(n, C, w, claimed, toks_rest):
    try:
        assign = [int(t) for t in toks_rest]
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
    used = len(load)
    if used != claimed:
        return False, f"assignment uses {used} containers but you reported {claimed}"
    return True, "ok"


def validate(input_text: str, output_text: str):
    sys.setrecursionlimit(10000)
    data = input_text.split()
    idx = 0
    n = int(data[idx]); idx += 1
    C = int(data[idx]); idx += 1
    w = [int(data[idx + i]) for i in range(n)]; idx += n

    optimal = _min_bins(n, C, w)

    toks = output_text.split()
    if not toks:
        return False, "empty output"
    try:
        claimed = int(toks[0])
    except ValueError:
        return False, f"first token must be the container count, got {toks[0]!r}"
    if claimed != optimal:
        return False, f"reported {claimed} containers but the minimum is {optimal}"

    ok, msg = _check_assignment(n, C, w, claimed, toks[1:])
    if not ok:
        return False, msg
    return True, "valid minimum loading"
