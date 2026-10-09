import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # 2-SAT with n variables, each variable has two literals: x (upgraded) and -x (legacy)
    # We use 0-based indexing: literal x -> node 2*(x-1) for positive, 2*(x-1)+1 for negative
    # Actually let's map: for variable i (1..n), positive literal i -> 2*i, negative -> 2*i+1
    # But to save memory, use 2*n nodes: var i positive = 2*(i-1), negative = 2*(i-1)+1

    size = 2 * n
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
        # Policy: (a OR b)
        # Add implication: not a -> b, not b -> a
        # Literal encoding: positive x -> 2*(x-1), negative -x -> 2*(-x-1)+1
        def lit(val):
            if val > 0:
                return 2 * (val - 1)
            else:
                return 2 * (-val - 1) + 1
        def neg(val):
            if val > 0:
                return 2 * (val - 1) + 1
            else:
                return 2 * (-val - 1)
        
        na = neg(a)
        nb = neg(b)
        la = lit(a)
        lb = lit(b)
        add_edge(na, lb)
        add_edge(nb, la)

    # Tarjan's SCC
    index = 0
    indices = [-1] * size
    lowlink = [0] * size
    onstack = [False] * size
    stack = []
    comp = [-1] * size
    comp_count = 0

    sys.setrecursionlimit(1 << 25)
    
    # Iterative Tarjan to avoid recursion limit issues
    for start in range(size):
        if indices[start] != -1:
            continue
        # iterative DFS
        work = [(start, 0)]
        while work:
            v, pi = work[-1]
            if pi == 0:
                indices[v] = index
                lowlink[v] = index
                index += 1
                stack.append(v)
                onstack[v] = True
            e = head[v]
            found = False
            # resume from pi-th edge
            # we need to iterate edges; since we use adjacency list with arrays, 
            # we can't easily resume. Let's use a different approach.
            break
        
        # Actually, let's implement properly with iterative DFS using explicit edge pointers
        # We'll use a call stack approach
    
    # Reimplement properly
    indices = [-1] * size
    lowlink = [0] * size
    onstack = [False] * size
    stack = []
    comp = [-1] * size
    comp_count = 0
    index_counter = 0
    
    for start in range(size):
        if indices[start] != -1:
            continue
        # iterative DFS with explicit state
        dfs_stack = [(start, head[start])]
        indices[start] = index_counter
        lowlink[start] = index_counter
        index_counter += 1
        stack.append(start)
        onstack[start] = True
        
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
                    onstack[w] = True
                    dfs_stack.append((w, head[w]))
                elif onstack[w]:
                    if indices[w] < lowlink[v]:
                        lowlink[v] = indices[w]
            else:
                dfs_stack.pop()
                if lowlink[v] == indices[v]:
                    while True:
                        w = stack.pop()
                        onstack[w] = False
                        comp[w] = comp_count
                        if w == v:
                            break
                    comp_count += 1
                if dfs_stack:
                    parent = dfs_stack[-1][0]
                    if lowlink[v] < lowlink[parent]:
                        lowlink[parent] = lowlink[v]

    # Check satisfiability
    assignment = [0] * n
    for i in range(n):
        pos = 2 * i
        neg = 2 * i + 1
        if comp[pos] == comp[neg]:
            print("NO")
            return
        # If comp[pos] < comp[neg], pos is in a later SCC (topologically later means true)
        # In Tarjan, lower comp index = later in topological order (finished later)
        # Actually in Tarjan's algorithm, SCCs are numbered in reverse topological order
        # So comp with smaller index is later in topological order -> should be assigned true
        assignment[i] = 1 if comp[pos] < comp[neg] else 0

    print("YES")
    print(' '.join(map(str, assignment)))

solve()