"""Objective for the time-budget / approximation study (audit B7, gate 3).

Bin packing is a minimization problem, so a valid-but-non-optimal loading (using more containers than
necessary) deserves partial credit inversely proportional to the containers it uses. `value()`
recomputes the containers used from the assignment in the output (it does NOT trust the claimed
number), returning 0 for an invalid loading. studies/time_budget/scoring.py divides optimal/produced
to get the ratio (MINIMIZE).
"""

MINIMIZE = True   # minimize the number of containers


def value(input_text: str, output_text: str) -> float:
    data = input_text.split()
    idx = 0
    n = int(data[idx]); idx += 1
    C = int(data[idx]); idx += 1
    w = [int(data[idx + i]) for i in range(n)]; idx += n

    toks = output_text.split()
    if len(toks) < 1 + n:
        return 0.0                        # missing assignment -> no credit
    try:
        assign = [int(t) for t in toks[1:1 + n]]
    except ValueError:
        return 0.0

    load = {}
    for i, b in enumerate(assign):
        if b < 1:
            return 0.0
        load[b] = load.get(b, 0) + w[i]
        if load[b] > C:
            return 0.0                    # a container over capacity -> invalid -> no credit
    return float(len(load))
