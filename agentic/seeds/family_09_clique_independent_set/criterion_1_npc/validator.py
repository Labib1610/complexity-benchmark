import sys


def validate(input_text: str, output_text: str):
    sys.setrecursionlimit(100000)
    data = input_text.split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1

    adj = [0] * n
    for _ in range(m):
        u = int(data[idx]) - 1; v = int(data[idx + 1]) - 1; idx += 2
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)

    # Re-derive ground truth: does a k-clique exist? (branch and bound)
    found = [False]

    def expand(rsize, P):
        if found[0]:
            return
        if rsize == k:
            found[0] = True
            return
        if rsize + bin(P).count("1") < k:
            return
        Pp = P
        while Pp and not found[0]:
            v = (Pp & -Pp).bit_length() - 1
            Pp &= Pp - 1
            P &= ~(1 << v)
            expand(rsize + 1, P & adj[v])
            if rsize + bin(P).count("1") < k:
                return

    expand(0, (1 << n) - 1)
    feasible = found[0]

    toks = output_text.split()
    if not toks:
        return False, "empty output"

    head = toks[0].upper()
    if head == "NO":
        if feasible:
            return False, "reported NO but a tight-knit group of size k exists"
        return True, "correctly reported no such group"

    if head != "YES":
        return False, f"first token must be YES or NO, got {toks[0]!r}"

    if not feasible:
        return False, "reported YES but no tight-knit group of size k exists"

    try:
        verts = [int(t) for t in toks[1:]]
    except ValueError:
        return False, "non-integer user number"

    if len(verts) != k:
        return False, f"expected {k} users, got {len(verts)}"
    if len(set(verts)) != k:
        return False, "duplicate user in the group"
    for w in verts:
        if w < 1 or w > n:
            return False, f"user {w} out of range 1..{n}"

    vs = [w - 1 for w in verts]
    for i in range(k):
        for j in range(i + 1, k):
            if not (adj[vs[i]] >> vs[j] & 1):
                return False, f"users {verts[i]} and {verts[j]} are not connected"

    return True, "valid tight-knit group of size k"
