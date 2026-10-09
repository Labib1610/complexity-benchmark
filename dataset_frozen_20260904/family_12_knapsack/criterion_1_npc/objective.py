"""Objective for the time-budget / approximation study (audit B7, gate 3).

Knapsack is a maximization problem, so a non-optimal but feasible selection deserves partial credit
proportional to the value it actually achieves. `value()` recomputes the achieved value from the
witness in the output (it does NOT trust the claimed number on line 1), returning 0 for an infeasible
or malformed selection. studies/time_budget/scoring.py divides produced/optimal to get the ratio.
"""

MINIMIZE = False   # maximize total value


def value(input_text: str, output_text: str) -> float:
    data = input_text.split()
    idx = 0
    n = int(data[idx]); B = int(data[idx + 1]); idx += 2
    items = []
    for _ in range(n):
        c = int(data[idx]); v = int(data[idx + 1]); idx += 2
        items.append((c, v))

    toks = output_text.split()
    if not toks:
        return 0.0
    # Line 1 is the claimed value; the real score comes from the witness indices that follow.
    try:
        picks = [int(t) for t in toks[1:]]
    except ValueError:
        return 0.0

    chosen = set()
    for p in picks:
        if p < 1 or p > n or p in chosen:
            return 0.0            # malformed / out-of-range / duplicate -> no credit
        chosen.add(p)

    total_cost = sum(items[p - 1][0] for p in chosen)
    if total_cost > B:
        return 0.0                # infeasible selection -> no credit
    return float(sum(items[p - 1][1] for p in chosen))
