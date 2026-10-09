def validate(input_text: str, output_text: str):
    data = input_text.split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    edge_set = set()
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        edge_set.add(frozenset((u, v)))

    toks = output_text.split()
    if len(toks) % 2 != 0:
        return False, "output is not a list of vertex pairs"
    try:
        vals = [int(t) for t in toks]
    except ValueError:
        return False, "non-integer in output"

    pairs = [(vals[i], vals[i + 1]) for i in range(0, len(vals), 2)]
    if len(pairs) != k + 1:
        return False, f"expected {k + 1} independent corridors, got {len(pairs)}"

    used = set()
    for (u, v) in pairs:
        if frozenset((u, v)) not in edge_set:
            return False, f"({u} {v}) is not a corridor in the layout"
        if u in used or v in used:
            return False, f"corridor ({u} {v}) shares a junction with another chosen corridor"
        used.add(u)
        used.add(v)

    return True, "valid set of k+1 pairwise independent corridors"
