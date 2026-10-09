import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # 2-SAT: variable i (1-indexed) -> node 2*i for True, 2*i+1 for False
    # literal x>0: node 2*x; literal x<0: node 2*(-x)+1
    size = 2 * (n + 1)
    head = [-1] * size
    to = []
    nxt = []

    def add_edge(u, v):
        to.append(v)
        nxt.append(head[u])
        head[u] = len(to) - 1

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        # rule: a OR b
        # not a -> b, not b -> a
        na = (2 * abs(a) + 1) if a > 0 else (2 * (-a))
        nb = (2 * abs(b) + 1) if b > 0 else (2 * (-b))
        la = (2 * a) if a > 0 else (2 * (-a) + 1)
        lb = (2 * b) if b > 0 else (2 * (-b) + 1)
        add_edge(na, lb)
        add_edge(nb, la)

    # Tarjan SCC
    index = 0
    indices = [-1] * size
    lowlink = [0] * size
    on_stack = [False] * size
    stack = []
    comp = [-1] * size

    sys.setrecursionlimit(1 << 25)

    # iterative Tarjan
    for start in range(2, size):
        if indices[start] != -1:
            continue
        call_stack = [(start, head[start], 0)]
        while call_stack:
            v, e, state = call_stack[-1]
            if state == 0:
                indices[v] = index
                lowlink[v] = index
                index += 1
                stack.append(v)
                on_stack[v] = True
                call_stack[-1] = (v, e, 1)
            else:
                if e != -1:
                    w = to[e]
                    if indices[w] == -1:
                        call_stack[-1] = (v, head[v], 2)
                        call_stack.append((w, head[w], 0))
                        continue
                    elif on_stack[w]:
                        if indices[w] < lowlink[v]:
                            lowlink[v] = indices[w]
                    call_stack[-1] = (v, nxt[e], 2)
                    continue
                else:
                    if lowlink[v] == indices[v]:
                        while True:
                            w = stack.pop()
                            on_stack[w] = False
                            comp[w] = v
                            if w == v:
                                break
                    call_stack.pop()
                    if call_stack:
                        parent = call_stack[-1][0]
                        if lowlink[v] < lowlink[parent]:
                            lowlink[parent] = lowlink[v]

    # check satisfiability
    for i in range(1, n + 1):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return

    # assign: if comp[true] < comp[false] in reverse topological order -> true
    # Tarjan produces SCCs in reverse topological order, so smaller comp id = later in topo
    # We want value true if SCC of true node comes after SCC of false node in topo order
    # i.e., comp[true] < comp[false] (since Tarjan assigns in reverse topo)
    assignment = [0] * (n + 1)
    for i in range(1, n + 1):
        assignment[i] = 1 if comp[2 * i] < comp[2 * i + 1] else 0

    out = ["YES", " ".join(str(assignment[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out) + "\n")

solve()