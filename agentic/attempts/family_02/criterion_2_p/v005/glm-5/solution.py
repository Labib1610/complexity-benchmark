import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    clauses = []
    idx = 2
    for _ in range(m):
        a = int(data[idx]); b = int(data[idx+1])
        idx += 2
        clauses.append((a, b))

    # 2-SAT with n variables, each variable i has literal i (true) and -i (false)
    # literal x: if x>0 means variable x is True, if x<0 means variable -x is False
    # We map literal x to node:
    #   if x>0: 2*(x-1)
    #   if x<0: 2*(-x-1)+1
    # negation of node:
    #   if even: +1, if odd: -1

    size = 2 * n
    graph = [[] for _ in range(size)]
    rgraph = [[] for _ in range(size)]

    def node(lit):
        if lit > 0:
            return 2 * (lit - 1)
        else:
            return 2 * (-lit - 1) + 1

    def neg(u):
        return u ^ 1

    for a, b in clauses:
        # clause (a or b): add edges ~a -> b and ~b -> a
        na = node(a)
        nb = node(b)
        graph[na].append(nb)
        rgraph[nb].append(na)
        graph[neg(na)].append(neg(nb))  # wait, need ~b -> a
        # fix: ~b -> a means neg(nb) -> na
        # let's redo carefully
        # remove the wrong edge
        # Actually we appended neg(na)->neg(nb) which is wrong.
        pass

    # Rebuild graph correctly
    graph = [[] for _ in range(size)]
    rgraph = [[] for _ in range(size)]
    for a, b in clauses:
        na = node(a)
        nb = node(b)
        # ~a -> b
        graph[neg(na)].append(nb)
        rgraph[nb].append(neg(na))
        # ~b -> a
        graph[neg(nb)].append(na)
        rgraph[na].append(neg(nb))

    # Kosaraju SCC
    visited = [False] * size
    order = []
    for i in range(size):
        if not visited[i]:
            stack = [(i, 0)]
            while stack:
                v, p = stack[-1]
                if p == 0:
                    visited[v] = True
                if p < len(graph[v]):
                    w = graph[v][p]
                    stack[-1] = (v, p + 1)
                    if not visited[w]:
                        stack.append((w, 0))
                else:
                    stack.pop()
                    order.append(v)

    visited = [False] * size
    comp = [-1] * size
    cid = 0
    for u in reversed(order):
        if not visited[u]:
            stack = [u]
            visited[u] = True
            c = cid
            cid += 1
            while stack:
                v = stack.pop()
                comp[v] = c
                for w in rgraph[v]:
                    if not visited[w]:
                        visited[w] = True
                        stack.append(w)

    # Check satisfiability
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return

    # Assign: if comp[true_literal] > comp[false_literal] then true
    assignment = [0] * n
    for i in range(n):
        if comp[2*i] > comp[2*i+1]:
            assignment[i] = 1
        else:
            assignment[i] = 0

    print("YES")
    print(' '.join(map(str, assignment)))

solve()