import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # 2-SAT: variables 1..n, node 2*i = false(i), 2*i+1 = true(i)
    # We use 0-based: for var i (1..n): false = 2*(i-1), true = 2*(i-1)+1
    size = 2 * n
    head = [-1] * size
    to = []
    nxt = []
    
    def add_edge(u, v):
        to.append(v)
        nxt.append(head[u])
        head[u] = len(to) - 1
    
    # For requirement (l1, l2): at least one must be satisfied.
    # If l1 is false -> l2 must be true; if l2 is false -> l1 must be true.
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        v1 = abs(l1)
        s1 = 1 if l1 > 0 else 0
        v2 = abs(l2)
        s2 = 1 if l2 > 0 else 0
        
        # node indices
        # true node for v: 2*(v-1)+1, false node: 2*(v-1)
        n1_true = 2 * (v1 - 1) + 1
        n1_false = 2 * (v1 - 1)
        n2_true = 2 * (v2 - 1) + 1
        n2_false = 2 * (v2 - 1)
        
        a1 = n1_true if s1 else n1_false
        na1 = n1_false if s1 else n1_true
        a2 = n2_true if s2 else n2_false
        na2 = n2_false if s2 else n2_true
        
        # not a1 -> a2, not a2 -> a1
        add_edge(na1, a2)
        add_edge(na2, a1)
    
    # Tarjan's SCC
    index_counter = [0]
    stack = []
    on_stack = [False] * size
    index = [-1] * size
    lowlink = [0] * size
    scc_id = [-1] * size
    scc_count = [0]
    
    sys.setrecursionlimit(1 << 25)
    
    # Iterative Tarjan to avoid recursion limit issues
    for start in range(size):
        if index[start] != -1:
            continue
        # call stack: (node, iterator_state)
        call_stack = [(start, head[start])]
        while call_stack:
            node, edge_ptr = call_stack[-1]
            if edge_ptr == head[node] and index[node] == -1:
                index[node] = index_counter[0]
                lowlink[node] = index_counter[0]
                index_counter[0] += 1
                stack.append(node)
                on_stack[node] = True
            # explore edges
            advanced = False
            while edge_ptr != -1:
                w = to[edge_ptr]
                if index[w] == -1:
                    call_stack[-1] = (node, nxt[edge_ptr])
                    call_stack.append((w, head[w]))
                    advanced = True
                    break
                elif on_stack[w]:
                    if index[w] < lowlink[node]:
                        lowlink[node] = index[w]
                edge_ptr = nxt[edge_ptr]
            if advanced:
                continue
            # done with node
            if lowlink[node] == index[node]:
                while True:
                    w = stack.pop()
                    on_stack[w] = False
                    scc_id[w] = scc_count[0]
                    if w == node:
                        break
                scc_count[0] += 1
            call_stack.pop()
            if call_stack:
                parent = call_stack[-1][0]
                if lowlink[node] < lowlink[parent]:
                    lowlink[parent] = lowlink[node]
    
    # Check satisfiability
    for i in range(n):
        if scc_id[2 * i] == scc_id[2 * i + 1]:
            print("NO")
            return
    
    # Build assignment: if scc_id[true] < scc_id[false] in reverse topological order,
    # Tarjan gives SCCs in reverse topological order (higher scc_id = earlier in topo).
    # Standard: choose true if scc_id[true_node] < scc_id[false_node] is wrong;
    # Actually: SCCs are numbered in reverse topological order, so smaller scc_id = later in topo.
    # We want to set variable to true if true_node's SCC comes after false_node's SCC in topo,
    # i.e., scc_id[true] < scc_id[false] means true is later in topo -> set true.
    # Wait: Tarjan outputs SCCs in reverse topological order. So scc_id 0 is the last in topo.
    # A node should be true if its SCC is "greater" in topological order... 
    # Standard convention: set x = true if comp[true] < comp[false] (since lower comp = later in topo = stronger)
    # Let me just use: set true if scc_id[true] > scc_id[false] is the common convention...
    # Actually the common convention with Tarjan (which outputs reverse topo) is:
    # value = scc_id[true] < scc_id[false]
    
    result = []
    for i in range(n):
        true_node = 2 * i + 1
        false_node = 2 * i
        # In reverse topological order (Tarjan), smaller scc_id = later in topo order
        # We pick the one that appears later in topo (smaller scc_id) - this is the standard
        val = 1 if scc_id[true_node] < scc_id[false_node] else 0
        result.append(str(val))
    
    print("YES")
    print(" ".join(result))

solve()