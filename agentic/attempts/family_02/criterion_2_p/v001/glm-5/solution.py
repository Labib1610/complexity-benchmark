import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # 2-SAT with n variables, variables indexed 1..n
    # literal x: positive -> 2*x, negative -> 2*(-x)+1
    # We'll use 0-based indexing for nodes: node for literal v is:
    #   if v > 0: 2*(v-1)
    #   if v < 0: 2*(-v-1)+1
    # complement: node ^ 1

    size = 2 * n
    graph = [[] for _ in range(size)]
    rgraph = [[] for _ in range(size)]

    def node(v):
        if v > 0:
            return 2 * (v - 1)
        else:
            return 2 * (-v - 1) + 1

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        a = node(l1)
        b = node(l2)
        # rule: a OR b
        # add edge (not a -> b) and (not b -> a)
        na = a ^ 1
        nb = b ^ 1
        graph[na].append(b)
        graph[nb].append(a)
        rgraph[b].append(na)
        rgraph[a].append(nb)

    # Kosaraju SCC
    order = []
    visited = [False] * size
    stack = []
    # iterative DFS
    for i in range(size):
        if not visited[i]:
            visited[i] = True
            stack.append((i, 0))
            while stack:
                v, idx = stack[-1]
                if idx < len(graph[v]):
                    w = graph[v][idx]
                    stack[-1] = (v, idx + 1)
                    if not visited[w]:
                        visited[w] = True
                        stack.append((w, 0))
                else:
                    stack.pop()
                    order.append(v)

    comp = [-1] * size
    c = 0
    for i in reversed(order):
        if comp[i] == -1:
            # BFS/DFS on reverse graph
            comp[i] = c
            stack2 = [i]
            while stack2:
                v = stack2.pop()
                for w in rgraph[v]:
                    if comp[w] == -1:
                        comp[w] = c
                        stack2.append(w)
            c += 1

    # Check satisfiability
    assignment = [0] * n
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
        assignment[i] = 1 if comp[2 * i] > comp[2 * i + 1] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

solve()