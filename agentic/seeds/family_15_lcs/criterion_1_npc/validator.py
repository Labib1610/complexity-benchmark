import sys
from functools import lru_cache


def validate(input_text: str, output_text: str):
    sys.setrecursionlimit(1000000)
    data = input_text.split()
    k = int(data[0])
    seqs = [data[1 + i] for i in range(k)]
    lens = [len(s) for s in seqs]

    # Re-derive the length of a longest shared motif via the same k-dim DP.
    @lru_cache(maxsize=None)
    def dp(pos):
        for j in range(k):
            if pos[j] == lens[j]:
                return 0
        chars = {seqs[j][pos[j]] for j in range(k)}
        best = 0
        if len(chars) == 1:
            best = 1 + dp(tuple(p + 1 for p in pos))
        for j in range(k):
            nxt = list(pos)
            nxt[j] += 1
            v = dp(tuple(nxt))
            if v > best:
                best = v
        return best

    L = dp(tuple([0] * k))

    toks = output_text.split()
    if not toks:
        return False, "empty output"

    try:
        claimed = int(toks[0])
    except ValueError:
        return False, f"first token must be the length, got {toks[0]!r}"

    if claimed != L:
        return False, f"reported length {claimed} but the maximum is {L}"

    motif = toks[1] if len(toks) > 1 else ""
    if len(motif) != L:
        return False, f"provided motif has length {len(motif)}, expected {L}"

    # Verify motif is a subsequence of every sequence.
    for s in seqs:
        it = iter(s)
        if not all(ch in it for ch in motif):
            return False, f"'{motif}' is not a subsequence of every sequence"

    return True, "valid longest shared motif"
