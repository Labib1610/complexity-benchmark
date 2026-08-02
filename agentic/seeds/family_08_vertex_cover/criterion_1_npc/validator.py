import sys


def validate(input_text: str, output_text: str):
    sys.setrecursionlimit(100000)
    data = input_text.split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    edges = []
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        edges.append((u, v))

    # Re-derive ground truth: can k guards cover all corridors? (bounded search)
    in_cover = [False] * (n + 1)

    def first_uncovered():
        for (u, v) in edges:
            if not in_cover[u] and not in_cover[v]:
                return (u, v)
        return None

    def solve(budget):
        e = first_uncovered()
        if e is None:
            return True
        if budget == 0:
            return False
        u, v = e
        for w in (u, v):
            in_cover[w] = True
            if solve(budget - 1):
                in_cover[w] = False
                return True
            in_cover[w] = False
        return False

    feasible = solve(k)

    toks = output_text.split()
    if not toks:
        return False, "empty output"

    head = toks[0].upper()
    if head == "NO":
        if feasible:
            return False, "reported NO but k guards can cover all corridors"
        return True, "correctly reported that k guards are not enough"

    if head != "YES":
        return False, f"first token must be YES or NO, got {toks[0]!r}"

    if not feasible:
        return False, "reported YES but k guards cannot cover all corridors"

    try:
        verts = [int(t) for t in toks[1:]]
    except ValueError:
        return False, "non-integer guard position"

    cover = set()
    for w in verts:
        if w < 1 or w > n:
            return False, f"junction {w} out of range 1..{n}"
        cover.add(w)

    if len(cover) > k:
        return False, f"placed {len(cover)} guards, budget is {k}"

    for (u, v) in edges:
        if u not in cover and v not in cover:
            return False, f"corridor ({u} {v}) is not watched"

    return True, "valid guard placement of at most k guards"
