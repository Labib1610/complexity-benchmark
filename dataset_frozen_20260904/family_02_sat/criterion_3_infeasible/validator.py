def validate(input_text: str, output_text: str):
    data = input_text.split()
    idx = 0
    n, m = int(data[idx]), int(data[idx + 1]); idx += 2
    clauses = []
    for _ in range(m):
        a, b = int(data[idx]), int(data[idx + 1]); idx += 2
        clauses.append((a, b))

    toks = output_text.split()
    if len(toks) != 1:
        return False, f"expected exactly one integer, got {len(toks)} tokens"
    try:
        j = int(toks[0])
    except ValueError:
        return False, "output is not an integer"
    if j < 1 or j > n:
        return False, f"variable index {j} out of range [1..{n}]"

    # Build implication graph and run SCC to verify j is truly contradicted
    def lit(l):
        return 2 * (l - 1) if l > 0 else 2 * (-l - 1) + 1

    N = 2 * n
    adj  = [[] for _ in range(N)]
    radj = [[] for _ in range(N)]
    for a, b in clauses:
        la, lb = lit(a), lit(b)
        na, nb = la ^ 1, lb ^ 1
        adj[na].append(lb);  radj[lb].append(na)
        adj[nb].append(la);  radj[la].append(nb)

    visited = [False] * N
    order = []
    for s in range(N):
        if visited[s]:
            continue
        stack = [(s, iter(adj[s]))]
        visited[s] = True
        while stack:
            v, it = stack[-1]
            try:
                w = next(it)
                if not visited[w]:
                    visited[w] = True
                    stack.append((w, iter(adj[w])))
            except StopIteration:
                order.append(v)
                stack.pop()

    comp = [-1] * N
    c = 0
    for s in reversed(order):
        if comp[s] != -1:
            continue
        stk = [s]
        while stk:
            v = stk.pop()
            if comp[v] != -1:
                continue
            comp[v] = c
            for w in radj[v]:
                if comp[w] == -1:
                    stk.append(w)
        c += 1

    i = j - 1  # convert to 0-indexed
    if comp[2 * i] != comp[2 * i + 1]:
        return False, f"variable {j} is NOT in a contradiction (true/false literals in different SCCs)"

    # Also verify it is the SMALLEST such variable
    for k in range(i):
        if comp[2 * k] == comp[2 * k + 1]:
            return False, f"variable {j} is contradicted but variable {k + 1} is smaller and also contradicted"

    return True, f"variable {j} is the smallest contradicted variable"
