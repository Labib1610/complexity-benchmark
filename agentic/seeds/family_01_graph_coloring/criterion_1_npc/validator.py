def _three_colorable(n, adj):
    """Forward-checking + MRV: is the graph properly 3-colourable?"""
    import sys
    sys.setrecursionlimit(1 << 20)
    dom = [0b111] * (n + 1)
    assigned = [False] * (n + 1)

    def pick():
        best, bestc = -1, 4
        for v in range(1, n + 1):
            if not assigned[v]:
                c = bin(dom[v]).count("1")
                if c < bestc:
                    bestc, best = c, v
                    if c <= 1:
                        break
        return best

    def solve(remaining):
        if remaining == 0:
            return True
        v = pick()
        if dom[v] == 0:
            return False
        for ci in range(3):
            if dom[v] & (1 << ci):
                assigned[v] = True
                removed = []
                ok = True
                cmask = ~(1 << ci)
                for u in adj[v]:
                    if not assigned[u] and (dom[u] & (1 << ci)):
                        dom[u] &= cmask; removed.append(u)
                        if dom[u] == 0:
                            ok = False
                if ok and solve(remaining - 1):
                    return True
                for u in removed:
                    dom[u] |= (1 << ci)
                assigned[v] = False
        return False

    return solve(n)


def validate(input_text: str, output_text: str):
    data = input_text.split()
    idx = 0
    n = int(data[idx]); m = int(data[idx + 1]); idx += 2
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        adj[u].append(v); adj[v].append(u); edges.append((u, v))

    feasible = _three_colorable(n, adj)

    toks = output_text.split()
    if not toks:
        return False, "empty output"
    head = toks[0].upper()
    if head == "NO":
        if feasible:
            return False, "reported NO but a valid 3-colouring exists"
        return True, "correctly reported no colouring"
    if head != "YES":
        return False, f"first token must be YES or NO, got {toks[0]!r}"
    if not feasible:
        return False, "reported YES but no valid 3-colouring exists"

    try:
        col = [int(t) for t in toks[1:]]
    except ValueError:
        return False, "non-integer colour"
    if len(col) != n:
        return False, f"expected {n} colours, got {len(col)}"
    if any(c < 1 or c > 3 for c in col):
        return False, "colours must be in {1,2,3}"
    cassign = [0] + col
    for u, v in edges:
        if cassign[u] == cassign[v]:
            return False, f"adjacent vertices {u} and {v} share colour {cassign[u]}"
    return True, "valid 3-colouring"
