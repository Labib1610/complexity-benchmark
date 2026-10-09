from collections import deque


def _min_edge_cover(u, adj):
    """Minimum set cover with 2-element sets = minimum edge cover = u - max matching (Gallai),
    valid when every skill appears in some set. Returns int, or None if not bipartite."""
    color = [-1] * (u + 1)
    for st in range(1, u + 1):
        if color[st] != -1:
            continue
        color[st] = 0
        q = deque([st])
        while q:
            x = q.popleft()
            for y in adj[x]:
                if color[y] == -1:
                    color[y] = color[x] ^ 1; q.append(y)
                elif color[y] == color[x]:
                    return None
    A = [v for v in range(1, u + 1) if color[v] == 0]
    INF = float("inf")
    matchA = {v: 0 for v in A}; matchB = [0] * (u + 1); dist = {}

    def bfs():
        q = deque()
        for v in A:
            if matchA[v] == 0:
                dist[v] = 0; q.append(v)
            else:
                dist[v] = INF
        found = False
        while q:
            x = q.popleft()
            for y in adj[x]:
                w = matchB[y]
                if w == 0:
                    found = True
                elif dist.get(w, INF) == INF:
                    dist[w] = dist[x] + 1; q.append(w)
        return found

    def dfs(x):
        for y in adj[x]:
            w = matchB[y]
            if w == 0 or (dist.get(w, INF) == dist[x] + 1 and dfs(w)):
                matchA[x] = y; matchB[y] = x; return True
        dist[x] = INF; return False

    matching = 0
    while bfs():
        for v in A:
            if matchA[v] == 0 and dfs(v):
                matching += 1
    return u - matching


def validate(input_text: str, output_text: str):
    import sys
    sys.setrecursionlimit(300000)
    data = input_text.split()
    idx = 0
    u = int(data[idx]); s = int(data[idx + 1]); k = int(data[idx + 2]); idx += 3
    sets = []
    adj = [[] for _ in range(u + 1)]
    for _ in range(s):
        c = int(data[idx]); idx += 1
        elems = [int(data[idx + t]) for t in range(c)]; idx += c
        sets.append(elems)
        if c == 2:
            a, b = elems
            adj[a].append(b); adj[b].append(a)

    if any(len(st) != 2 for st in sets):
        return False, "criterion-2 promise violated: every set must have exactly 2 skills"
    min_ec = _min_edge_cover(u, adj)
    if min_ec is None:
        return False, "criterion-2 promise violated: skill graph is not bipartite"
    feasible = (min_ec <= k)

    toks = output_text.split()
    if not toks:
        return False, "empty output"

    head = toks[0].upper()
    if head == "NO":
        if feasible:
            return False, f"reported NO but a cover of size {k} exists (min is {min_ec})"
        return True, "correctly reported no cover of size k"

    if head != "YES":
        return False, f"first token must be YES or NO, got {toks[0]!r}"

    if not feasible:
        return False, f"reported YES but the minimum cover is {min_ec} > k={k}"

    try:
        picks = [int(t) for t in toks[1:]]
    except ValueError:
        return False, "non-integer consultant index"

    if len(picks) > k:
        return False, f"hired {len(picks)} consultants, exceeds budget k={k}"

    covered = set()
    for p in picks:
        if p < 1 or p > s:
            return False, f"consultant index {p} out of range 1..{s}"
        covered.update(sets[p - 1])

    if len(covered) != u or any(v not in covered for v in range(1, u + 1)):
        missing = [v for v in range(1, u + 1) if v not in covered]
        return False, f"skills {missing[:5]} are not covered"

    return True, "valid cover of size <= k"
