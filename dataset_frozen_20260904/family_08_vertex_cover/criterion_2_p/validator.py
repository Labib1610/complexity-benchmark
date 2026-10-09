from collections import deque


def _bipartite_min_vc(n, adj):
    """Minimum vertex cover of a bipartite graph = max matching (Koenig). Returns int, or None if
    the graph is not bipartite."""
    color = [-1] * (n + 1)
    for s in range(1, n + 1):
        if color[s] != -1:
            continue
        color[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if color[w] == -1:
                    color[w] = color[u] ^ 1
                    q.append(w)
                elif color[w] == color[u]:
                    return None
    A = [v for v in range(1, n + 1) if color[v] == 0]
    INF = float("inf")
    matchA = {u: 0 for u in A}; matchB = [0] * (n + 1); dist = {}

    def bfs():
        q = deque()
        for u in A:
            if matchA[u] == 0:
                dist[u] = 0; q.append(u)
            else:
                dist[u] = INF
        found = False
        while q:
            u = q.popleft()
            for w in adj[u]:
                x = matchB[w]
                if x == 0:
                    found = True
                elif dist.get(x, INF) == INF:
                    dist[x] = dist[u] + 1; q.append(x)
        return found

    def dfs(u):
        for w in adj[u]:
            x = matchB[w]
            if x == 0 or (dist.get(x, INF) == dist[u] + 1 and dfs(x)):
                matchA[u] = w; matchB[w] = u; return True
        dist[u] = INF; return False

    matching = 0
    while bfs():
        for u in A:
            if matchA[u] == 0 and dfs(u):
                matching += 1
    return matching


def validate(input_text: str, output_text: str):
    import sys
    sys.setrecursionlimit(300000)
    data = input_text.split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        adj[u].append(v); adj[v].append(u)
        edges.append((u, v))

    min_vc = _bipartite_min_vc(n, adj)
    if min_vc is None:
        return False, "input graph is not bipartite (criterion-2 promise violated)"
    feasible = (min_vc <= k)

    toks = output_text.split()
    if not toks:
        return False, "empty output"

    head = toks[0].upper()
    if head == "NO":
        if feasible:
            return False, f"reported NO but a vertex cover of size {k} exists (min is {min_vc})"
        return True, "correctly reported no vertex cover of size k"

    if head != "YES":
        return False, f"first token must be YES or NO, got {toks[0]!r}"

    if not feasible:
        return False, f"reported YES but the minimum vertex cover is {min_vc} > k={k}"

    try:
        picks = [int(t) for t in toks[1:]]
    except ValueError:
        return False, "non-integer vertex index"

    if len(picks) > k:
        return False, f"cover has {len(picks)} vertices, exceeds budget k={k}"

    chosen = set()
    for p in picks:
        if p < 1 or p > n:
            return False, f"vertex {p} out of range 1..{n}"
        chosen.add(p)

    for (u, v) in edges:
        if u not in chosen and v not in chosen:
            return False, f"corridor ({u},{v}) is not covered"

    return True, "valid vertex cover of size <= k"
