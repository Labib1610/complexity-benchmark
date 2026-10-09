def _optimal_value(items, B):
    # 0/1 knapsack DP over the budget (B <= 2000 -> fast). Independent of the reference's own run.
    dp = [0] * (B + 1)
    for c, v in items:
        if c > B:
            continue
        for j in range(B, c - 1, -1):
            cand = dp[j - c] + v
            if cand > dp[j]:
                dp[j] = cand
    return dp[B]


def validate(input_text: str, output_text: str):
    data = input_text.split()
    idx = 0
    n = int(data[idx]); B = int(data[idx + 1]); idx += 2
    items = []
    for _ in range(n):
        c = int(data[idx]); v = int(data[idx + 1]); idx += 2
        items.append((c, v))

    optimal = _optimal_value(items, B)

    toks = output_text.split()
    if not toks:
        return False, "empty output"

    try:
        claimed = int(toks[0])
    except ValueError:
        return False, f"first token must be the maximum value, got {toks[0]!r}"

    if claimed != optimal:
        return False, f"reported value {claimed} but the optimum is {optimal}"

    try:
        picks = [int(t) for t in toks[1:]]
    except ValueError:
        return False, "non-integer investment index"

    chosen = set()
    for p in picks:
        if p < 1 or p > n:
            return False, f"investment index {p} out of range 1..{n}"
        if p in chosen:
            return False, f"investment {p} listed twice"
        chosen.add(p)

    total_cost = sum(items[p - 1][0] for p in chosen)
    total_val = sum(items[p - 1][1] for p in chosen)
    if total_cost > B:
        return False, f"selected cost {total_cost} exceeds budget {B}"
    if total_val != optimal:
        return False, f"selected value {total_val} does not match the optimum {optimal}"

    return True, "valid optimal selection"
