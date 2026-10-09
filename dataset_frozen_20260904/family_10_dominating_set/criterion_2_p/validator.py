from collections import deque


def _min_dominating_set_tree(n, adj):
    INF = n + 5
    parent = [0] * (n + 1)
    order = []
    visited = [False] * (n + 1)
    visited[1] = True
    q = deque([1])
    while q:
        u = q.popleft(); order.append(u)
        for w in adj[u]:
            if not visited[w]:
                visited[w] = True; parent[w] = u; q.append(w)
    if len(order) != n:
        return None  # not connected / not a tree on 1..n
    children = [[] for _ in range(n + 1)]
    for v in order[1:]:
        children[parent[v]].append(v)

    IN = [0] * (n + 1); DOM = [0] * (n + 1); UND = [0] * (n + 1)
    for v in reversed(order):
        ch = children[v]
        s_in = 1; s_und = 0; base = 0; best_delta = INF; has_in = False
        for c in ch:
            s_in += min(IN[c], DOM[c], UND[c])
            s_und += DOM[c]
            mc = IN[c] if IN[c] <= DOM[c] else DOM[c]
            base += mc
            if IN[c] <= DOM[c]:
                has_in = True
            else:
                best_delta = min(best_delta, IN[c] - DOM[c])
        IN[v] = s_in; UND[v] = s_und
        DOM[v] = INF if not ch else (base if has_in else base + best_delta)
    return min(IN[1], DOM[1])


def validate(input_text: str, output_text: str):
    data = input_text.split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        adj[u].append(v); adj[v].append(u)

    if m != n - 1:
        return False, "criterion-2 promise violated: not a tree (m != n-1)"
    min_ds = _min_dominating_set_tree(n, adj)
    if min_ds is None:
        return False, "criterion-2 promise violated: graph is not a connected tree"
    feasible = (min_ds <= k)

    toks = output_text.split()
    if not toks:
        return False, "empty output"

    head = toks[0].upper()
    if head == "NO":
        if feasible:
            return False, f"reported NO but a dominating set of size {k} exists (min is {min_ds})"
        return True, "correctly reported no dominating set of size k"

    if head != "YES":
        return False, f"first token must be YES or NO, got {toks[0]!r}"

    if not feasible:
        return False, f"reported YES but the minimum dominating set is {min_ds} > k={k}"

    try:
        picks = [int(t) for t in toks[1:]]
    except ValueError:
        return False, "non-integer sensor index"

    if len(picks) > k:
        return False, f"placed {len(picks)} sensors, exceeds budget k={k}"

    chosen = set()
    for p in picks:
        if p < 1 or p > n:
            return False, f"location {p} out of range 1..{n}"
        chosen.add(p)

    # Every location must be a sensor or adjacent to one.
    covered = set(chosen)
    for v in chosen:
        for w in adj[v]:
            covered.add(w)
    if len(covered) != n:
        missing = [v for v in range(1, n + 1) if v not in covered]
        return False, f"locations {missing[:5]} are not covered"

    return True, "valid dominating set of size <= k"
