import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    idx = 2
    clauses = []
    for _ in range(m):
        c1 = int(data[idx]); c2 = int(data[idx+1]); c3 = int(data[idx+2])
        idx += 3
        clauses.append((c1, c2, c3))
    
    # 2-SAT: variable i (1-indexed) -> 2*i for positive, 2*i+1 for negative
    # literal c: if c>0 -> 2*c, if c<0 -> 2*(-c)+1
    # clause (a or b or c) = (!a -> b or c), (!b -> a or c), (!c -> a or b)
    # We add implications: !a -> b, !a -> c, !b -> a, !b -> c, !c -> a, !c -> b
    
    def lit(c):
        if c > 0:
            return 2*c
        else:
            return 2*(-c)+1
    
    def neg(l):
        return l ^ 1
    
    # Build graph
    size = 2*(n+1)
    graph = [[] for _ in range(size)]
    
    for c1, c2, c3 in clauses:
        a = lit(c1)
        b = lit(c2)
        c = lit(c3)
        # !a -> b, !a -> c
        graph[neg(a)].append(b)
        graph[neg(a)].append(c)
        # !b -> a, !b -> c
        graph[neg(b)].append(a)
        graph[neg(b)].append(c)
        # !c -> a, !c -> b
        graph[neg(c)].append(a)
        graph[neg(c)].append(b)
    
    # Tarjan's SCC
    index_counter = [0]
    stack = []
    lowlink = [0]*size
    index = [0]*size
    on_stack = [False]*size
    scc_id = [0]*size
    scc_count = [0]
    
    import sys
    sys.setrecursionlimit(1000000)
    
    def strongconnect(v):
        index[v] = index_counter[0]
        lowlink[v] = index_counter[0]
        index_counter[0] += 1
        stack.append(v)
        on_stack[v] = True
        
        for w in graph[v]:
            if index[w] == 0:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], index[w])
        
        if lowlink[v] == index[v]:
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc_id[w] = scc_count[0]
                if w == v:
                    break
            scc_count[0] += 1
    
    for v in range(2, 2*(n+1)):
        if index[v] == 0:
            strongconnect(v)
    
    # Check satisfiability
    assignment = [0]*(n+1)
    for i in range(1, n+1):
        pos = 2*i
        neg_lit = 2*i+1
        if scc_id[pos] == scc_id[neg_lit]:
            print("NO")
            return
        # If pos SCC > neg SCC (higher means later in topological order, i.e., comes after)
        # In Tarjan's, SCCs are numbered in reverse topological order
        # So lower scc_id means later in topological order (comes first)
        # We want to set the literal that appears first in topological order to false
        # i.e., if scc_id[pos] < scc_id[neg_lit], pos comes later in topo order, so set pos=true
        if scc_id[pos] < scc_id[neg_lit]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    print("YES")
    print(" ".join(str(assignment[i]) for i in range(1, n+1)))

solve()