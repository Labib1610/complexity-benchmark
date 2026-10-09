def validate(input_text: str, output_text: str):
    data = input_text.split()
    idx = 0
    k = int(data[idx]); t = int(data[idx + 1]); idx += 2
    appears = [False] * (k + 1)
    for _ in range(t):
        x = int(data[idx]); idx += 3
        if 1 <= x <= k:
            appears[x] = True

    smallest_empty = None
    for x in range(1, k + 1):
        if not appears[x]:
            smallest_empty = x
            break

    toks = output_text.split()
    if not toks:
        return False, "empty output"
    try:
        ans = int(toks[0])
    except ValueError:
        return False, f"expected a specialist number, got {toks[0]!r}"

    # The certificate is the smallest specialist appearing in no allowed crew (an uncoverable
    # element that proves infeasibility). A constant cannot pass -- it is instance-specific.
    if smallest_empty is None:
        return False, "no uncovered specialist exists (input violates the criterion promise)"
    if ans != smallest_empty:
        if 1 <= ans <= k and not appears[ans]:
            return False, f"specialist {ans} has no crew but is not the SMALLEST such ({smallest_empty})"
        return False, f"specialist {ans} is not an uncovered specialist"
    return True, f"valid certificate: specialist {smallest_empty} appears in no allowed crew"
