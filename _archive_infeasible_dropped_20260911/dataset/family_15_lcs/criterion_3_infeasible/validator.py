def validate(input_text: str, output_text: str):
    data = input_text.split()
    k = int(data[0])
    seqs = [data[1 + i] for i in range(k)]
    seq1_letters = set(seqs[0])
    seq_sets = [set(s) for s in seqs]

    toks = output_text.split()
    if not toks:
        return False, "empty output"

    # A bare NONE (or any non-certificate) must fail: this arm requires a checkable proof of
    # impossibility, not a constant answer (audit B5).
    if toks[0].upper() != "BLOCK":
        return False, f"first token must be BLOCK, got {toks[0]!r}"

    rest = toks[1:]
    if len(rest) % 2 != 0:
        return False, "each blocked letter needs a 'letter index' pair"

    covered = set()
    for i in range(0, len(rest), 2):
        c = rest[i]
        if len(c) != 1:
            return False, f"expected a single letter, got {c!r}"
        try:
            j = int(rest[i + 1])
        except ValueError:
            return False, f"sequence index must be an integer, got {rest[i + 1]!r}"
        if j < 2 or j > k:
            return False, f"sequence index {j} out of range 2..{k}"
        if c in seq_sets[j - 1]:
            return False, f"letter {c!r} DOES appear in sequence {j}, so it is not blocked there"
        covered.add(c)

    missing = seq1_letters - covered
    if missing:
        return False, f"letters {sorted(missing)} of sequence 1 are not blocked by any sequence"

    return True, "valid BLOCK certificate: every letter of sequence 1 is absent from some sequence"
