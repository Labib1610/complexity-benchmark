import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # 2-SAT: variables x_1..x_n (1-indexed)
    # literal i  -> node 2*i   (x_i = True)
    # literal ~i -> node 2*i+1 (x_i = False)
    # For variable i: 2*i is True, 2*i+1 is False.
    # literal_to_node(x): if x>0 -> 2*x (True), if x<0 -> 2*(-x)+1 (False)
    
    size = 2 * (n + 2)
    graph = [[] for _ in range(size)]
    
    def node(lit):
        if lit > 0:
            return 2 * lit       # x = True
        else:
            return 2 * (-lit) + 1  # x = False
    
    def neg(lit):
        return -lit
    
    def neg_node(nd):
        # node 2*i <-> 2*i+1
        return nd ^ 1
    
    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        # Pin releases if at least one prong triggered.
        # Prong x triggers if: x>0 and tumbler=1, or x<0 and tumbler=0.
        # So literal x means "tumbler |x| is set to (x>0 ? 1 : 0)".
        # Clause: (a OR b OR c)
        # Convert to 2-SAT: (a OR b) AND (a OR c) AND (b OR c)
        # Implication: ~a -> b, ~a -> c, ~b -> a, ~b -> c, ~c -> a, ~c -> b
        na, nb, nc = neg(a), neg(b), neg(c)
        pairs = [(na, b), (na, c), (nb, a), (nb, c), (nc, a), (nc, b)]
        for u, v in pairs:
            graph[node(u)].append(node(v))
    
    # Tarjan's SCC
    index_counter = [0]
    stack = []
    on_stack = [False] * size
    indices = [-1] * size
    lowlink = [0] * size
    scc_id = [-1] * size
    scc_count = [0]
    
    sys.setrecursionlimit(10000)
    
    def strongconnect(v):
        # iterative Tarjan to avoid recursion limit issues
        work = [(v, 0)]
        while work:
            node, pi = work[-1]
            if pi == 0:
                indices[node] = index_counter[0]
                lowlink[node] = index_counter[0]
                index_counter[0] += 1
                stack.append(node)
                on_stack[node] = True
            recurse = False
            neighbors = graph[node]
            for i in range(pi, len(neighbors)):
                w = neighbors[i]
                if indices[w] == -1:
                    work[-1] = (node, i + 1)
                    work.append((w, 0))
                    recurse = True
                    break
                elif on_stack[w]:
                    lowlink[node] = min(lowlink[node], indices[w])
            if recurse:
                continue
            # done processing node
            if lowlink[node] == indices[node]:
                while True:
                    w = stack.pop()
                    on_stack[w] = False
                    scc_id[w] = scc_count[0]
                    if w == node:
                        break
                scc_count[0] += 1
            work.pop()
            if work:
                parent = work[-1][0]
                lowlink[parent] = min(lowlink[parent], lowlink[node])
    
    for v in range(2, 2 * (n + 1)):
        if indices[v] == -1:
            strongconnect(v)
    
    # Check satisfiability
    assignment = [0] * (n + 1)
    for i in range(1, n + 1):
        t_node = 2 * i
        f_node = 2 * i + 1
        if scc_id[t_node] == scc_id[f_node]:
            print("NO")
            return
        # If t_node's SCC comes after f_node's SCC in topological order,
        # then t_node is True. Tarjan produces SCCs in reverse topological order,
        # so larger scc_id means earlier in topological order.
        assignment[i] = 1 if scc_id[t_node] > scc_id[f_node] else 0
    
    print("YES")
    print(' '.join(str(assignment[i]) for i in range(1, n + 1)))

solve()