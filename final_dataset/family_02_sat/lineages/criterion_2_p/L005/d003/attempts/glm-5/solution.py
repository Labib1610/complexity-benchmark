import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # 2-SAT: variable i (1-indexed) has nodes 2i (true) and 2i+1 (false)
    # literal x>0 means "x is 0" -> false node of x
    # literal x<0 means "x is 1" -> true node of x
    # For each route (l1, l2): NOT(l1 AND l2) => add edges l1 -> NOT l2, l2 -> NOT l1
    size = 2 * n + 2
    graph = [[] for _ in range(size)]
    rgraph = [[] for _ in range(size)]

    def node(lit):
        if lit > 0:
            return 2 * lit + 1  # false node
        else:
            return 2 * (-lit)   # true node

    def neg(x):
        return x ^ 1

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        a = node(l1)
        b = node(l2)
        # a -> not b
        graph[a].append(neg(b))
        rgraph[neg(b)].append(a)
        # b -> not a
        graph[b].append(neg(a))
        rgraph[neg(a)].append(b)

    # Kosaraju SCC
    visited = bytearray(size)
    order = []
    for i in range(2, 2 * n + 2):
        if not visited[i]:
            stack = [(i, 0)]
            visited[i] = 1
            while stack:
                v, idx = stack[-1]
                if idx < len(graph[v]):
                    w = graph[v][idx]
                    stack[-1] = (v, idx + 1)
                    if not visited[w]:
                        visited[w] = 1
                        stack.append((w, 0))
                else:
                    stack.pop()
                    order.append(v)

    visited = bytearray(size)
    comp = [-1] * size
    cid = 0
    for u in reversed(order):
        if not visited[u]:
            stack = [u]
            visited[u] = 1
            comp[u] = cid
            while stack:
                v = stack.pop()
                for w in rgraph[v]:
                    if not visited[w]:
                        visited[w] = 1
                        comp[w] = cid
                        stack.append(w)
            cid += 1

    # Check satisfiability and assign
    assignment = [0] * (n + 1)
    for i in range(1, n + 1):
        t = 2 * i      # true node (x=1)
        f = 2 * i + 1  # false node (x=0)
        if comp[t] == comp[f]:
            print("NO")
            return
        # We want: if true node is chosen, x=1; if false node chosen, x=0
        # comp[t] > comp[f] means true node is in a later SCC (topologically earlier)
        assignment[i] = 1 if comp[t] > comp[f] else 0

    print("YES")
    print(' '.join(map(str, assignment[1:])))

solve()