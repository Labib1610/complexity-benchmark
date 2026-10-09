import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # Variables: x_i = 1 means s_i = 1 (ON, Manifold A active)
    #            x_i = 0 means s_i = 0 (OFF, Manifold B active)
    # Literal encoding:
    #   positive l  -> Manifold B -> active when x_|l| = 0 -> literal NOT x_|l|
    #   negative l  -> Manifold A -> active when x_|l| = 1 -> literal x_|l|
    # We encode literal as integer:
    #   variable v in [1..n], literal = 2*v if positive literal (x_v = 1)
    #   literal = 2*v+1 if negative literal (x_v = 0)
    # For input l:
    #   l > 0: Manifold B -> NOT x_l -> literal 2*l+1
    #   l < 0: Manifold A -> x_|l| -> literal 2*|l|

    N = 2 * n
    head = [-1] * N
    to = []
    nxt = []

    def add_edge(u, v):
        to.append(v)
        nxt.append(head[u])
        head[u] = len(to) - 1

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        # literal for a
        if a > 0:
            la = 2 * a + 1
            nla = 2 * a
        else:
            la = 2 * (-a)
            nla = 2 * (-a) + 1
        # literal for b
        if b > 0:
            lb = 2 * b + 1
            nlb = 2 * b
        else:
            lb = 2 * (-b)
            nlb = 2 * (-b) + 1
        # clause: (not la) or (not lb)
        add_edge(la, nlb)
        add_edge(lb, nla)

    # Tarjan's SCC
    index_counter = 0
    stack = []
    on_stack = [False] * N
    indices = [-1] * N
    lowlink = [0] * N
    scc_id = [-1] * N
    scc_count = 0
    # iterative DFS
    dfs_stack = []

    for i in range(N):
        if indices[i] != -1:
            continue
        # start DFS from i
        dfs_stack.append((i, head[i]))
        indices[i] = index_counter
        lowlink[i] = index_counter
        index_counter += 1
        stack.append(i)
        on_stack[i] = True

        while dfs_stack:
            v, e = dfs_stack[-1]
            if e != -1:
                dfs_stack[-1] = (v, nxt[e])
                w = to[e]
                if indices[w] == -1:
                    indices[w] = index_counter
                    lowlink[w] = index_counter
                    index_counter += 1
                    stack.append(w)
                    on_stack[w] = True
                    dfs_stack.append((w, head[w]))
                elif on_stack[w]:
                    if indices[w] < lowlink[v]:
                        lowlink[v] = indices[w]
            else:
                dfs_stack.pop()
                if dfs_stack:
                    parent = dfs_stack[-1][0]
                    if lowlink[v] < lowlink[parent]:
                        lowlink[parent] = lowlink[v]
                if lowlink[v] == indices[v]:
                    while True:
                        w = stack.pop()
                        on_stack[w] = False
                        scc_id[w] = scc_count
                        if w == v:
                            break
                    scc_count += 1

    # Check satisfiability
    assignment = [0] * n
    for i in range(n):
        if scc_id[2*i] == scc_id[2*i+1]:
            print("NO")
            return
        # If x_i SCC comes after not x_i SCC in topological order,
        # then x_i is true -> s_i = 1
        assignment[i] = 1 if scc_id[2*i] > scc_id[2*i+1] else 0

    out = ["YES", " ".join(map(str, assignment))]
    sys.stdout.write("\n".join(out))

solve()