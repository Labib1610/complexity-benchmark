"""Objective for the time-budget / approximation study (audit B7, gate 3).

Shortest common superstring is a minimization problem: any string that contains every fragment is
valid, and a shorter one is better (a plain concatenation is valid but long). `value()` returns the
length of the output if it is a valid superstring of every fragment, else 0 (no credit).
studies/time_budget/scoring.py divides optimal/produced for the ratio (MINIMIZE).
"""

MINIMIZE = True   # minimize the superstring length


def value(input_text: str, output_text: str) -> float:
    data = input_text.split()
    k = int(data[0])
    frags = [data[1 + i] for i in range(k)]

    out = output_text.split()
    if not out:
        return 0.0
    sup = out[0]
    if any(f not in sup for f in frags):
        return 0.0            # not a superstring of every fragment -> no credit
    return float(len(sup))
