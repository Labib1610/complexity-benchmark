import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # 2-SAT with n variables, variables indexed 1..n
    # literal x: positive -> 2*x-2, negative -> 2*x-1
    size = 2 * n
    head = [-1] * size
    to = []
    nxt = []

    def add_edge(u, v):
        to.append(v)
        nxt.append(head[u])
        head[u] = len(to) - 1

    def add_impl(u, v):
        add_edge(u, v)

    def add_clause(a, b):
        # a or b
        na = a ^ 1
        nb = b ^ 1
        add_impl(na, b)
        add_impl(nb, a)

    def lit(val):
        if val > 0:
            return 2 * (val - 1)
        else:
            return 2 * (-val - 1) + 1

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        add_clause(lit(a), lit(b))

    # Tarjan SCC
    index = 0
    indices = [-1] * size
    lowlink = [0] * size
    onstack = [False] * size
    stack = []
    comp = [-1] * size
    comp_id = 0

    sys.setrecursionlimit(1 << 25)

    # iterative Tarjan
    for start in range(size):
        if indices[start] != -1:
            continue
        call_stack = [(start, head[start], False)]
        while call_stack:
            node, e, processed = call_stack.pop()
            if processed:
                lowlink[node] = min(lowlink[node], lowlink[to[e]] if e != -1 else lowlink[node])
                e = nxt[e] if e != -1 else -1
                while e != -1:
                    v = to[e]
                    if indices[v] == -1:
                        # need to process v, push back current state
                        call_stack.append((node, e, True))
                        call_stack.append((v, head[v], False))
                        break
                    elif onstack[v]:
                        lowlink[node] = min(lowlink[node], indices[v])
                    e = nxt[e]
                else:
                    if lowlink[node] == indices[node]:
                        while True:
                            w = stack.pop()
                            onstack[w] = False
                            comp[w] = comp_id
                            if w == node:
                                break
                        comp_id += 1
            else:
                indices[node] = index
                lowlink[node] = index
                index += 1
                stack.append(node)
                onstack[node] = True
                e2 = head[node]
                while e2 != -1:
                    v = to[e2]
                    if indices[v] == -1:
                        call_stack.append((node, e2, True))
                        call_stack.append((v, head[v], False))
                        break
                    elif onstack[v]:
                        lowlink[node] = min(lowlink[node], indices[v])
                    e2 = nxt[e2]
                else:
                    if lowlink[node] == indices[node]:
                        while True:
                            w = stack.pop()
                            onstack[w] = False
                            comp[w] = comp_id
                            if w == node:
                                break
                        comp_id += 1

    assignment = [0] * (n + 1)
    for i in range(1, n + 1):
        pos = 2 * (i - 1)
        neg = pos + 1
        if comp[pos] == comp[neg]:
            print("NO")
            return
        assignment[i] = 1 if comp[pos] < comp[neg] else 0

    out = ["YES"]
    out.append(" ".join(str(assignment[i]) for i in range(1, n + 1)))
    sys.stdout.write("\n".join(out) + "\n")

solve()