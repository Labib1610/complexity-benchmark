def validate(input_text: str, output_text: str):
    data = input_text.split()
    k = int(data[0])
    seqs = [data[1 + i] for i in range(k)]   # k == 2
    s, t = seqs[0], seqs[1]
    n, m = len(s), len(t)

    # Ground-truth LCS length via O(n*m) DP.
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if s[i] == t[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    L = dp[0][0]

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

    # Any longest motif is accepted -- verify it is a subsequence of both sequences.
    for seq in seqs:
        it = iter(seq)
        if not all(ch in it for ch in motif):
            return False, f"'{motif}' is not a subsequence of every sequence"

    return True, "valid longest shared motif"
