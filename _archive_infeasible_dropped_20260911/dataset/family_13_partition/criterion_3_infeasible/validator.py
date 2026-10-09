def validate(input_text: str, output_text: str):
    data = input_text.split()
    n = int(data[0])
    d = [int(data[1 + i]) for i in range(n)]
    total = sum(d)

    toks = output_text.split()
    if not toks:
        return False, "empty output"

    head = toks[0].upper()

    # A bare NO (or any non-certificate) must fail: this arm requires a checkable proof of
    # impossibility, not a constant answer (audit B5).
    if head == "ODD":
        if total % 2 == 1:
            return True, f"valid ODD certificate: total {total} is odd"
        return False, f"ODD certificate invalid: total {total} is even"

    if head == "MAX":
        if 2 * max(d) > total:
            return True, f"valid MAX certificate: longest task {max(d)} exceeds half of {total}"
        return False, f"MAX certificate invalid: no task exceeds half of {total}"

    if head == "MOD":
        if len(toks) < 2:
            return False, "MOD certificate missing the divisor d"
        try:
            g = int(toks[1])
        except ValueError:
            return False, f"MOD divisor must be an integer, got {toks[1]!r}"
        if g < 2:
            return False, f"MOD divisor must be >= 2, got {g}"
        if total % 2 != 0:
            return False, "MOD certificate invalid: total is odd (use ODD)"
        if any(x % g != 0 for x in d):
            return False, f"MOD certificate invalid: not every duration is divisible by {g}"
        if (total // 2) % g == 0:
            return False, f"MOD certificate invalid: {g} also divides half the total"
        return True, f"valid MOD certificate: every duration divisible by {g}, half-total not"

    return False, f"first token must be ODD, MAX, or MOD, got {toks[0]!r}"
