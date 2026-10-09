import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    # Literal encoding: l > 0 means var l is true; l < 0 means var |l| is false
    # Node for literal l: 2*(|l|-1) + (0 if l>0 else 1) ... let's use l>0 -> 2*l-2, l<0 -> 2*(-l)-1
    # Actually simpler: map literal l to node id
    # For var i (1..n): literal +i -> 2*i, literal -i -> 2*i+1 (using 0-based or 1-based)
    # Let's use: literal l -> if l>0: 2*(l-1), if l<0: 2*(-l-1)+1
    # Negation: flip last bit
    
    size = 2 * n
    adj = [[] for _ in range(size)]
    radj = [[] for _ in range(size)]
    
    def node(l):
        if l > 0:
            return 2 * (l - 1)
        else:
            return 2 * (-l - 1) + 1
    
    for _ in range(m):
        l1 = int(input_data[idx]); idx += 1
        l2 = int(input_data[idx]); idx += 1
        # clause (l1 or l2): -l1 -> l2, -l2 -> l1
        u = node(-l1)
        v = node(l2)
        adj[u].append(v)
        radj[v].append(u)
        u = node(-l2)
        v = node(l1)
        adj[u].append(v)
        radj[v].append(u)
    
    # Kosaraju's SCC
    visited = [False] * size
    order = []
    
    sys.setrecursionlimit(1 << 25)
    
    # Iterative DFS to avoid recursion limit issues
    for start in range(size):
        if visited[start]:
            continue
        stack = [(start, 0)]
        visited[start] = True
        while stack:
            v, i = stack[-1]
            if i < len(adj[v]):
                w = adj[v][i]
                stack[-1] = (v, i + 1)
                if not visited[w]:
                    visited[w] = True
                    stack.append((w, 0))
            else:
                stack.pop()
                order.append(v)
    
    visited2 = [False] * size
    comp = [-1] * size
    
    for start in reversed(order):
        if visited2[start]:
            continue
        stack = [start]
        visited2[start] = True
        c = []
        while stack:
            v = stack.pop()
            c.append(v)
            for w in radj[v]:
                if not visited2[w]:
                    visited2[w] = True
                    stack.append(w)
        cid = comp[c[0]]
        if cid == -1:
            cid = len(c)  # just a marker, we'll reassign
        for v in c:
            comp[v] = start  # use start as component id
    
    # Reassign component ids properly
    comp_id = {}
    cid_counter = 0
    comp2 = [0] * size
    for v in range(size):
        if comp[v] not in comp_id:
            comp_id[comp[v]] = cid_counter
            cid_counter += 1
        comp2[v] = comp_id[comp[v]]
    
    # Check satisfiability: for each var i, literal +i and -i must be in different SCCs
    # and comp(+i) > comp(-i) means +i is true (since we process in reverse topological order)
    # Actually in Kosaraju, order of SCC assignment: first assigned SCC is last in topological order
    # comp2[v] smaller = later in topological order... let me think.
    # In Kosaraju, SCCs are found in reverse topological order. So first found = last topo.
    # comp2 values: first found has smallest id. So smaller comp2 = later in topo order.
    # For 2-SAT, we set literal true if its SCC comes later in topo order (smaller comp2 id).
    
    assignment = [0] * (n + 1)
    for i in range(1, n + 1):
        pos = node(i)       # literal +i
        neg = node(-i)      # literal -i
        if comp2[pos] == comp2[neg]:
            print("NO")
            return
        # +i is true if comp2[pos] < comp2[neg] (pos in later topo order)
        if comp2[pos] < comp2[neg]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    print("YES")
    print(" ".join(str(assignment[i]) for i in range(1, n + 1)))

solve()