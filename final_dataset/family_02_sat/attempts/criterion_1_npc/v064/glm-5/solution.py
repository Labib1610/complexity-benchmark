import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    clauses = []
    idx = 2
    for _ in range(m):
        a = int(data[idx]); b = int(data[idx+1]); c = int(data[idx+2])
        idx += 3
        clauses.append((a, b, c))
    
    # 2-SAT formulation:
    # For each clause (l1, l2, l3), at least one must be satisfied.
    # Equivalent to: NOT(l1) -> (l2 OR l3), NOT(l2) -> (l1 OR l3), NOT(l3) -> (l1 OR l2)
    # We add implications: NOT(li) -> lj for j != i, for each i.
    
    # Variable i (1-indexed): positive means active, negative means inactive.
    # Node encoding: 2*i for positive, 2*i+1 for negative (i from 0 to n-1)
    # Actually let's use: for variable v (1..n), node 2*(v-1) = true, 2*(v-1)+1 = false
    # Literal l: if l > 0, node = 2*(l-1); if l < 0, node = 2*(-l-1)+1
    # Negation: node ^ 1
    
    def lit_node(l):
        if l > 0:
            return 2 * (l - 1)
        else:
            return 2 * (-l - 1) + 1
    
    # Build implication graph
    size = 2 * n
    adj = [[] for _ in range(size)]
    radj = [[] for _ in range(size)]
    
    for (l1, l2, l3) in clauses:
        lits = [l1, l2, l3]
        for i in range(3):
            for j in range(3):
                if i != j:
                    # NOT(lits[i]) -> lits[j]
                    u = lit_node(lits[i]) ^ 1
                    v = lit_node(lits[j])
                    adj[u].append(v)
                    radj[v].append(u)
    
    # Kosaraju's SCC
    visited = [False] * size
    order = []
    for i in range(size):
        if not visited[i]:
            stack = [(i, 0)]
            while stack:
                node, ptr = stack.pop()
                if ptr == 0:
                    if visited[node]:
                        continue
                    visited[node] = True
                while ptr < len(adj[node]):
                    nxt = adj[node][ptr]
                    ptr += 1
                    if not visited[nxt]:
                        stack.append((node, ptr))
                        stack.append((nxt, 0))
                        break
                else:
                    order.append(node)
    
    comp = [-1] * size
    cid = 0
    for node in reversed(order):
        if comp[node] == -1:
            stack = [node]
            comp[node] = cid
            while stack:
                u = stack.pop()
                for v in radj[u]:
                    if comp[v] == -1:
                        comp[v] = cid
                        stack.append(v)
            cid += 1
    
    # Check satisfiability
    assignment = [0] * n
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
        assignment[i] = 1 if comp[2*i] > comp[2*i+1] else 0
    
    print("YES")
    print(" ".join(map(str, assignment)))

solve()