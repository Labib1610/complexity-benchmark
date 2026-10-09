import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # Build implication graph for 2-SAT.
    # Variable i (1-indexed): node 2*i is i=True, node 2*i+1 is i=False.
    # Literal v: if v>0 -> 2*v, if v<0 -> 2*(-v)+1
    # Clause (a or b): add edges ~a->b and ~b->a
    
    edges = [[] for _ in range(2 * n + 2)]
    
    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        
        # Encode literals
        if a > 0:
            la = 2 * a
            nla = 2 * a + 1
        else:
            la = 2 * (-a) + 1
            nla = 2 * (-a)
        
        if b > 0:
            lb = 2 * b
            nlb = 2 * b + 1
        else:
            lb = 2 * (-b) + 1
            nlb = 2 * (-b)
        
        edges[nla].append(lb)
        edges[nlb].append(la)
    
    # Tarjan's SCC
    index = 0
    indices = [0] * (2 * n + 2)
    lowlink = [0] * (2 * n + 2)
    on_stack = [False] * (2 * n + 2)
    stack = []
    comp = [0] * (2 * n + 2)
    comp_id = 0
    
    sys.setrecursionlimit(1 << 25)
    
    # Iterative Tarjan to avoid recursion limit issues
    for start in range(2, 2 * n + 2):
        if indices[start] != 0:
            continue
        # Stack of (node, iterator position)
        call_stack = [(start, 0)]
        while call_stack:
            v, pi = call_stack[-1]
            if pi == 0:
                index += 1
                indices[v] = index
                lowlink[v] = index
                stack.append(v)
                on_stack[v] = True
            if pi < len(edges[v]):
                w = edges[v][pi]
                call_stack[-1] = (v, pi + 1)
                if indices[w] == 0:
                    call_stack.append((w, 0))
                elif on_stack[w]:
                    if indices[w] < lowlink[v]:
                        lowlink[v] = indices[w]
            else:
                if lowlink[v] == indices[v]:
                    comp_id += 1
                    while True:
                        w = stack.pop()
                        on_stack[w] = False
                        comp[w] = comp_id
                        if w == v:
                            break
                call_stack.pop()
                if call_stack:
                    parent = call_stack[-1][0]
                    if lowlink[v] < lowlink[parent]:
                        lowlink[parent] = lowlink[v]
    
    # Check satisfiability
    for i in range(1, n + 1):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
    
    # Assign values
    assignment = [0] * (n + 1)
    for i in range(1, n + 1):
        # If comp[2*i] < comp[2*i+1], then 2*i is in a later SCC (topologically later)
        # In Tarjan, lower comp_id means later in topological order
        # We want to set literal to True if it appears later in topological order
        if comp[2 * i] < comp[2 * i + 1]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    print("YES")
    print(' '.join(str(assignment[i]) for i in range(1, n + 1)))

solve()