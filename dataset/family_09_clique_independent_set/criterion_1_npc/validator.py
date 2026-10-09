def _max_is_size(n, adjG):
    """Max independent set size = max clique in the complement (bitset B&B, n <= ~46)."""
    comp = [(((1 << n) - 1) ^ (1 << i)) & ~adjG[i] for i in range(n)]
    best = 0

    def expand(Rsize, P):
        nonlocal best
        if P == 0:
            if Rsize > best:
                best = Rsize
            return
        if Rsize + bin(P).count("1") <= best:
            return
        Pp = P
        while Pp:
            if Rsize + bin(P).count("1") <= best:
                return
            v = (Pp & -Pp).bit_length() - 1
            Pp &= Pp - 1
            P &= ~(1 << v)
            expand(Rsize + 1, P & comp[v])

    expand(0, (1 << n) - 1)
    return best


def validate(input_text: str, output_text: str):
    data = input_text.split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    adjG = [0] * n
    adj_set = set()
    for _ in range(m):
        u = int(data[idx]) - 1; v = int(data[idx + 1]) - 1; idx += 2
        adjG[u] |= (1 << v)
        adjG[v] |= (1 << u)
        adj_set.add((min(u, v), max(u, v)))

    optimal = _max_is_size(n, adjG)
    feasible = (k <= n) and (optimal >= k)

    toks = output_text.split()
    if not toks:
        return False, "empty output"

    head = toks[0].upper()
    if head == "NO":
        if feasible:
            return False, f"reported NO but an independent set of size {k} exists"
        return True, "correctly reported no independent set of size k"

    if head != "YES":
        return False, f"first token must be YES or NO, got {toks[0]!r}"

    if not feasible:
        return False, f"reported YES but no independent set of size {k} exists (max is {optimal})"

    try:
        picks = [int(t) for t in toks[1:]]
    except ValueError:
        return False, "non-integer vertex index"

    if len(picks) != k:
        return False, f"expected {k} vertices, got {len(picks)}"

    chosen = set()
    for p in picks:
        if p < 1 or p > n:
            return False, f"vertex {p} out of range 1..{n}"
        if p in chosen:
            return False, f"vertex {p} listed twice"
        chosen.add(p)

    cl = [p - 1 for p in picks]
    for i in range(len(cl)):
        for j in range(i + 1, len(cl)):
            a, b = cl[i], cl[j]
            if (min(a, b), max(a, b)) in adj_set:
                return False, f"vertices {a + 1} and {b + 1} are connected -- not independent"

    return True, "valid independent set of size k"
