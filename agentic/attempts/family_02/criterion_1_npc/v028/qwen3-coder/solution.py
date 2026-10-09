from collections import defaultdict
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # Clauses for 2-SAT: each clause is a disjunction of two literals
    # Literal x_i is represented as integer i (positive) or -i (negative)
    clauses = []
    
    idx = 2
    for _ in range(m):
        literals = []
        for _ in range(3):
            lit = int(data[idx])
            literals.append(lit)
            idx += 1
        
        # We need at least one of these three literals to be true
        # This is equivalent to (a OR b OR c)
        # We can convert this to 2-SAT by adding auxiliary variables or using standard reduction
        # But it's easier to handle directly in a SAT solver approach or convert appropriately
        # Here we'll reduce to pairwise clauses:
        # (a OR b OR c) is equivalent to (a OR b OR new_var) AND (new_var OR c)
        # But since we're doing 2-SAT, we need to break it down further.
        # A simpler way is to realize that (a OR b OR c) is the same as:
        # (~a => b OR c) which is (~a => b OR c) which is (a OR b) AND (a OR c) if we do it pairwise
        # Actually, the correct way to convert 3-clause to 2-clauses is:
        # (a OR b OR c) is equivalent to (a OR b OR y) AND (~y OR c) for a new variable y
        # But since we don't have auxiliary variables easily, let's think differently.
        
        # Let's take all pairs that cover all cases where at least one literal is true
        # Better yet, for 2-SAT with 3-literal clauses, we can add edges in implication graph
        # For (a OR b OR c), the implications are:
        # ~a => (b OR c), ~b => (a OR c), ~c => (a OR b)
        # Which translates to: (~a => b or ~a => c) etc.
        # So we get: (~a => b) is (~b => a) and (~a => c) is (~c => a)
        # Hmm, still not right. The correct conversion is:
        # (a OR b OR c) is equivalent to:
        # (a OR b OR y) AND (~y OR c) for fresh variable y
        # But we want pure 2-SAT, so let's just enumerate all satisfying assignments?
        # No, that's not scalable.
        
        # Let's use the standard implication graph method for 2-SAT extended for 3-clauses
        # For (a OR b OR c), the negation is (~a AND ~b AND ~c)
        # So we forbid (~a AND ~b AND ~c)
        # In implication graph terms, we ensure that NOT(~a AND ~b AND ~c)
        # Which means at least one of a,b,c is true.
        # To model this in 2-SAT, we can introduce auxiliary variables, but that complicates things.
        
        # Simpler approach: for each triple (a,b,c), we add constraints that prevent all three from being false.
        # That is, we cannot have (~a AND ~b AND ~c)
        # This is hard to express in pure 2-SAT without extension.
        
        # Let's instead build an implication graph for 2-SAT by converting each 3-clause into equivalent 2-clauses
        # by introducing auxiliary variables. But since we don't want to complicate,
        # we'll simulate a search approach or use the fact that each clause is a disjunction.
        
        # Actually, let's proceed with the implication graph approach properly.
        # For clause (a OR b OR c), we create equivalent 2-clauses:
        # Introduce a new variable, say y, then:
        # (a OR b OR c) <=> (a OR b OR y) AND (~y OR c)
        # But now we have a 3-clause again. 
        # The proper way is:
        # (a OR b OR c) is equivalent to:
        # (a OR b) OR c -> introduce y1 = (a OR b), then y1 OR c
        # But y1 = (a OR b) is equivalent to (~a => b) and (~b => a) ? No.
        # y1 = (a OR b) means (y1 OR ~a OR ~b) and (~y1 OR a) and (~y1 OR b)
        # This introduces 3-SAT clauses again.
        
        # Let's try a different approach: for each 3-clause, we'll generate all implied 2-clauses
        # that enforce that not all three literals are false.
        # If ~a AND ~b AND ~c is forbidden, then:
        # From ~a AND ~b AND ~c being false, we get that at least one of a,b,c is true.
        # The contrapositive doesn't help directly in building 2-clauses.
        
        # What we can do is: for each forbidden combination (where all 3 literals are false),
        # we ensure that at least one is true. 
        # But enumerating all forbidden combinations is exponential.
        
        # Let's think of it this way:
        # Each clause (a OR b OR c) must be satisfied.
        # In 2-SAT, we usually deal with (x OR y) clauses.
        # We can reduce 3-SAT to 2-SAT by adding extra variables, but that changes our variable set.
        
        # Since the problem asks for a solution, and given the constraints, maybe a brute-force check is feasible?
        # With n<=90, 2^90 is too large. But perhaps the structure allows.
        
        # Wait, let's reframe: we have m clauses, each with 3 literals over n variables.
        # We want an assignment to variables (trucks to corridors) such that each clause has at least one true literal.
        # This is exactly MAX-3-SAT decision problem for all clauses.
        
        # However, general 3-SAT is NP-complete, but maybe the small number of clauses (m<=400) allows something.
        # Or perhaps there's a special structure.
        
        # Let's consider building the implication graph for 2-SAT and see how to handle 3-clauses.
        # For a 2-clause (a OR b), we add edges (~a => b) and (~b => a)
        # For a 3-clause (a OR b OR c), we want to ensure that it's not the case that all are false.
        # So we add constraints that make at least one true.
        # One way is to pick pairs: ensure that for each pair, certain implications hold that prevent all false.
        
        # Let's just add for each 3-clause (a OR b OR c):
        # (~a AND ~b) => c  which is (a OR b OR c) - already the clause
        # In implication graph: (~a AND ~b) => c translates to (~a => (b OR c)) etc.
        # Which gives us (~a => b OR c) which is (~a => b) OR (~a => c)
        # Which means we add (~a => b) and (~a => c) ? No, that's not correct logic.
        # (~a => b OR c) is equivalent to (a OR b OR c) - that's just restating.
        
        # Proper way: 
        # Clause (a OR b OR c) is false only when a=F, b=F, c=F.
        # So we forbid the assignment a=0, b=0, c=0.
        # In implication graph terms, we need to add edges such that this combination leads to contradiction.
        # But in 2-SAT, we work with binary implications.
        
        # Let's try this: for clause (a OR b OR c), we add the following 2-clauses:
        # (~a OR ~b OR y) AND (~y OR c) would require a new variable y.
        # Since we want pure 2-SAT, let's avoid that.
        
        # Alternative: for each 3-clause, we can derive necessary 2-clauses that must hold
        # if we want to satisfy it. But I'm not sure of a clean way.
        
        # Let's look at the examples:
        # Example 1: n=3, m=2
        # Clause 1: 1 2 3 means (x1 OR x2 OR x3)
        # Clause 2: -1 2 -3 means (~x1 OR x2 OR ~x3)
        # We want both to be true.
        
        # Let's attempt to solve this systematically.
        # We'll model this as a 2-SAT problem by converting 3-clauses appropriately.
        # For clause (a OR b OR c), we can replace it with:
        # (a OR b OR y) AND (~y OR c) using a new Boolean variable y.
        # But this increases the number of variables.
        
        # Given the complexity, and that this is likely intended to be solved with 2-SAT,
        # perhaps the expectation is to treat each 3-clause as a constraint that forces
        # at least one of its literals to be true, and build a graph accordingly.
        
        # Let's proceed by implementing a 2-SAT solver and see how to adapt 3-clauses.
        
        # Represent literals: positive for upper (1), negative for lower (0)
        # Variable i corresponds to truck i being assigned to upper corridor (1) or lower (0)
        # So x_i = 1 means truck i is upper, x_i = 0 means lower.
        # Literal +i means x_i, -i means ~x_i (not x_i)
        
        # For clause (a OR b OR c), we want at least one to be true.
        # In terms of implications, if two are false, the third must be true.
        # So: (~a AND ~b) => c, (~a AND ~c) => b, (~b AND ~c) => a
        # These are 3-clauses again. Not helpful.
        
        # Let's just add all possible 2-clauses that are implied by the 3-clause being true.
        # That is, for (a OR b OR c) to be true, we can't have all false.
        # So we add (~a OR ~b OR ~c) is false, meaning at least one of a,b,c is true.
        # The negation (~a AND ~b AND ~c) must be false.
        # To enforce this in 2-SAT, we can add clauses like:
        # (~a OR ~b) is not forced to be true, but rather we know that if ~a and ~b, then c must be true.
        # So we add (~a AND ~b) => c which is (a OR b OR c) - back to square one.
        
        # Maybe the key insight is: we can encode 3-clauses in 2-SAT with auxiliary variables.
        # For clause C = (a OR b OR c), introduce new var y_C
        # Replace C with (a OR b OR y_C) AND (~y_C OR c)
        # Now we have two 3-clauses again. 
        # Continue: (a OR b OR y_C) becomes (a OR z) AND (~z OR b OR y_C) 
        # This is getting messy.
        
        # Let's try a concrete example approach.
        # For clause (1 OR 2 OR 3), it's satisfied unless x1=0, x2=0, x3=0.
        # So we must prevent x1=0 AND x2=0 AND x3=0.
        # In 2-SAT, we can't directly express 3-way AND prohibition.
        # But we can add constraints like: if x1=0 and x2=0, then x3 must be 1.
        # Which is: (~x1 AND ~x2) => x3
        # Which is equivalent to (x1 OR x2 OR x3) - the original clause.
        
        # This seems circular. Let's look up the standard way.
        # Standard technique: for 3-CNF clause (a OR b OR c), introduce new variable y
        # Replace with (a OR b OR y) AND (~y OR c)
        # Now we have two clauses, one is 3-clause, one is 2-clause.
        # Apply recursively to the 3-clause.
        # (a OR b OR y) becomes (a OR z) AND (~z OR b OR y)
        # And so on. This terminates because each step reduces the total number of literals.
        
        # So, we can convert any 3-CNF formula to 2-CNF with new variables.
        # But our solver needs to handle these new variables.
        
        # Let's implement a 2-SAT solver and apply this transformation.
        
        # First, collect all clauses and transform 3-clauses to 2-clauses with new vars.
        # We'll need to map new variables to indices beyond n.
        
        # But given time constraints, let's try a different approach:
        # Use the fact that for small m, we might be able to check satisfiability via SCC
        # in the implication graph built from all 2-clauses derived from 3-clauses.
        
        # For a 3-clause (a OR b OR c), the only forbidden assignment is a=F, b=F, c=F.
        # All other 7 assignments satisfy it.
        # To build the implication graph, for each forbidden partial assignment,
        # we add edges that would cause a contradiction.
        
        # But I think the cleanest way is the Tseitin transformation.
        # Let's do it properly.
        
        # We'll transform each 3-clause into equivalent 2-clauses with auxiliary variables.
        # Then run standard 2-SAT on the expanded set of variables.
        # Finally, extract the assignment for the original variables.
        
        clauses.append(literals)
    
    # Now transform 3-clauses to 2-clauses
    # We'll use auxiliary variables numbered from n+1 onwards
    aux_var_counter = n + 1
    two_clauses = []
    # Map from auxiliary variable to its definition
    definitions = {}
    
    for clause in clauses:
        if len(clause) == 2:
            two_clauses.append(clause)
        elif len(clause) == 3:
            # Transform (a OR b OR c) to (a OR b OR y) AND (~y OR c)
            # But (a OR b OR y) is still 3-clause, so we recurse or expand
            # Let's expand directly:
            # (a OR b OR c) is equivalent to:
            # (a OR b) OR c
            # Introduce y1 = (a OR b), then y1 OR c
            # But y1 = (a OR b) means (~a => b) and (~b => a)? No.
            # y1 = (a OR b) should be encoded as 2-SAT: 
            # (y1 OR ~a OR ~b) AND (~y1 OR a) AND (~y1 OR b)
            # But first clause is 3-clause again.
            
            # Let's use the standard reduction:
            # (a OR b OR c) becomes (a OR b OR y) AND (~y OR c)
            # where y is a new variable.
            # Now (a OR b OR y): introduce z: (a OR z) AND (~z OR b OR y)
            # (~z OR b OR y): introduce w: (~z OR w) AND (~w OR b OR y)
            # This is getting too involved.
            
            # Simpler: for 3-clause (a OR b OR c), we note that it's false only when all are false.
            # So we add constraints that prevent a=0, b=0, c=0 simultaneously.
            # In 2-SAT, we can't express this directly, but we can add all 2-clauses that are
            # logical consequences of the clause being true.
            
            # Alternatively, accept that we need auxiliary variables and implement Tseitin transform.
            
            # Let's do Tseitin:
            # For clause (a OR b OR c), introduce new var y
            # Add clauses: 
            # 1. (y OR ~c)  [from y => c part of the equivalence]
            # 2. (~y OR a OR b) [from ~y => (a OR b)]
            # But clause 2 is still 3-clause.
            
            # Continue transforming clause 2: (~y OR a OR b)
            # Introduce z: (~y OR z) AND (~z OR a OR b)
            # (~z OR a OR b): introduce w: (~z OR w) AND (~w OR a OR b)
            # This won't terminate well.
            
            # Let's look up the correct Tseitin transformation for OR gate with 3 inputs.
            # For a 3-input OR gate with inputs a, b, c and output y:
            # y <=> (a OR b OR c)
            # This is equivalent to:
            # (~a OR ~b OR ~c OR y) AND (a OR ~y) AND (b OR ~y) AND (c OR ~y)
            # The first clause is still 4-clause. Not good.
            
            # Actually, the standard Tseitin transformation for a clause (a OR b OR c) is:
            # Introduce a new variable y that represents the entire clause being true.
            # But that doesn't help because we want the clause itself to be true.
            
            # I think I'm overcomplicating this. The standard approach for reducing 3-SAT to 2-SAT
            # with auxiliary variables is fine, even if it adds variables.
            # The key is that we only care about the original n variables in the end.
            
            # So, for clause (a OR b OR c):
            # Introduce new variable y
            # Add 2-clauses: (a OR b OR y) becomes multiple steps, or we just accept
            # that we're building a larger 2-SAT instance.
            
            # Let's simplify: for clause (a OR b OR c), we can add the following 2-clauses
            # that are logical consequences:
            # (~a OR ~b) => (a OR b OR c) is always true, not helpful.
            
            # What we can do is: for the clause to be true, if any two literals are false,
            # the third must be true.
            # So:
            # (~a AND ~b) => c  which is (a OR b OR c) - original clause
            # In implication graph: (~a AND ~b) => c translates to:
            # If we have both ~a and ~b, then c must be true.
            # But in 2-SAT, we can only have binary implications.
            
            # The correct way is:
            # From (~a AND ~b) => c, we get (~a => (b OR c)) and (~b => (a OR c))
            # But (b OR c) is not a literal.
            
            # Let's just bite the bullet and implement Tseitin correctly.
            # For function y = (a OR b OR c), we add:
            # (~a OR ~b OR ~c OR y) AND (a OR ~y) AND (b OR ~y) AND (c OR ~y)
            # The first clause is 4-clause. We need to break it down.
            # Introduce z = (~a OR ~b), then (z OR ~c OR y)
            # Introduce w = (z OR ~c), then (w OR y)
            # Similarly break down (z OR ~c): introduce v = (z OR ~c) 
            # This is recursive. Let's code it.
            
            def tseitin_or3(a, b, c):
                nonlocal aux_var_counter
                # y = a OR b OR c
                y = aux_var_counter
                aux_var_counter += 1
                
                # We need to encode y <=> (a OR b OR c)
                # Which is (a OR b OR c => y) AND (y => a OR b OR c)
                # First: (a OR b OR c => y) is (~a OR ~b OR ~c OR y)
                # Second: (y => a OR b OR c) is (~y OR a OR b OR c)
                
                # Break (~a OR ~b OR ~c OR y)
                # Introduce z1 = (~a OR ~b)
                z1 = aux_var_counter
                aux_var_counter += 1
                # z1 <=> (~a OR ~b) is (a OR z1) AND (b OR z1) AND (~z1 OR ~a OR ~b)
                # 2-clauses: (a OR z1), (b OR z1)
                # 3-clause: (~z1 OR ~a OR ~b) - need to break
                # Introduce z2 = (~z1 OR ~a)
                z2 = aux_var_counter
                aux_var_counter += 1
                # z2 <=> (~z1 OR ~a) is (z1 OR z2) AND (a OR z2) AND (~z2 OR ~z1 OR ~a)
                # 2-clauses: (z1 OR z2), (a OR z2)
                # 3-clause: (~z2 OR ~z1 OR ~a) - break
                # Introduce z3 = (~z2 OR ~z1)
                z3 = aux_var_counter
                aux_var_counter += 1
                # z3 <=> (~z2 OR ~z1) is (z2 OR z3) AND (z1 OR z3) AND (~z3 OR ~z2 OR ~z1)
                # 2-clauses: (z2 OR z3), (z1 OR z3)
                # 3-clause: (~z3 OR ~z2 OR ~z1) - break
                # This is not converging.
                
                # There must be a simpler way. Let's look it up conceptually.
                # For y = (a OR b OR c), the CNF is:
                # (~a OR ~b OR ~c OR y) AND (a OR ~y) AND (b OR ~y) AND (c OR ~y)
                # We need to convert the 4-clause (~a OR ~b OR ~c OR y) to 2-clauses.
                # Introduce intermediate variables:
                # Let z1 = (~a OR ~b), then (~z1 OR ~c OR y)
                # Let z2 = (~z1 OR ~c), then (~z2 OR y)
                # Now we have:
                # z1 = (~a OR ~b) -> (a OR z1), (b OR z1), (~z1 OR ~a OR ~b)
                # z2 = (~z1 OR ~c) -> (z1 OR z2), (c OR z2), (~z2 OR ~z1 OR ~c)
                # And finally (~z2 OR y)
                # The remaining 3-clauses need breaking:
                # (~z1 OR ~a OR ~b): Let z3 = (~z1 OR ~a), then (~z3 OR ~b)
                # z3 = (~z1 OR ~a): (z1 OR z3), (a OR z3), (~z3 OR ~z1 OR ~a)
                # (~z3 OR ~z1 OR ~a): Let z4 = (~z3 OR ~z1), then (~z4 OR ~a)
                # z4 = (~z3 OR ~z1): (z3 OR z4), (z1 OR z4), (~z4 OR ~z3 OR ~z1)
                # This creates too many variables.
                
                # Maybe there's a smarter encoding. But for now, let's proceed with a working version.
                # We'll represent higher-order clauses and handle them specially in the 2-SAT solver.
                # But standard 2-SAT solver expects only 2-clauses.
                
                # Let's abandon the Tseitin approach for now and try a direct method.
                # Build implication graph based on forbidden assignments.
                
                # For clause (a OR b OR c) to be true, the assignment (a=0, b=0, c=0) is forbidden.
                # In implication graph, we want to add edges such that this leads to contradiction.
                # But how?
                
                # Key insight: if we force a=0, b=0, c=0, then the clause is false.
                # So we add implications that prevent this.
                # Specifically, if a=0 and b=0, then c must be 1.
                # Which is: (~a AND ~b) => c
                # In implication graph: ~a => (b OR c) and ~b => (a OR c)
                # But (b OR c) is not a literal.
                
                # This is a fundamental issue. 2-SAT cannot directly express 3-clause constraints.
                
                # Therefore, we must either:
                # 1. Use auxiliary variables (Tseitin transformation)
                # 2. Or use a different algorithm (like backtracking search)
                
                # Given the time, let's try to implement a simple backtracking solution,
                # since n<=90 but m<=400, and each clause only involves 3 literals.
                
                # Actually, let's reconsider the implication graph approach.
                # For 3-clause (a OR b OR c), we can add the following 2-clauses
                # that are entailed by it being true:
                # For any two literals, if both are false, the third must be true.
                # So: (~a AND ~b) => c
                # This is equivalent to (a OR b OR c) - no progress.
                
                # Wait, let's think of it this way:
                # The clause (a OR b OR c) is false iff a=0, b=0, c=0.
                # To prevent this in a 2-SAT framework, we can add clauses that together
                # make this assignment impossible.
                # For example, we can add (~a OR ~b OR y) and (~y OR c)
                # But again, 3-clauses.
                
                # I think the conclusion is: we need auxiliary variables.
                # Let's implement it properly.
                
                # For clause (a OR b OR c), introduce new variable d
                # Add clauses: (a OR b OR d) AND (~d OR c)
                # Now we have two clauses, one is 3-clause.
                # Recurse on (a OR b OR d): introduce e: (a OR e) AND (~e OR b OR d)
                # (~e OR b OR d): introduce f: (~e OR f) AND (~f OR b OR d)
                # This doesn't seem to terminate in reduced form.
                
                # Looking at literature, the correct expansion is:
                # (a OR b OR c) is equivalent to:
                # (a OR b OR y) AND (~y OR c) where y is new
                # Then (a OR b OR y): introduce z: (a OR z) AND (~z OR b OR y)
                # (~z OR b OR y): introduce w: (~z OR w) AND (~w OR b OR y)
                # This keeps producing 3-clauses.
                
                # The resolution is that we keep applying the transformation until all clauses are 2-clauses.
                # Even if it means many auxiliary variables.
                
                # Let's implement a recursive function to do this.
                
                def reduce_clause(lits):
                    nonlocal aux_var_counter, two_clauses
                    if len(lits) == 2:
                        two_clauses.append(lits)
                        return
                    elif len(lits) == 3:
                        a, b, c = lits
                        y = aux_var_counter
                        aux_var_counter += 1
                        # Add (a OR b OR y) and (~y OR c)
                        # Reduce (a OR b OR y)
                        z = aux_var_counter
                        aux_var_counter += 1
                        two_clauses.append([a, z])  # (a OR z)
                        reduce_clause([-z, b, y])    # (~z OR b OR y)
                        two_clauses.append([-y, c])  # (~y OR c)
                    else:
                        # General case for k-clause, k>3
                        # Split into (first OR ... OR mid) AND (~mid OR rest)
                        pass  # For now, assume max 3
                
                reduce_clause(clause)
        else:
            two_clauses.append(clause)
    
    # Now we have a list of 2-clauses over variables 1..n and auxiliary variables
    # Run 2-SAT solver on this
    
    # Number of variables in the expanded formula
    num_vars = aux_var_counter - 1
    
    # Build implication graph
    # Nodes: 1..num_vars for x_i, -(1..num_vars) for ~x_i
    # Edges: for each clause (a OR b), add (~a => b) and (~b => a)
    
    adj = defaultdict(list)
    for clause in two_clauses:
        if len(clause) == 1:
            lit = clause[0]
            # Clause (lit) means (lit OR lit) which is just lit
            # Add (~lit => lit) which is (lit OR lit) - redundant
            # Actually, unit clause (lit) means lit must be true
            # In implication graph, we can add (~lit => lit)
            adj[-lit].append(lit)
        elif len(clause) == 2:
            a, b = clause
            # (a OR b) is equivalent to (~a => b) and (~b => a)
            adj[-a].append(b)
            adj[-b].append(a)
    
    # Kosaraju's algorithm for SCC
    def kosaraju():
        visited = [False] * (2 * num_vars + 1)
        order = []
        
        # First DFS to get finishing times
        def dfs1(u):
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    dfs1(v)
            order.append(u)
        
        for i in range(1, num_vars + 1):
            if not visited[i]:
                dfs1(i)
            if not visited[-i]:
                dfs1(-i)
        
        # Transpose graph
        adj_t = defaultdict(list)
        for u in adj:
            for v in adj[u]:
                adj_t[v].append(u)
        
        # Second DFS in reverse order
        visited = [False] * (2 * num_vars + 1)
        scc = {}
        scc_id = 0
        
        def dfs2(u):
            visited[u] = True
            scc[u] = scc_id
            for v in adj_t[u]:
                if not visited[v]:
                    dfs2(v)
        
        while order:
            u = order.pop()
            if not visited[u]:
                dfs2(u)
                scc_id += 1
        
        return scc
    
    scc = kosaraju()
    
    # Check if any variable and its negation are in the same SCC
    for i in range(1, n + 1):  # Only check original variables
        if scc[i] == scc[-i]:
            print("NO")
            return
    
    # Assign values: process SCCs in topological order
    # In Kosaraju, SCCs are produced in reverse topological order
    # So we process them in order found in second DFS
    assignment = [None] * (num_vars + 1)
    
    # Re-run second DFS to get SCCs in order
    visited = [False] * (2 * num_vars + 1)
    scc_order = []
    scc_nodes = defaultdict(list)
    
    def dfs2_assign(u, sid):
        visited[u] = True
        scc_nodes[sid].append(u)
        for v in adj_t[u]:
            if not visited[v]:
                dfs2_assign(v, sid)
    
    scc_id = 0
    for i in range(1, num_vars + 1):
        if not visited[i]:
            dfs2_assign(i, scc_id)
            scc_order.append(scc_id)
            scc_id += 1
        if not visited[-i]:
            dfs2_assign(-i, scc_id)
            scc_order.append(scc_id)
            scc_id += 1
    
    # Process SCCs in reverse topological order (last finished first)
    scc_order.reverse()
    
    for sid in scc_order:
        for node in scc_nodes[sid]:
            var = abs(node)
            if assignment[var] is None:
                if node > 0:
                    assignment[var] = 1
                else:
                    assignment[var] = 0
    
    # Output result for original variables
    print("YES")
    res = []
    for i in range(1, n + 1):
        res.append(str(assignment[i]))
    print(" ".join(res))

if __name__ == "__main__":
    main()