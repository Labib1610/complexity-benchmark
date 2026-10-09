import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    clauses = []
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        l3 = int(next(it))
        clauses.append((l1, l2, l3))
    
    # 2-SAT formulation
    # Variable i: valve i is 1 (True) or 0 (False)
    # For each check (l1, l2, l3), at least one must match
    # This is a clause: (match1 OR match2 OR match3)
    # Convert to 2-SAT by introducing auxiliary variable for each check
    
    # match_i is True if valve |li| has state (li > 0 ? 1 : 0)
    # match_i = (li > 0) == valve[|li|]
    
    # We need: match1 OR match2 OR match3
    # Using Tseitin transformation:
    # a = match1, b = match2, c = match3
    # Introduce auxiliary variable d (d = a OR b OR c)
    # d -> (a OR b OR c)
    # (a OR b OR c) -> d
    # 
    # For d -> (a OR b OR c): equivalent to (!d OR a OR b OR c)
    # Split into: (!d OR a OR x), (!x OR b OR c)
    # Further split: (!d OR a OR x), (!x OR b OR y), (!y OR c)
    # 
    # For (a OR b OR c) -> d: equivalent to (!a -> d), (!b -> d), (!c -> d)
    # i.e., (a OR d), (b OR d), (c OR d)
    
    # Total variables: n valves + m auxiliary (one per check)
    # Variable indexing: 1..n for valves, n+1..n+m for auxiliary
    
    # Implication graph: 2*(n+m) nodes (each var has True and False)
    # Node indices: 2*(var-1) for False, 2*(var-1)+1 for True
    
    N = n + m
    graph = [[] for _ in range(2 * N)]
    
    def get_node(var, val):
        # var is 1-indexed, val is 0 or 1
        return 2 * (var - 1) + val
    
    def add_implication(var1, val1, var2, val2):
        # Add edge: (var1=val1) -> (var2=val2)
        u = get_node(var1, val1)
        v = get_node(var2, val2)
        graph[u].append(v)
    
    for check_idx, (l1, l2, l3) in enumerate(clauses):
        d = n + 1 + check_idx  # auxiliary variable for this check
        
        # Process each literal
        specs = []
        for li in (l1, l2, l3):
            valve = abs(li)
            target = 1 if li > 0 else 0
            specs.append((valve, target))
        
        # d -> (a OR b OR c) via intermediate variables
        # (!d OR a OR x), (!x OR b OR y), (!y OR c)
        # Also need: x -> (b OR c), y -> c
        
        if m == 0:
            continue
            
        # For 3 literals, we need 2 intermediate variables (x, y)
        # Let's use: x = n + m + 1 + 2*check_idx, y = x + 1
        # But we only have n+m variables. Let's reconsider.
        
        # Actually, let's use a different approach:
        # For clause (a OR b OR c), we can use:
        # (!a -> b OR c) which is (!a -> x), (x -> b OR c)
        # where x is auxiliary
        
        # Simpler: use the standard 3-SAT to 2-SAT reduction
        # For each clause (l1 OR l2 OR l3):
        # Introduce new variable x
        # Add: (!l1 -> x), (x -> l2 OR l3)
        # The second part needs another variable y:
        # (x -> y), (y -> l2), (!l2 -> !y), (y -> l3 OR ...)
        # This gets complicated.
        
        # Let me use a cleaner approach:
        # For clause (a OR b OR c):
        # Add: (!a -> b), (!a -> c), (!b -> a), (!b -> c), (!c -> a), (!c -> b)
        # Wait, this is wrong because it forces multiple literals to be true.
        
        # Correct approach: Tseitin transformation
        # For clause (a OR b OR c), introduce auxiliary d
        # d <-> (a OR b OR c)
        # 
        # d -> (a OR b OR c): (!d OR a OR b OR c)
        #   = (!d OR a OR x) AND (!x OR b OR c)
        #   = (!d OR a OR x) AND (!x OR b OR y) AND (!y OR c)
        # 
        # (a OR b OR c) -> d: (!a -> d) AND (!b -> d) AND (!c -> d)
        #   = (a OR d) AND (b OR d) AND (c OR d)
        
        # We need 2 auxiliary variables per clause for the intermediate x, y
        # But we only allocated 1 auxiliary per clause.
        
        # Let's re-allocate: n valves + 2*m auxiliary (2 per clause)
        pass
    
    # Rebuild with correct number of variables
    N = n + 2 * m
    graph = [[] for _ in range(2 * N)]
    
    def get_node(var, val):
        return 2 * (var - 1) + val
    
    def add_implication(var1, val1, var2, val2):
        u = get_node(var1, val1)
        v = get_node(var2, val2)
        graph[u].append(v)
    
    for check_idx, (l1, l2, l3) in enumerate(clauses):
        # Auxiliary variables for this clause
        x = n + 1 + 2 * check_idx      # first intermediate
        y = x + 1                       # second intermediate
        
        # Literal specifications
        specs = []
        for li in (l1, l2, l3):
            valve = abs(li)
            target = 1 if li > 0 else 0
            specs.append((valve, target))
        
        a_valve, a_target = specs[0]
        b_valve, b_target = specs[1]
        c_valve, c_target = specs[2]
        
        # (!d OR a OR x) becomes: d -> (a OR x), which is (!d -> a) and (!d -> x)
        # No wait, (!d OR a OR x) = !d -> (a OR x) is not directly a 2-CNF
        # 
        # Let's think again. (!d OR a OR x) is a 3-CNF clause.
        # To convert to 2-CNF implications:
        # (d AND !a) -> x, i.e., add edge (d, !a) -> x
        # But we can't have edges from conjunction of two literals.
        # 
        # The correct 2-CNF for (!d OR a OR x):
        # (d -> a) OR x, which is (!d -> a) OR x
        # Hmm, this is still not 2-CNF.
        # 
        # Actually, (!d OR a OR x) = (d -> (a OR x))
        # In 2-SAT, we can express this as:
        # (d AND !a) -> x, which needs auxiliary
        # 
        # Let me use a different formulation.
        # For clause (a OR b OR c):
        # We want at least one of a, b, c to be true.
        # 
        # Using resolution: introduce x, y such that
        # x = b OR c
        # Then clause becomes (a OR x)
        # And we need x <-> (b OR c)
        # 
        # x <-> (b OR c):
        # x -> (b OR c): (!x OR b OR c) = (x -> b) OR (x -> c)? No.
        #   (!x OR b OR c) = (x AND !b) -> c, (x AND !c) -> b
        #   Still not 2-CNF.
        # 
        # Actually, the standard way:
        # (!x OR b OR c) can be written as:
        # (!x OR b OR y) AND (!y OR c) where y is another auxiliary
        # 
        # So for (a OR b OR c):
        # Introduce x, y
        # (a OR x), (!x OR b OR y), (!y OR c)
        # 
        # (a OR x): (!a -> x), i.e., add edge (!a) -> x
        # (!x OR b OR y): (x -> b) OR y, which is (x AND !b) -> y
        #   Not directly 2-CNF. Need to split differently.
        # 
        # Let me try: (!x OR b OR y) = (x -> (b OR y))
        # = (x AND !b) -> y
        # = (x AND !y) -> b
        # Neither is 2-CNF.
        # 
        # OK, the correct Tseitin transformation for OR:
        # For x = a OR b:
        # Clauses: (!a -> x), (!b -> x), (x -> a OR b)
        # (!a -> x) = (a OR x): 2-CNF
        # (!b -> x) = (b OR x): 2-CNF
        # (x -> a OR b) = (!x OR a OR b): not 2-CNF directly
        #   But we can rewrite as: (x -> a) OR (x -> b)? No, that's wrong.
        #   Actually (!x OR a OR b) = (x AND !a) -> b = (x AND !b) -> a
        #   Still not 2-CNF.
        # 
        # The trick: (!x OR a OR b) can be handled by introducing another variable.
        # But for 3-SAT to 2-SAT, we use:
        # For clause (a OR b OR c), introduce x:
        # (a OR b OR !x) AND (x OR c)
        # Check: if a, b, c all false, then first clause needs !x true, so x false.
        #        Then second clause needs (false OR false) which is false. Contradiction.
        # If at least one of a, b, c true:
        #   - If a or b true, first clause satisfied, x can be anything.
        #   - If c true, second clause satisfied, x can be anything.
        # So this encoding is correct!
        # 
        # (a OR b OR !x): (!a AND !b) -> !x, i.e., add edges (!a -> !x), (!b -> !x)? No.
        #   (a OR b OR !x) = (!a -> b OR !x) = (!a AND !b) -> !x
        #   Not 2-CNF directly.
        # 
        # Hmm, let me think again.
        # (a OR b OR !x) is a 3-CNF clause. To convert to 2-CNF:
        # Introduce y:
        # (a OR b OR !x) = (a OR y) AND (!y OR b OR !x)? No.
        # 
        # Actually, the standard reduction from 3-SAT to 2-SAT doesn't preserve equivalence,
        # it preserves satisfiability. But for our case, we need to find a satisfying assignment.
        # 
        # Let me use a different approach: for each clause (a OR b OR c),
        # we can enumerate which literal is true (3 choices) and add implications.
        # 
        # If a is false, then (b OR c) must be true.
        # If b is false, then (a OR c) must be true.
        # If c is false, then (a OR b) must be true.
        # 
        # For (!a -> (b OR c)):
        # Introduce x = (b OR c)
        # Then (!a -> x), and x <-> (b OR c)
        # 
        # x <-> (b OR c):
        # (b OR c) -> x: (!b -> x), (!c -> x)
        # x -> (b OR c): (!x -> b OR c) = (!x AND !b) -> c = (!x AND !c) -> b
        #   Not 2-CNF.
        # 
        # Alternative: x = b OR c is equivalent to:
        # x = !(!b AND !c)
        # So !x = !b AND !c
        # x <-> !(b AND c)? No, that's wrong.
        # 
        # Let me just use the fact that for 3-SAT clause (a OR b OR c),
        # we can introduce auxiliary variables and convert to 2-SAT.
        # 
        # The standard conversion:
        # For clause (a OR b OR c), introduce x:
        # (a OR x), (b OR !x), (c OR !x)
        # Check: if a, b, c all false, then first clause needs x true,
        #        second clause needs !x true (since b false), contradiction.
        # If a true: first clause satisfied, x can be anything.
        # If b true: second clause satisfied, x can be anything.
        # If c true: third clause satisfied, x can be anything.
        # So this encoding is correct!
        # 
        # (a OR x): (!a -> x)
        # (b OR !x): (!b -> !x), equivalently (x -> b)
        # (c OR !x): (!c -> !x), equivalently (x -> c)
        # 
        # So for clause (a OR b OR c):
        # Introduce x
        # Add: (!a -> x), (x -> b), (x -> c)
        # 
        # Wait, let me verify:
        # If a, b, c all false:
        #   (!a -> x) means (true -> x), so x must be true.
        #   (x -> b) means (true -> false), contradiction.
        # If a true:
        #   (!a -> x) means (false -> x), no constraint on x.
        #   Other clauses don't constrain anything since a is true.
        # If b true:
        #   (!a -> x) means (false -> x) if a false, so x can be anything.
        #   (x -> b) means (x -> true), always satisfied.
        #   (x -> c) means (x -> false) if c false, so x must be false.
        #   But wait, if b is true and c is false, x must be false.
        #   Then (!a -> x) means (true -> false) if a false, contradiction.
        #   So if a false, b true, c false, we get contradiction.
        #   But the clause (a OR b OR c) is satisfied since b is true!
        # 
        # Hmm, there's an issue. Let me reconsider.
        # 
        # Actually, the encoding (a OR x), (b OR !x), (c OR !x) is:
        # - If a false, x must be true (from first clause).
        # - If x true, b must be true OR c must be true (from second and third).
        #   Wait, (b OR !x) means if b false then !x true, i.e., x false.
        #   (c OR !x) means if c false then !x true, i.e., x false.
        #   So if x true, then b must be true (from second clause) AND c must be true (from third clause).
        # 
        # This is wrong! The encoding forces b AND c to be true if x is true.
        # 
        # Let me try another encoding.
        # For clause (a OR b OR c), introduce x:
        # (a OR b OR !x) AND (x OR c)
        # 
        # (a OR b OR !x): if a and b both false, then !x must be true, so x false.
        # (x OR c): if x false, then c must be true.
        # 
        # So if a, b, c all false:
        #   From first clause: x must be false.
        #   From second clause: c must be true. Contradiction.
        # 
        # If a true: first clause satisfied, x can be anything, second clause: x OR c.
        # If b true: same as above.
        # If c true: second clause satisfied, first clause: a OR b OR !x.
        # 
        # Now, (a OR b OR !x) is still a 3-CNF clause. We need to convert it.
        # Introduce y:
        # (a OR b OR !x) = (a OR y) AND (!y OR b OR !x)
        # Hmm, (!y OR b OR !x) is still 3-CNF.
        # 
        # Let me try: (a OR b OR !x) = (a OR y) AND (!y OR b) AND (!y OR !x)? No, that's wrong.
        # 
        # Actually, (a OR b OR !x) can be converted as follows:
        # Introduce y:
        # (a OR y), (!y OR b OR !x)
        # 
        # (!y OR b OR !x) = (y -> b OR !x) = (y AND !b) -> !x
        # Still not 2-CNF.
        # 
        # Let me try yet another approach.
        # (a OR b OR !x) = (a OR b) OR !x
        # Introduce y = (a OR b):
        # (y OR !x), and y <-> (a OR b)
        # 
        # y <-> (a OR b):
        # (a OR b) -> y: (!a -> y), (!b -> y)
        # y -> (a OR b): (!y -> a OR b) = (!y AND !a) -> b = (!y AND !b) -> a
        #   Not 2-CNF.
        # 
        # OK here's the key insight: we don't need y <-> (a OR b), we just need
        # the whole formula to be satisfiable iff the original is.
        # 
        # For (a OR b OR !x) AND (x OR c):
        # We can use:
        # (a OR y), (b OR !y), (!x OR y), (x OR c)
        # where y is auxiliary.
        # 
        # Let's verify:
        # - If a, b, c all false:
        #   (a OR y) means y must be true.
        #   (b OR !y) means !y must be true (since b false), so y false. Contradiction.
        # - If a true:
        #   (a OR y) satisfied, y can be anything.
        #   (b OR !y): if b false, !y must be true, so y false.
        #   (!x OR y): if y false, !x must be true, so x false.
        #   (x OR c): if x false, c must be true. But c is false. Contradiction?
        #   Wait, if a is true, the original clause is satisfied. Why is there a contradiction?
        # 
        # The issue is that the auxiliary variables introduce additional constraints.
        # 
        # Let me think differently. For the clause (a OR b OR c), we want:
        # At least one of a, b, c is true.
        # 
        # We can model this as:
        # (!a -> b OR c)
        # (!b -> a OR c)
        # (!c -> a OR b)
        # 
        # For (!a -> b OR c):
        # This is equivalent to (a OR b OR c), which is our original clause.
        # 
        # To convert (!a -> b OR c) to 2-CNF:
        # Introduce x such that x <-> (b OR c).
        # Then (!a -> x) and x <-> (b OR c).
        # 
        # (!a -> x) = (a OR x): 2-CNF
        # 
        # x <-> (b OR c):
        # x -> (b OR c): (!x OR b OR c), not 2-CNF
        # (b OR c) -> x: (!b -> x), (!c -> x), both 2-CNF
        # 
        # For (!x OR b OR c), we can introduce y:
        # (!x OR b OR y) AND (!y OR c)
        # 
        # (!x OR b OR y): (x AND !b) -> y, not 2-CNF
        # 
        # Hmm, this is getting complicated. Let me just use a known reduction.
        # 
        # Actually, for 3-SAT, there's a standard reduction to 2-SAT that introduces
        # O(n) auxiliary variables per clause. But that's overkill.
        # 
        # Let me use a simpler approach: since n <= 90, we can use backtracking with pruning.
        # But m can be up to 400, which might be too slow.
        # 
        # Actually, let's think about the structure of the problem.
        # Each clause has 3 literals. We need at least one literal to be true.
        # 
        # For small n (<= 90), we can use a SAT solver or backtracking.
        # But let's try the 2-SAT approach more carefully.
        # 
        # Here's a correct reduction:
        # For clause (a OR b OR c), introduce auxiliary variables x and y.
        # 
        # The clause is equivalent to:
        # (a OR x) AND (b OR !x OR y) AND (c OR !y)
        # 
        # Let's verify:
        # - If a true: (a OR x) satisfied, x can be anything.
        #   (b OR !x OR y): if b false and !x false (i.e., x true), then y must be true.
        #   (c OR !y): if y true, !y false, so c must be true. But c might be false!
        #   Wait, this seems wrong.
        # 
        # Let me re-examine. The encoding should be:
        # (a OR x) AND (!x OR b OR y) AND (!y OR c)
        # 
        # - If a, b, c all false:
        #   (a OR x): x must be true.
        #   (!x OR b OR y): since x true, !x false. b false. So y must be true.
        #   (!y OR c): since y true, !y false. c false. Contradiction.
        # - If a true:
        #   (a OR x) satisfied, x can be anything.
        #   Other clauses don't force anything specific.
        # - If b true:
        #   (a OR x): if a false, x must be true.
        #   (!x OR b OR y): satisfied since b true.
        #   (!y OR c): if c false, !y must be true, so y false.
        #   So x true, y false. Consistent.
        # - If c true:
        #   (a OR x): if a false, x must be true.
        #   (!x OR b OR y): since x true, !x false. If b false, y must be true.
        #   (!y OR c): satisfied since c true.
        #   So x true, y true. Consistent.
        # 
        # Great, this encoding works!
        # 
        # So for clause (a OR b OR c):
        # Introduce x, y
        # Add: (a OR x), (!x OR b OR y), (!y OR c)
        # 
        # Converting to implications:
        # (a OR x): (!a -> x)
        # (!x OR b OR y): (x AND !b) -> y, which is not 2-CNF.
        # 
        # Hmm, still the same issue.
        # 
        # Let me try: (!x OR b OR y) = (x -> b OR y) = (x AND !b) -> y
        # We can't express this directly in 2-CNF.
        # 
        # Alternative: (!x OR b OR y) = (!x OR b) OR y = (x -> b) OR y
        # This is (x -> b) OR y = (!x OR b) OR y = (!x OR b OR y), same thing.
        # 
        # Let me try a different split:
        # (!x OR b OR y) = (!x OR z) AND (!z OR b OR y) where z is another auxiliary? No, that makes it worse.
        # 
        # Actually, (!x OR b OR y) can be written as:
        # (!x OR b OR y) = (!x OR y OR b)
        # Introduce z:
        # (!x OR y OR z) AND (!z OR b)
        # 
        # (!x OR y OR z): still 3-CNF
        # 
        # OK let me try yet another approach. The standard way to convert 3-SAT to 2-SAT:
        # 
        # For clause (l1 OR l2 OR l3), introduce new variable x.
        # Replace with: (l1 OR l2 OR x) AND (!x OR l3)
        # 
        # (l1 OR l2 OR x) is still 3-CNF. Repeat:
        # (l1 OR l2 OR x) = (l1 OR y) AND (!y OR l2 OR x)
        # 
        # (!y OR l2 OR x) is still 3-CNF. Repeat:
        # (!y OR l2 OR x) = (!y OR z) AND (!z OR l2 OR x)
        # 
        # This doesn't terminate!
        # 
        # The issue is that OR of 3 literals can't be directly converted to 2-CNF.
        # We need a different approach.
        # 
        # Actually, the key insight is that we're not trying to convert a single clause,
        # but the entire formula. The Tseitin transformation introduces auxiliary variables
        # and converts the entire formula to CNF with each clause having at most 3 literals.
        # But we need 2-CNF.
        # 
        # For 2-SAT, we can only handle clauses with at most 2 literals.
        # A clause with 3 literals like (a OR b OR c) cannot be directly converted to 2-CNF
        # without changing the semantics.
        # 
        # However, we can use the following trick:
        # For clause (a OR b OR c), we introduce an auxiliary variable d and add:
        # (a OR d), (b OR d), (c OR d), (!d OR a OR b OR c)
        # 
        # The first three are 2-CNF. The last one is 4-CNF, which is worse.
        # 
        # Let me think about this differently. The problem is 3-SAT, which is NP-complete.
        # We can't solve it in polynomial time (unless P=NP).
        # 
        # But wait, the constraints are small: n <= 90, m <= 400.
        # We can use a SAT solver or backtracking.
        # 
        # Let me implement a simple backtracking algorithm with unit propagation.
        # 
        # Actually, let me reconsider the 2-SAT approach.
        # 
        # For each clause (l1 OR l2 OR l3), we need at least one literal to be true.
        # This is equivalent to: NOT (all three literals are false).
        # 
        # If we think of it as: NOT (!l1 AND !l2 AND !l3), this is a NAND of 3 literals.
        # 
        # In 2-SAT, we can express binary NAND: NOT (a AND b) = (!a OR !b).
        # But for ternary NAND, we need: NOT (a AND b AND c) = (!a OR !b OR !c).
        # This is still a 3-CNF clause.
        # 
        # So the problem is inherently 3-SAT, and we can't reduce it to 2-SAT in polynomial time.
        # 
        # Let me implement a backtracking solver.
        
        # Backtracking with unit propagation and pure literal elimination
        pass
    
    # Since the problem is 3-SAT, let's use a proper SAT solver approach.
    # We'll use the DPLL algorithm with unit propagation.
    
    # First, let's parse the clauses properly.
    parsed_clauses = []
    for l1, l2, l3 in clauses:
        clause = []
        for li in (l1, l2, l3):
            valve = abs(li)
            target = 1 if li > 0 else 0
            # Literal: (valve, target) means valve should be target
            # If target is 1, the literal is satisfied when valve is 1.
            # If target is 0, the literal is satisfied when valve is 0.
            clause.append((valve, target))
        parsed_clauses.append(clause)
    
    # DPLL algorithm
    assignment = [None] * (n + 1)  # 1-indexed, None means unassigned
    
    def evaluate_clause(clause, assignment):
        """Returns True if clause is satisfied, False if unsatisfied, None if undetermined."""
        has_unassigned = False
        for valve, target in clause:
            if assignment[valve] is None:
                has_unassigned = True
            elif assignment[valve] == target:
                return True
        return None if has_unassigned else False
    
    def unit_propagate(clauses, assignment):
        """Performs unit propagation. Returns False if conflict detected."""
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                result = evaluate_clause(clause, assignment)
                if result is False:
                    return False  # Conflict
                if result is None:
                    # Check if this is a unit clause
                    unassigned = [(v, t) for v, t in clause if assignment[v] is None]
                    if len(unassigned) == 1:
                        valve, target = unassigned[0]
                        assignment[valve] = target
                        changed = True
        return True
    
    def dpll(clauses, assignment, n):
        """DPLL algorithm. Returns True if satisfiable, False otherwise."""
        # Make a copy of assignment
        assignment = assignment[:]
        
        # Unit propagation
        if not unit_propagate(clauses, assignment):
            return False
        
        # Check if all clauses are satisfied
        all_satisfied = True
        for clause in clauses:
            result = evaluate_clause(clause, assignment)
            if result is False:
                return False
            if result is None:
                all_satisfied = False
        
        if all_satisfied:
            return True
        
        # Find an unassigned variable
        for valve in range(1, n + 1):
            if assignment[valve] is None:
                # Try both values
                for target in [0, 1]:
                    new_assignment = assignment[:]
                    new_assignment[valve] = target
                    if dpll(clauses, new_assignment, n):
                        # Copy the satisfying assignment back
                        for i in range(1, n + 1):
                            if new_assignment[i] is not None:
                                assignment[i] = new_assignment[i]
                        return True
                return False
        
        return True
    
    # Actually, let's use a more efficient approach.
    # Since n <= 90, we can use a randomized algorithm like WalkSAT or a proper SAT solver.
    # But for simplicity, let's use a backtracking approach with better heuristics.
    
    # Let's implement a simple recursive backtracking with unit propagation.
    
    def solve_sat(clauses, assignment, n):
        """Solves the SAT problem. Returns the satisfying assignment or None."""
        assignment = assignment[:]
        
        # Unit propagation
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                # Count satisfied, unsatisfied, and unassigned literals
                satisfied = False
                unassigned = []
                for valve, target in clause:
                    if assignment[valve] is not None:
                        if assignment[valve] == target:
                            satisfied = True
                            break
                    else:
                        unassigned.append((valve, target))
                
                if satisfied:
                    continue
                
                if len(unassigned) == 0:
                    return None  # Conflict: all literals are false
                
                if len(unassigned) == 1:
                    # Unit clause: must assign this literal
                    valve, target = unassigned[0]
                    assignment[valve] = target
                    changed = True
        
        # Check if all clauses are satisfied
        all_satisfied = True
        for clause in clauses:
            satisfied = False
            for valve, target in clause:
                if assignment[valve] is not None and assignment[valve] == target:
                    satisfied = True
                    break
            if not satisfied:
                all_satisfied = False
                break
        
        if all_satisfied:
            # Fill in remaining variables with arbitrary values
            for i in range(1, n + 1):
                if assignment[i] is None:
                    assignment[i] = 0
            return assignment
        
        # Find an unassigned variable (use a heuristic: most constrained variable)
        best_valve = None
        best_count = -1
        for valve in range(1, n + 1):
            if assignment[valve] is None:
                # Count how many clauses this variable appears in
                count = sum(1 for clause in clauses if any(v == valve for v, _ in clause))
                if count > best_count:
                    best_count = count
                    best_valve = valve
        
        if best_valve is None:
            # All variables assigned, but not all clauses satisfied
            return None
        
        # Try both values for the best valve
        for target in [0, 1]:
            new_assignment = assignment[:]
            new_assignment[best_valve] = target
            result = solve_sat(clauses, new_assignment, n)
            if result is not None:
                return result
        
        return None
    
    # Handle edge case: no clauses
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    result = solve_sat(parsed_clauses, [None] * (n + 1), n)
    
    if result is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(str(result[i]) for i in range(1, n + 1)))

solve()