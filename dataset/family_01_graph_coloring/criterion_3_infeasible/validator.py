def validate(input_text: str, output_text: str):
    lines = input_text.split()
    n = int(lines[0]); m = int(lines[1])
    edges = set()
    idx = 2
    for _ in range(m):
        u = int(lines[idx]); v = int(lines[idx + 1]); idx += 2
        edges.add((min(u, v), max(u, v)))
    toks = output_text.split()
    if len(toks) != 3:
        return False, "expected exactly three integers"
    a, b, c = (int(t) for t in toks)
    if not (a < b < c):
        return False, "not strictly increasing"
    for x, y in ((a, b), (a, c), (b, c)):
        if (x, y) not in edges:
            return False, f"pair {x}-{y} is not a conflict"
    return True, "valid triangle"
