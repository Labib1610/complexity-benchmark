import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # 2-SAT variables: asset i has literal i (buy) and ~i (sell)
    # We use 1-based indexing for assets.
    # Literal encoding: positive literal x -> 2*x, negative literal -x -> 2*x+1
    # Actually let's use: for asset i, var i is 0-indexed: 2*i = buy, 2*i+1 = sell
    # But let's keep 1-based for clarity: asset i -> 2*(i-1) and 2*(i-1)+1

    size = 2 * n
    graph = [[] for _ in range(size)]
    rev_graph = [[] for _ in range(size)]

    def lit_to_node(x):
        # x is non-zero integer, |x| in 1..n
        i = abs(x) - 1
        if x > 0:
            return 2 * i      # buy
        else:
            return 2 * i + 1  # sell

    def neg(node):
        return node ^ 1

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        a = lit_to_node(l1)
        b = lit_to_node(l2)
        # Report is valid unless both outcomes contradicted.
        # So we cannot have both a and b false.
        # Clause: (a OR b)
        # Implications: ~a -> b, ~b -> a
        na = neg(a)
        nb = neg(b)
        graph[na].append(b)
        graph[nb].append(a)
        rev_graph[b].append(na)
        rev_graph[a].append(nb)

    # Kosaraju's SCC
    order = []
    visited = [False] * size
    stack = []

    # Iterative DFS for order
    for i in range(size):
        if not visited[i]:
            stack.append((i, 0))
            while stack:
                node, idx = stack.pop()
                if idx == 0:
                    if visited[node]:
                        continue
                    visited[node] = True
                # process neighbors
                neighbors = graph[node]
                if idx < len(neighbors):
                    nxt = neighbors[idx]
                    stack.append((node, idx + 1))
                    if not visited[nxt]:
                        stack.append((nxt, 0))
                else:
                    order.append(node)

    visited = [False] * size
    comp = [-1] * size
    cid = 0

    for node in reversed(order):
        if not visited[node]:
            # DFS on rev_graph
            stack = [node]
            visited[node] = True
            component = []
            while stack:
                u = stack.pop()
                component.append(u)
                for v in rev_graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            for u in component:
                comp[u] = cid
            cid += 1

    # Check satisfiability
    assignment = [0] * n
    for i in range(n):
        buy = 2 * i
        sell = 2 * i + 1
        if comp[buy] == comp[sell]:
            print("NO")
            return
        # If comp[buy] > comp[sell], buy is in a later SCC (topologically later means true in standard Kosaraju)
        # In Kosaraju, SCCs are numbered in reverse topological order.
        # So higher comp id = earlier in topological order = false.
        # We want to set literal to true if its SCC comes later in topological order.
        # Actually standard: if comp[u] < comp[v] then u is topologically after v? 
        # Let's think: order list is built by finishing times. We process reversed(order).
        # The first SCC found (cid=0) is a sink in the condensation? No.
        # In Kosaraju, the first component found in the second pass is a source in the condensation graph.
        # Wait: second pass processes nodes in decreasing finishing time.
        # The node with highest finishing time is in a source SCC.
        # So comp id 0 is a source SCC.
        # In 2-SAT, we set a literal true if its SCC is topologically later (i.e., comes after in topological order).
        # Source SCCs come first, so they have smaller comp ids.
        # We set literal true if comp[lit] > comp[neg(lit)]? No.
        # Standard rule: if comp[x] < comp[~x], set x to true. Because smaller comp id = source side = earlier in topo order.
        # Hmm, let me recall: In Kosaraju as implemented, comp ids are assigned in order of discovery in second pass.
        # Second pass goes in decreasing finishing time, so it discovers source SCCs first.
        # So comp id 0 is a source. In topological order, sources come first.
        # A literal is set to true if it appears later in topological order than its negation.
        # Later in topo order = larger comp id? No, sources have small comp id and come first.
        # So larger comp id = later in topo order = true.
        # So: set buy=1 if comp[buy] > comp[sell].
        if comp[buy] > comp[sell]:
            assignment[i] = 1
        else:
            assignment[i] = 0

    print("YES")
    print(' '.join(map(str, assignment)))

solve()