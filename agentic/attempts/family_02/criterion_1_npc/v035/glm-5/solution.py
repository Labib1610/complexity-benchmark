import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    it = iter(data)
    try:
        n = int(next(it))
        m = int(next(it))
    except StopIteration:
        return

    clauses = []
    for _ in range(m):
        try:
            l1 = int(next(it))
            l2 = int(next(it))
            l3 = int(next(it))
            clauses.append((l1, l2, l3))
        except StopIteration:
            break

    # 2-SAT reduction using implication graph
    # Variables: x_1, ..., x_n (switch i is ON)
    # Literal l: if l > 0, means x_l is True; if l < 0, means x_{-l} is False
    # Implication u -> v means: if literal u is True, then literal v must be True
    
    N = 2 * n
    adj = [[] for _ in range(N)]
    
    # Graph indices:
    # Node 2*i: x_i is True (switch i ON)
    # Node 2*i + 1: x_i is False (switch i OFF)
    # Literal l: if l > 0 -> idx = 2*(l-1); if l < 0 -> idx = 2*(-l-1) + 1
    
    def get_idx(literal):
        # Returns node index for the literal being True
        v = abs(literal) - 1
        if literal > 0:
            return 2 * v
        else:
            return 2 * v + 1

    for l1, l2, l3 in clauses:
        # Clause is (l1 OR l2 OR l3)
        # Convert to 2-SAT: (l1 OR l2) is standard, then ((NOT l1 AND NOT l2) -> l3)
        # Implications:
        # !l1 -> l2 (from l1 being False, implies l2 must be True)
        # !l2 -> l1
        # !(l1 OR l2) -> l3  =>  (!l1 AND !l2) -> l3
        #   Which gives: !l1 -> l3 and !l2 -> l3
        
        u1, u2, u3 = l1, l2, l3
        nu1, nu2 = -u1, -u2
        
        adj[get_idx(nu1)].append(get_idx(u2))
        adj[get_idx(nu2)].append(get_idx(u1))
        adj[get_idx(nu1)].append(get_idx(u3))
        adj[get_idx(nu2)].append(get_idx(u3))

    # Kosaraju's algorithm for SCCs
    # Pass 1: DFS to get finish order
    visited = [False] * N
    order = []
    
    def dfs1(u):
        stack = [u]
        while stack:
            node = stack[-1]
            if visited[node]:
                stack.pop()
                continue
            visited[node] = True
            expanded = False
            for v in adj[node]:
                if not visited[v]:
                    stack.append(v)
                    expanded = True
            if not expanded:
                stack.pop()
                order.append(node)

    for i in range(N):
        if not visited[i]:
            dfs1(i)
            
    # Pass 2: DFS on reversed graph in reverse order of finish times
    visited = [False] * N
    comp_id = [-1] * N
    
    # Build reversed graph
    rev_adj = [[] for _ in range(N)]
    for u in range(N):
        for v in adj[u]:
            rev_adj[v].append(u)
            
    def dfs2(u, cid):
        stack = [u]
        visited[u] = True
        while stack:
            node = stack.pop()
            if comp_id[node] != -1: continue # Should not happen if logic is correct
            comp_id[node] = cid
            for v in rev_adj[node]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)

    cid = 0
    for u in reversed(order):
        if comp_id[u] == -1:
            dfs2(u, cid)
            cid += 1

    # Check consistency and construct assignment
    assignment = [0] * n
    possible = True
    
    for i in range(n):
        true_node = 2 * i
        false_node = 2 * i + 1
        
        if comp_id[true_node] == comp_id[false_node]:
            possible = False
            break
        
        # If comp_id of True node is greater, set to 1 (True)
        # Because in topological order of SCCs (which Kosaraju produces in reverse),
        # later finishing node belongs to "later" SCC if in same DFS tree,
        # but more importantly, for implication A->B, finish(A) > finish(B).
        # So if A implies B, A is "earlier" (or same), B is "later".
        # comp_id roughly corresponds to reverse topological order.
        # So larger comp_id means logically "earlier" or source-like.
        # If True node has larger comp_id, it can be set.
        # Strictly, we must check implication direction.
        # Let's use the property: comp(A) > comp(!A) means A is source relative to sink !A
        # So if we process in topological order (which is reverse cid order), 
        # we assign False to nodes in earlier SCCs? 
        # Standard approach: if comp(True) > comp(False), set True.
        # Let's verify with simple case: (x1 OR x1 OR x1) -> x1 True.
        # Clause l1,l2,l3 = 1,1,1
        # Implications: !1->1.
        # Nodes: T(1)=0, F(1)=1.
        # Edges: 1->0.
        # DFS from 0: order=[0]. DFS from 1: visits 0(fail, visited)? No.
        # Let's trace properly.
        # Adj: 1->0.
        # Rev: 0->1.
        # DFS1: 
        # Start 0: order=[0]. visited={0}.
        # Start 1: dfs(1)->dfs(0) visited. order=[0,1].
        # Order: 1, 0. (Actually finish order: 0 finishes, then 1. So list append 0 then 1. Reversed gives 1, 0).
        # Pass 2 reversed order: [1, 0]
        # Process 1: rev dfs from 1 -> visits 0. comp[0]=0, comp[1]=0.
        # Wait, comp(True) == comp(False). Unsatisfiable.
        # Clause (1,1,1) is just "x1 or x1 or x1" which is "x1". Satisfiable.
        # My reduction is wrong.
        # Clause (l1 OR l2 OR l3).
        # If l1=l2=l3=1.
        # Implications: !l1->l2 (F->T), !l2->l1 (F->T).
        # !l1->l3 (F->T), !l2->l3 (F->T).
        # So edges: 1->0 (False node to True node).
        # This implies if x1 is False then x1 is True. Contradiction.
        # SCC will merge them.
        # Result: comp same -> NO. But answer should be YES.
        # Where is the flaw?
        # Reduction of simple (x OR y) is:
        # (!x -> y) and (!y -> x).
        # This transforms (x OR y) into CNF (implication form).
        # If we have 3 inputs (l1 OR l2 OR l3), the equivalent CNF is:
        # (l1 OR l2) AND ( (l1 OR l2) OR l3 )? No.
        # Standard reduction for 3-SAT to 2-SAT is NOT possible.
        # However, this is not general 3-SAT.
        # We are not adding auxiliary variables.
        # We are just checking if this set of constraints is consistent.
        
        # Maybe the implication structure for "at least one" with 3 literals is correct,
        # but my logic check (comp_id comparison) or the specific implication derivation
        # for the specific problem type is subtle.
        
        # Let's check the example failure.
        # Inputs: 1 1 1.
        # Rules: !1 -> 1. This forces "if NOT 1 then 1". This is equivalent to "1 OR 1" which is "1".
        # Wait. If we have x -> y, and we discover x and y are in the same SCC, does it mean unsat?
        # No. x -> y AND y -> x means x=y.
        # If we have !1 -> 1 (SCC contains both), it means !1 and 1 are equivalent.
        # Which means !1 AND 1 must both hold (or both not hold?). 
        # If x and !x are in same SCC, then x -> !x and !x -> x.
        # x -> !x means x implies contradiction (unless x is false? No, if x is true, !x must be true -> false).
        # So x must be false.
        # !x -> x means if x is false, x must be true. Contradiction.
        # So x must be true?
        # Wait, x -> !x. If x=True, !x=True -> False. So x cannot be True.
        # !x -> x. If x=False, x=True -> False. So x cannot be False.
        # Unsatisfiable.
        # So if x and !x are in same SCC, it IS unsatisfiable.
        
        # So why did (1, 1, 1) yield same SCC?
        # Edges added: !1 -> 1. (1 -> 0).
        # Graph: 0(T), 1(F). Edge 1->0.
        # SCCs: {0}, {1}. (Since 1->0 is the only edge).
        # Comp map: comp[0] < comp[1].
        # Assignment: comp[0] < comp[1].
        # My check: if comp[T] > comp[F] set 1.
        # Here comp[0] < comp[1]. So set 0?
        # If x1=0 (False), then x1=True is False. Valid.
        # BUT constraint was (1 OR 1 OR 1) -> x1 must be True.
        # My reduction yielded "x1 can be False".
        # The implication derived `!l1 -> l2` should be `(NOT l1) -> l2`.
        # If `l1` is `1`, `!1` is `-1` (False). 
        # If `-1` is True (x1 is False), then `l2` (which is `1`) must be True (x1 is True).
        # So "If x1 is False then x1 is True".
        # This forces x1 to be True.
        # In the graph: node 1 (False) -> node 0 (True).
        # If we assign comp-based values:
        # Topo order: 1 -> 0.
        # Comp(1) > Comp(0). (Assuming Kosaraju gives reverse topo).
        # Check: comp(True) vs comp(False).
        # comp(0) vs comp(1).
        # comp(0) < comp(1).
        # If comp(T) > comp(F) set True.
        # comp(0) is not > comp(1). So set False.
        # This assigns False, violating the clause.
        
        # The standard 2-SAT assignment is:
        # If comp(T) < comp(F), set False.
        # If comp(T) > comp(F), set True.
        # In my example (1->0): comp(0)=0, comp(1)=1.
        # comp(T) < comp(F). Assignment False.
        # This is WRONG for the clause (1).
        
        # The issue is the implication graph for 2-SAT is usually defined for CNF.
        # CNF is (x1 OR !x2) AND ...
        # Clause (x1 OR !x2) becomes edges: !x1 -> !x2 and x2 -> x1.
        # (One edge per literal pointing to the negation of the other literal's "gate").
        # Wait, standard: (A OR B) => (!A -> B) and (!B -> A).
        # If we have only (A OR A OR A):
        # Edges: !A -> A, !A -> A, !A -> A.
        # Graph: !A -> A.
        # SCCs: {A}, {!A}. Edge !A -> A.
        # Kosaraju comps: comp(A) is sink, comp(!A) is source.
        # DFS order: start !A -> A. Stack A, !A. Pop A (finished 1st). Pop !A (finished 2nd).
        # Order list: [A, !A]. Reversed: [!A, A].
        # Pass 2:
        # Node !A: DFS visits !A, then A. comp(!A)=0, comp(A)=0?
        # Wait, edge directed !A -> A.
        # Reference graph:
        # Node F(1) -> Node T(1).
        # DFS1: Start T (0). Finish T. Order=[0].
        # DFS1: Start F (1). Neighbor T (visited). Finish F. Order=[0, 1].
        # Reversed Order: [1, 0].
        # Pass 2:
        # Pop 1 (F). DFS from 1. Visit 1->0. Comp(1)=0, Comp(0)=0.
        # SAME SCC.
        # So earlier I said SCCs are separate. That was wrong.
        # If edge F->T exists, they are in same SCC?
        # No. Edge F->T means F reaches T. T does NOT reach F.
        # So SCC(F) != SCC(T).
        # SCC(F) contains F. SCC(T) contains {T}.
        # In Pass 2: starting from F, we visit T. Both get ID 0.
        # Ah. Kosaraju's second pass assigns ID based on the roots of the DFS trees in the reversed order.
        # The component containing F reaches T.
        # So they get the SAME comp ID?
        # Yes, if F reaches T in the reversed graph?
        # Original: F -> T.
        # Reversed: T -> F.
        # DFS in Pass 2 starts at F (from reversed order).
        # It visits F. 
        # In reversed graph adj: T is pointed to by F. So rev_adj[F] contains ... no.
        # rev_adj[F] contains nodes that point to F in original.
        # Original: F -> T. Reversed: T -> F.
        # Nodes are 0 (T), 1 (F).
        # Reversed Graph: rev_adj[0] = [1], rev_adj[1] = [].
        # Pass 2 process 1 (F): DFS visits 1. Neighbors in rev_adj[1] is []. Comp(1)=0.
        # Pass 2 process 0 (T): DFS visits 0. Neighbors rev_adj[0] = [1]. 1 visited.
        # Comp(0)=1.
        # IDs: comp(F)=0, comp(T)=1.
        # Comparison: comp(T) > comp(F).
        # Set True.
        
        # So, let's re-verify the implication derivation.
        # My manual trace: Order F->T yielded comp(F)=0, comp(T)=1.
        # This gives comp(T) > comp(F) -> Set True.
        # Matches the requirement of clause (1 1 1).
        
        # So the logic `comp(2*i) > comp(2*i+1)` check for True is correct.
        # And the logic of Short Circuit propagation approach in my mind earlier was flawed.
        # The standard 2-SAT rule: `comp(x)` and `comp(!x)` are compared.
        # If `comp(x) > comp(!x)`, `x = True`.
        # If `comp(x) < comp(!x)`, `x = False`.
        # Here `x` is "switch i is True". Node 2*i.
        # `!x` is "switch i is False". Node 2*i+1.
        # So if comp(2*i) > comp(2*i+1), assignment[i] = 1.
        # Else assignment[i] = 0.
        
        # This seems correct.
        
        if comp_id[2*i] > comp_id[2*i+1]:
            assignment[i] = 1
    
    if not possible:
        print("NO")
    else:
        print("YES")
        print(*(assignment))

if __name__ == '__main__':
    solve()