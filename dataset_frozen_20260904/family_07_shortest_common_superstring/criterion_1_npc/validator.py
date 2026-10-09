def _min_scs_length(frags):
    """Length of a shortest common superstring of `frags` via Held-Karp over overlaps."""
    # drop fragments contained in another (keep the rest 'live')
    live = []
    for i, fi in enumerate(frags):
        if any(i != j and fi in fj and (len(fi) < len(fj) or (len(fi) == len(fj) and j < i))
               for j, fj in enumerate(frags)):
            continue
        live.append(fi)
    m = len(live)
    if m == 0:
        return 0
    if m == 1:
        return len(live[0])

    ov = [[0] * m for _ in range(m)]
    for i in range(m):
        a = live[i]
        for j in range(m):
            if i == j:
                continue
            b = live[j]
            for L in range(min(len(a), len(b)), 0, -1):
                if a[len(a) - L:] == b[:L]:
                    ov[i][j] = L
                    break

    INF = float("inf")
    dp = [[INF] * m for _ in range(1 << m)]
    for i in range(m):
        dp[1 << i][i] = len(live[i])
    for mask in range(1 << m):
        for i in range(m):
            cur = dp[mask][i]
            if cur == INF:
                continue
            for j in range(m):
                if mask >> j & 1:
                    continue
                nv = cur + len(live[j]) - ov[i][j]
                nmask = mask | (1 << j)
                if nv < dp[nmask][j]:
                    dp[nmask][j] = nv
    full = (1 << m) - 1
    return min(dp[full])


def validate(input_text: str, output_text: str):
    data = input_text.split()
    k = int(data[0])
    frags = [data[1 + i] for i in range(k)]

    min_len = _min_scs_length(frags)

    out = output_text.split()
    if not out:
        return False, "empty output"
    sup = out[0]

    for f in frags:
        if f not in sup:
            return False, f"fragment {f!r} is not a substring of the output"
    if len(sup) != min_len:
        return False, f"output length {len(sup)} is not the minimum {min_len}"
    return True, "valid shortest common superstring"
