def validate(input_text: str, output_text: str):
    data = input_text.split()
    idx = 0
    n = int(data[idx]); B = int(data[idx + 1]); idx += 2
    costs = []
    for _ in range(n):
        c = int(data[idx]); idx += 2
        costs.append(c)
    min_cost = min(costs)

    toks = output_text.split()
    if not toks:
        return False, "empty output"

    head = toks[0].upper()

    # A bare NO (or any non-certificate) must fail: this arm requires a checkable proof of
    # impossibility, not a constant answer (audit B5).
    if head != "MIN":
        return False, f"first token must be MIN, got {toks[0]!r}"
    if len(toks) < 2:
        return False, "MIN certificate missing the value m"
    try:
        m = int(toks[1])
    except ValueError:
        return False, f"MIN value must be an integer, got {toks[1]!r}"

    # Valid iff B < m <= every cost. Then every cost >= m > B, so nothing is affordable.
    if m <= B:
        return False, f"MIN certificate invalid: m={m} does not exceed the budget {B}"
    if m > min_cost:
        return False, f"MIN certificate invalid: m={m} exceeds the cheapest cost {min_cost}"
    return True, f"valid MIN certificate: every cost >= {m} > budget {B}"


