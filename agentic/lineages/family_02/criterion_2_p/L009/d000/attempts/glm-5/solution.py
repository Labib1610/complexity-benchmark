import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # 2-SAT with n variables, variables numbered 1..n
    # literal x: positive -> 2*(x-1), negative -> 2*(x-1)+1
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
        add_edge(v ^ 1, u ^ 1)

    def lit_node(x):
        if x > 0:
            return 2 * (x - 1)
        else:
            return 2 * (-x - 1) + 1

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        # rule: a OR b
        # equivalent to (not a -> b) and (not b -> a)
        na = lit_node(a) ^ 1
        nb = lit_node(b) ^ 1
        add_impl(na, lit_node(b))
        add_impl(nb, lit_node(a))

    # Tarjan's SCC
    index = 0
    indices = [-1] * size
    lowlink = [0] * size
    on_stack = [False] * size
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
            v, e, returned = call_stack[-1]
            if not returned:
                indices[v] = index
                lowlink[v] = index
                index += 1
                stack.append(v)
                on_stack[v] = True
                call_stack[-1] = (v, e, True)
                # process edges
                while e != -1:
                    w = to[e]
                    if indices[w] == -1:
                        call_stack.append((w, head[w], False))
                        e = nxt[e]
                        call_stack[-2] = (v, e, True)
                        break
                    elif on_stack[w]:
                        if indices[w] < lowlink[v]:
                            lowlink[v] = indices[w]
                        e = nxt[e]
                    else:
                        e = nxt[e]
                else:
                    # no more edges, finalize v
                    if lowlink[v] == indices[v]:
                        while True:
                            w = stack.pop()
                            on_stack[w] = False
                            comp[w] = comp_id
                            if w == v:
                                break
                        comp_id += 1
                    call_stack.pop()
                    if call_stack:
                        parent = call_stack[-1][0]
                        if lowlink[v] < lowlink[parent]:
                            lowlink[parent] = lowlink[v]
            else:
                # returned from child, finalize v
                if lowlink[v] == indices[v]:
                    while True:
                        w = stack.pop()
                        on_stack[w] = False
                        comp[w] = comp_id
                        if w == v:
                            break
                    comp_id += 1
                call_stack.pop()
                if call_stack:
                    parent = call_stack[-1][0]
                    if lowlink[v] < lowlink[parent]:
                        lowlink[parent] = lowlink[v]

    # check satisfiability
    assignment = [0] * n
    for i in range(n):
        pos = 2 * i
        neg = 2 * i + 1
        if comp[pos] == comp[neg]:
            print("NO")
            return
        assignment[i] = 1 if comp[pos] < comp[neg] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

solve()