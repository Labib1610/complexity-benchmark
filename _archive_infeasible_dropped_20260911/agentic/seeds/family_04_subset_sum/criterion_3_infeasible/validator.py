def validate(input_text: str, output_text: str):
    data = input_text.split()
    idx = 0
    n = int(data[idx]); idx += 1
    costs = [int(data[idx + i]) for i in range(n)]; idx += n
    T = int(data[idx]); idx += 1

    toks = output_text.split()
    if not toks:
        return False, "empty output"

    head = toks[0].upper()

    # A bare NO (or any non-certificate) must fail: this arm requires a checkable proof of
    # impossibility, not a constant answer (audit B5).
    if head == "SUM":
        total = sum(costs)
        if T > total:
            return True, f"valid SUM certificate: T={T} exceeds total {total}"
        return False, f"SUM certificate invalid: T={T} does not exceed total {sum(costs)}"

    if head == "MOD":
        if len(toks) < 2:
            return False, "MOD certificate missing the divisor d"
        try:
            d = int(toks[1])
        except ValueError:
            return False, f"MOD divisor must be an integer, got {toks[1]!r}"
        if d < 2:
            return False, f"MOD divisor must be >= 2, got {d}"
        if any(c % d != 0 for c in costs):
            return False, f"MOD certificate invalid: not every cost is divisible by {d}"
        if T % d == 0:
            return False, f"MOD certificate invalid: {d} also divides T={T}"
        return True, f"valid MOD certificate: every cost divisible by {d}, T not"

    return False, f"first token must be SUM or MOD, got {toks[0]!r}"
