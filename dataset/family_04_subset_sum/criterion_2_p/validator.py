def validate(input_text: str, output_text: str):
    data = input_text.split()
    idx = 0
    n = int(data[idx]); idx += 1
    costs = [int(data[idx + i]) for i in range(n)]; idx += n
    T = int(data[idx]); idx += 1

    # Re-derive ground truth via boolean DP over reachable sums (T <= 500).
    if T < 0:
        feasible = False
    else:
        reach = [False] * (T + 1)
        reach[0] = True
        for c in costs:
            if c > T:
                continue
            for j in range(T, c - 1, -1):
                if reach[j - c]:
                    reach[j] = True
        feasible = reach[T]

    toks = output_text.split()
    if not toks:
        return False, "empty output"

    head = toks[0].upper()
    if head == "NO":
        if feasible:
            return False, "reported NO but a group sums to exactly T"
        return True, "correctly reported no group"

    if head != "YES":
        return False, f"first token must be YES or NO, got {toks[0]!r}"

    if not feasible:
        return False, "reported YES but no group sums to exactly T"

    try:
        idxs = [int(t) for t in toks[1:]]
    except ValueError:
        return False, "non-integer index in chosen group"

    if len(set(idxs)) != len(idxs):
        return False, "duplicate index in chosen group"

    for i in idxs:
        if i < 1 or i > n:
            return False, f"index {i} out of range 1..{n}"

    total = sum(costs[i - 1] for i in idxs)
    if total != T:
        return False, f"chosen group sums to {total}, not {T}"

    return True, "valid group summing to T"
