def validate(input_text: str, output_text: str):
    data = input_text.split()
    n = int(data[0])
    d = [int(data[1 + i]) for i in range(n)]
    total = sum(d)

    # Re-derive ground truth: can the tasks be split into two equal totals?
    if total % 2 != 0:
        feasible = False
        target = None
    else:
        target = total // 2
        half = n // 2
        A = d[:half]
        Bp = d[half:]

        def sums(part):
            res = {0}
            for v in part:
                res |= {s + v for s in res}
            return res

        sb = sums(Bp)
        feasible = any((target - s) in sb for s in sums(A))

    toks = output_text.split()
    if not toks:
        return False, "empty output"

    head = toks[0].upper()
    if head == "NO":
        if feasible:
            return False, "reported NO but an equal split exists"
        return True, "correctly reported no equal split"

    if head != "YES":
        return False, f"first token must be YES or NO, got {toks[0]!r}"

    if not feasible:
        return False, "reported YES but no equal split exists"

    try:
        picks = [int(t) for t in toks[1:]]
    except ValueError:
        return False, "non-integer task index"

    chosen = set()
    for p in picks:
        if p < 1 or p > n:
            return False, f"task index {p} out of range 1..{n}"
        if p in chosen:
            return False, f"task {p} listed twice"
        chosen.add(p)

    machine1 = sum(d[p - 1] for p in chosen)
    if machine1 != target:
        return False, f"first machine total {machine1} is not half of {total}"

    return True, "valid equal split"
