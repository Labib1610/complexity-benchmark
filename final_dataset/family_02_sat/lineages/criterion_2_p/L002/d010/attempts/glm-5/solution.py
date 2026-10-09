import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    # Build implication graph: 2*n nodes, node 2*i = literal (i+1 is True), node 2*i+1 = literal (i+1 is False)
    # Literal encoding: positive c -> index c-1, value True (node 2*(c-1))
    #                  negative c -> index |c|-1, value False (node 2*(|c|-1)+1)
    
    edges = [[] for _ in range(2 * n)]
    
    for _ in range(m):
        c1 = int(next(it))
        c2 = int(next(it))
        
        # v1 = s_{|c1|} if c1>0 else 1-s_{|c1|}
        # v2 = s_{|c2|} if c2>0 else 1-s_{|c2|}
        # I = 1/3 iff v1 != v2 (one is 0, other is 1)
        # We need I != 1/3, so v1 == v2
        # v1 == v2 means: (c1>0 and c2>0) -> s_a == s_b
        #                (c1>0 and c2<0) -> s_a == 1-s_b, i.e., s_a != s_b
        #                (c1<0 and c2>0) -> 1-s_a == s_b, i.e., s_a != s_b
        #                (c1<0 and c2<0) -> 1-s_a == 1-s_b, i.e., s_a == s_b
        
        a = abs(c1) - 1
        b = abs(c2) - 1
        sign1 = 1 if c1 > 0 else -1
        sign2 = 1 if c2 > 0 else -1
        
        # v1 == v2
        # If sign1 == sign2: s_a == s_b
        # If sign1 != sign2: s_a != s_b
        
        if sign1 == sign2:
            # s_a == s_b
            # a True -> b True
            edges[2*a].append(2*b)
            # b True -> a True
            edges[2*b].append(2*a)
            # a False -> b False
            edges[2*a+1].append(2*b+1)
            # b False -> a False
            edges[2*b+1].append(2*a+1)
        else:
            # s_a != s_b
            # a True -> b False
            edges[2*a].append(2*b+1)
            # b False -> a True
            edges[2*b+1].append(2*a)
            # a False -> b True
            edges[2*a+1].append(2*b)
            # b True -> a False
            edges[2*b].append(2*a+1)
    
    # Tarjan's SCC
    setrecursionlimit(1 << 25)
    
    index_counter = [0]
    stack = []
    on_stack = [False] * (2 * n)
    indices = [-1] * (2 * n)
    lowlink = [0] * (2 * n)
    comp = [-1] * (2 * n)
    comp_id = 0
    
    import sys as _sys
    _sys.setrecursionlimit(1 << 25)
    
    # Iterative Tarjan to avoid recursion limit issues
    for start in range(2 * n):
        if indices[start] != -1:
            continue
        # iterative DFS
        work_stack = [(start, 0)]
        while work_stack:
            node, pi = work_stack[-1]
            if pi == 0:
                indices[node] = index_counter[0]
                lowlink[node] = index_counter[0]
                index_counter[0] += 1
                stack.append(node)
                on_stack[node] = True
            recurse = False
            neighbors = edges[node]
            while pi < len(neighbors):
                w = neighbors[pi]
                pi += 1
                if indices[w] == -1:
                    work_stack[-1] = (node, pi)
                    work_stack.append((w, 0))
                    recurse = True
                    break
                elif on_stack[w]:
                    lowlink[node] = min(lowlink[node], indices[w])
            if recurse:
                continue
            # Done with node
            if lowlink[node] == indices[node]:
                while True:
                    w = stack.pop()
                    on_stack[w] = False
                    comp[w] = comp_id
                    if w == node:
                        break
                comp_id += 1
            work_stack.pop()
            if work_stack:
                parent = work_stack[-1][0]
                lowlink[parent] = min(lowlink[parent], lowlink[node])
    
    # Check satisfiability
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
    
    # Assign values
    assignment = [0] * n
    for i in range(n):
        # If comp[2*i] < comp[2*i+1], then 2*i is in a later SCC (processed earlier in topological order)
        # In Tarjan, lower comp_id = later in topological order (processed first)
        # We want to set literal to True if its SCC comes later (lower comp_id)
        if comp[2*i] < comp[2*i+1]:
            assignment[i] = 1  # s_i = True
        else:
            assignment[i] = 0  # s_i = False
    
    print("YES")
    print(' '.join(map(str, assignment)))

solve()