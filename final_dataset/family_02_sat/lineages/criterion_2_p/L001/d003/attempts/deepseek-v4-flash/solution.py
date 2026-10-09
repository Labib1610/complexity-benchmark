import sys
sys.setrecursionlimit(10**6)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    # 2-SAT: variable i -> 2*i for False, 2*i+1 for True
    # We'll use 0-based indexing for variables: 0..n-1
    N = 2 * n
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def add_imp(u, v):
        g[u].append(v)
        rg[v].append(u)

    for _ in range(m):
        a, b = map(int, input().split())
        # literal: positive -> True, negative -> False
        # Convert to node index
        def lit_to_node(lit):
            var = abs(lit) - 1
            if lit > 0:
                return 2 * var + 1  # True
            else:
                return 2 * var      # False

        u = lit_to_node(a)
        v = lit_to_node(b)
        # Clause (u OR v) => (!u -> v) and (!v -> u)
        add_imp(u ^ 1, v)
        add_imp(v ^ 1, u)

    # Tarjan SCC
    index = 0
    indices = [-1] * N
    lowlink = [0] * N
    onstack = [False] * N
    stack = []
    comp = [-1] * N
    comp_count = 0

    def strongconnect(v):
        nonlocal index, comp_count
        indices[v] = lowlink[v] = index
        index += 1
        stack.append(v)
        onstack[v] = True

        for w in g[v]:
            if indices[w] == -1:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif onstack[w]:
                lowlink[v] = min(lowlink[v], indices[w])

        if lowlink[v] == indices[v]:
            while True:
                w = stack.pop()
                onstack[w] = False
                comp[w] = comp_count
                if w == v:
                    break
            comp_count += 1

    for v in range(N):
        if indices[v] == -1:
            strongconnect(v)

    # Check satisfiability
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return

    # Build assignment: choose value based on SCC order (comp id)
    # In Kosaraju/Tarjan, comp ids are in reverse topological order of condensation.
    # We assign True if comp[2*i] > comp[2*i+1] (since comp ids are assigned in reverse topological order)
    assignment = [0] * n
    for i in range(n):
        # comp[2*i] is False node, comp[2*i+1] is True node
        if comp[2*i] > comp[2*i+1]:
            assignment[i] = 1  # True
        else:
            assignment[i] = 0  # False

    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    solve()