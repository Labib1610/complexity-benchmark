"""Objective for the time-budget / approximation study (audit B7, gate 3).

Multiple-sequence LCS is a maximization problem, so a shorter-but-valid common motif deserves
partial credit proportional to its length. `value()` recomputes the achieved length from the motif
in the output (it does NOT trust the claimed number), returning 0 if the motif is not a common
subsequence of every sequence. studies/time_budget/scoring.py divides produced/optimal for the ratio.
"""

MINIMIZE = False   # maximize motif length


def _is_subsequence(motif, s):
    it = iter(s)
    return all(ch in it for ch in motif)


def value(input_text: str, output_text: str) -> float:
    data = input_text.split()
    k = int(data[0])
    seqs = [data[1 + i] for i in range(k)]

    toks = output_text.split()
    if len(toks) < 2:
        # length line only (or empty) -> motif is empty -> length 0
        return 0.0
    motif = toks[1]
    if not all(_is_subsequence(motif, s) for s in seqs):
        return 0.0            # not a common subsequence -> no credit
    return float(len(motif))
