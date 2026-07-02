def validate(input_text: str, output_text: str):
    data = input_text.split()
    idx = 0
    n, m = int(data[idx]), int(data[idx + 1]); idx += 2
    clauses = []
    for _ in range(m):
        a, b = int(data[idx]), int(data[idx + 1]); idx += 2
        clauses.append((a, b))

    # Re-solve 2-SAT to know ground truth satisfiability
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

    satisfiable = all(comp[2 * i] != comp[2 * i + 1] for i in range(n))

    toks = output_text.split()
    if not toks:
        return False, "empty output"

    if toks[0] == "NO":
        if satisfiable:
            return False, "reported NO but formula is satisfiable"
        return True, "correctly identified as unsatisfiable"

    if toks[0] != "YES":
        return False, f"first token must be YES or NO, got {toks[0]!r}"

    if not satisfiable:
        return False, "reported YES but formula is unsatisfiable"

    if len(toks) != n + 1:
        return False, f"expected YES + {n} values, got {len(toks) - 1} values after YES"

    try:
        assignment = [int(toks[i + 1]) for i in range(n)]
    except ValueError:
        return False, "non-integer in assignment"

    if any(v not in (0, 1) for v in assignment):
        return False, "assignment values must be 0 or 1"

    for a, b in clauses:
        def lv(l):
            v = abs(l) - 1
            return assignment[v] if l > 0 else 1 - assignment[v]
        if lv(a) == 0 and lv(b) == 0:
            return False, f"clause ({a} {b}) is not satisfied"

    return True, "valid satisfying assignment"
