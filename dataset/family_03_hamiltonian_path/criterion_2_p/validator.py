from collections import deque


def _dag_has_hamiltonian_path(n, adj, indeg):
    """A DAG has a Hamiltonian path iff its topological order is unique (one in-degree-0 vertex at
    every Kahn step) and every consecutive pair is an edge. Returns the order or None."""
    indeg = indeg[:]
    q = deque(v for v in range(1, n + 1) if indeg[v] == 0)
    order = []
    while q:
        if len(q) != 1:
            return None
        v = q.popleft()
        order.append(v)
        for u in adj[v]:
            indeg[u] -= 1
            if indeg[u] == 0:
                q.append(u)
    if len(order) != n:
        return None
    return order


def validate(input_text: str, output_text: str):
    data = input_text.split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    adj = [[] for _ in range(n + 1)]
    edge = set()
    indeg = [0] * (n + 1)
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        adj[u].append(v); edge.add((u, v)); indeg[v] += 1

    order = _dag_has_hamiltonian_path(n, adj, indeg)
    feasible = order is not None

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
        if (a, b) not in edge:
            return False, f"no one-way road from {a} to {b}"
    return True, "valid delivery route"
