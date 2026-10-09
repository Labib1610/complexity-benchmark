def validate(input_text: str, output_text: str):
    data = input_text.split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    # count distinct undirected edges actually present (defensive)
    edges = set()
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        edges.add((min(u, v), max(u, v)))
    m_distinct = len(edges)

    toks = output_text.split()
    if not toks:
        return False, "empty output"

    head = toks[0].upper()

    # A bare NO (or any non-certificate) must fail: this arm requires a checkable proof of
    # impossibility, not a constant answer (audit B5).
    if head == "SIZE":
        if k > n:
            return True, f"valid SIZE certificate: k={k} exceeds the {n} vertices"
        return False, f"SIZE certificate invalid: k={k} does not exceed n={n}"

    if head == "COMPLETE":
        if m_distinct == n * (n - 1) // 2 and k >= 2:
            return True, "valid COMPLETE certificate: the graph is complete, so max IS = 1 < k"
        if m_distinct != n * (n - 1) // 2:
            return False, "COMPLETE certificate invalid: the graph is not complete"
        return False, f"COMPLETE certificate invalid: k={k} < 2, so an IS of size k exists"

    return False, f"first token must be SIZE or COMPLETE, got {toks[0]!r}"
