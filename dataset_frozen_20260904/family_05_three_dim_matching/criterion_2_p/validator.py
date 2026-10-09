from collections import deque


def _perfect_XZ_matching(k, zopts):
    """Perfect bipartite matching between specialists and slots (Hopcroft-Karp). Returns bool."""
    INF = float("inf")
    matchX = [0] * (k + 1); matchZ = [0] * (k + 1); dist = [0] * (k + 1)

    def bfs():
        q = deque()
        for x in range(1, k + 1):
            if matchX[x] == 0:
                dist[x] = 0; q.append(x)
            else:
                dist[x] = INF
        found = False
        while q:
            x = q.popleft()
            for z in zopts[x]:
                w = matchZ[z]
                if w == 0:
                    found = True
                elif dist[w] == INF:
                    dist[w] = dist[x] + 1; q.append(w)
        return found

    def dfs(x):
        for z in zopts[x]:
            w = matchZ[z]
            if w == 0 or (dist[w] == dist[x] + 1 and dfs(w)):
                matchX[x] = z; matchZ[z] = x
                return True
        dist[x] = INF
        return False

    matching = 0
    while bfs():
        for x in range(1, k + 1):
            if matchX[x] == 0 and dfs(x):
                matching += 1
    return matching == k


def validate(input_text: str, output_text: str):
    data = input_text.split()
    idx = 0
    k = int(data[idx]); t = int(data[idx + 1]); idx += 2
    allowed = set()
    Yset = [set() for _ in range(k + 1)]
    zopts = [[] for _ in range(k + 1)]
    for _ in range(t):
        x = int(data[idx]); y = int(data[idx + 1]); z = int(data[idx + 2]); idx += 3
        allowed.add((x, y, z))
        Yset[x].add(y)
        zopts[x].append(z)

    # Verify the tractable promise: each specialist ties to exactly one machine, and those machines
    # are all distinct (a bijection X->Y).
    Y = [0] * (k + 1)
    seen_y = set()
    for x in range(1, k + 1):
        if len(Yset[x]) != 1:
            return False, f"criterion-2 promise violated: specialist {x} works with != 1 machine"
        Y[x] = next(iter(Yset[x]))
        if Y[x] in seen_y:
            return False, "criterion-2 promise violated: two specialists share a machine"
        seen_y.add(Y[x])

    feasible = _perfect_XZ_matching(k, zopts)

    toks = output_text.split()
    if not toks:
        return False, "empty output"
    head = toks[0].upper()
    if head == "NO":
        if feasible:
            return False, "reported NO but a valid selection of crews exists"
        return True, "correctly reported no selection"
    if head != "YES":
        return False, f"first token must be YES or NO, got {toks[0]!r}"
    if not feasible:
        return False, "reported YES but no valid selection exists"

    nums = toks[1:]
    if len(nums) != 3 * k:
        return False, f"expected {k} crews (3*k values), got {len(nums)}"
    try:
        vals = [int(v) for v in nums]
    except ValueError:
        return False, "non-integer value in crews"
    cov_x, cov_y, cov_z = set(), set(), set()
    for i in range(k):
        x, y, z = vals[3 * i], vals[3 * i + 1], vals[3 * i + 2]
        if (x, y, z) not in allowed:
            return False, f"crew ({x} {y} {z}) is not an allowed combination"
        if x in cov_x or y in cov_y or z in cov_z:
            return False, "a specialist, machine, or slot is used more than once"
        cov_x.add(x); cov_y.add(y); cov_z.add(z)
    full = set(range(1, k + 1))
    if cov_x != full or cov_y != full or cov_z != full:
        return False, "not every specialist, machine, and slot is covered exactly once"
    return True, "valid selection of k crews"
