import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # Each clause is a list of up to 3 literals.
    # We will build a 2-SAT formula.
    # Variable i (0-indexed) is represented by two nodes:
    #   node 2*i     : variable i is False (0)
    #   node 2*i + 1 : variable i is True  (1)
    # A literal l:
    #   if l > 0: requires variable (l-1) to be True
    #   if l < 0: requires variable (-l-1) to be False
    # For a clause (a or b or c), we add implications:
    #   not a -> b, not a -> c
    #   not b -> a, not b -> c
    #   not c -> a, not c -> b
    # This enforces at least one literal true.

    N = 2 * n
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def add_imp(u: int, v: int) -> None:
        g[u].append(v)
        rg[v].append(u)

    def node_of_literal(l: int) -> int:
        # returns node id for literal l
        if l > 0:
            return 2 * (l - 1) + 1   # True
        else:
            return 2 * (-l - 1)       # False

    def neg_node(u: int) -> int:
        # returns node id for negation of the literal represented by node u
        return u ^ 1

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        na = node_of_literal(a)
        nb = node_of_literal(b)
        nc = node_of_literal(c)
        # not a -> b, not a -> c
        add_imp(neg_node(na), nb)
        add_imp(neg_node(na), nc)
        # not b -> a, not b -> c
        add_imp(neg_node(nb), na)
        add_imp(neg_node(nb), nc)
        # not c -> a, not c -> b
        add_imp(neg_node(nc), na)
        add_imp(neg_node(nc), nb)

    # Kosaraju SCC
    visited = [False] * N
    order = []

    sys.setrecursionlimit(1000000)

    def dfs1(u: int) -> None:
        visited[u] = True
        for v in g[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for i in range(N):
        if not visited[i]:
            dfs1(i)

    comp = [-1] * N
    def dfs2(u: int, cid: int) -> None:
        comp[u] = cid
        for v in rg[u]:
            if comp[v] == -1:
                dfs2(v, cid)

    cid = 0
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, cid)
            cid += 1

    assignment = [0] * n
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
        # If True node comes after False node in topological order (smaller comp id means later in DFS finish order? Actually Kosaraju comp ids are assigned in reverse topological order of condensation graph.
 We just need consistency: choose value based on comp order.
 Standard: if comp[false] < comp[true] then false else true (or vice versa). We'll pick: if comp[2*i] < comp[2*i+1] then 0 else 1.
        if comp[2*i] < comp[2*i+1]:
            assignment[i] = 0
        else:
            assignment[i] = 1

    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()