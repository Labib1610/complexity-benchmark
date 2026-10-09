def _has_hamiltonian_path_undirected(n, adj):
    """Bitmask DP: does an undirected Hamiltonian path exist? (n <= 20)"""
    if n == 1:
        return True
    full = (1 << n) - 1
    # dp[mask] = bitset of vertices v such that a Ham path on `mask` ends at v
    dp = [0] * (1 << n)
    for v in range(n):
        dp[1 << v] = 1 << v
    for mask in range(1, full + 1):
        ends = dp[mask]
        if ends == 0:
            continue
        e = ends
        while e:
            v = (e & -e).bit_length() - 1
            e &= e - 1
            for u in range(n):
                if (mask >> u & 1) == 0 and (adj[v] >> u & 1):
                    dp[mask | (1 << u)] |= (1 << u)
    return dp[full] != 0


def validate(input_text: str, output_text: str):
    data = input_text.split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    adj = [0] * n
    edge = set()
    for _ in range(m):
        u = int(data[idx]) - 1; v = int(data[idx + 1]) - 1; idx += 2
        adj[u] |= (1 << v); adj[v] |= (1 << u)
        edge.add((min(u, v), max(u, v)))

    feasible = _has_hamiltonian_path_undirected(n, adj)

    toks = output_text.split()
    if not toks:
        return False, "empty output"
    head = toks[0].upper()
    if head == "NO":
        if feasible:
            return False, "reported NO but a valid route exists"
        return True, "correctly reported no route"
    if head != "YES":
        return False, f"first token must be YES or NO, got {toks[0]!r}"
    if not feasible:
        return False, "reported YES but no valid route exists"

    try:
        seq = [int(t) for t in toks[1:]]
    except ValueError:
        return False, "non-integer location in route"
    if len(seq) != n or sorted(seq) != list(range(1, n + 1)):
        return False, "route must be a permutation of all n locations"
    for a, b in zip(seq, seq[1:]):
        if (min(a - 1, b - 1), max(a - 1, b - 1)) not in edge:
            return False, f"no road between consecutive locations {a} and {b}"
    return True, "valid delivery route"
