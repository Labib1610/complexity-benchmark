import sys
from collections import defaultdict
import random

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Read clauses
    # 1-indexed variables: 1..n
    # Literal representation:
    # var x (1..n): positive literal is 2*x, negative literal is 2*x + 1
    # negation of lit: lit ^ 1
    # var of lit: lit >> 1
    # sign of lit: (lit & 1) == 0 -> True (positive), 1 -> False (negative)
    
    def to_lit(v):
        if v > 0:
            return 2 * v
        else:
            return 2 * (-v) + 1

    clauses = []
    idx = 2
    for _ in range(m):
        l1 = int(input_data[idx])
        l2 = int(input_data[idx+1])
        l3 = int(input_data[idx+2])
        idx += 3
        c = list(set([to_lit(l1), to_lit(l2), to_lit(l3)]))
        # If clause contains both x and not x, it's always satisfied, skip
        tautology = False
        vars_in_c = set()
        for lit in c:
            if (lit ^ 1) in c:
                tautology = True
                break
        if not tautology:
            clauses.append(c)

    # Simple CDCL SAT Solver
    class CDCL:
        def __init__(self, num_vars, clauses):
            self.n = num_vars
            self.clauses = [list(c) for c in clauses]
            self.watches = defaultdict(list)
            
            # Value of variable: -1 (unassigned), 1 (True), 0 (False)
            self.assigns = [-1] * (self.n + 1)
            self.lit_val = [-1] * (2 * self.n + 2)
            
            self.decision_level = 0
            self.trail = []
            self.trail_lim = []
            self.reason = [None] * (self.n + 1)
            self.level = [0] * (self.n + 1)
            
            # VSIDS scores
            self.activity = [0.0] * (self.n + 1)
            self.var_inc = 1.0
            self.var_decay = 0.95
            
            # Init clauses and watches
            for ci, c in enumerate(self.clauses):
                for lit in c:
                    self.activity[lit >> 1] += 1.0
                if len(c) >= 2:
                    self.watches[c[0]].append(ci)
                    self.watches[c[1]].append(ci)
                elif len(c) == 1:
                    self.watches[c[0]].append(ci)

        def lit_value(self, lit):
            return self.lit_val[lit]

        def assign_lit(self, lit, reason_clause_idx=None):
            var = lit >> 1
            val = 1 if (lit & 1) == 0 else 0
            self.assigns[var] = val
            self.lit_val[2 * var] = val
            self.lit_val[2 * var + 1] = 1 - val
            self.level[var] = self.decision_level
            self.reason[var] = reason_clause_idx
            self.trail.append(lit)

        def propagate(self):
            # Process trail from current position
            prop_head = getattr(self, 'prop_head', 0)
            while prop_head < len(self.trail):
                p = self.trail[prop_head]
                prop_head += 1
                false_lit = p ^ 1
                
                # Check watches for false_lit
                watches_list = self.watches[false_lit]
                self.watches[false_lit] = []
                
                i = 0
                while i < len(watches_list):
                    ci = watches_list[i]
                    c = self.clauses[ci]
                    
                    # Ensure false_lit is at c[1]
                    if c[0] == false_lit:
                        c[0], c[1] = c[1], c[0]
                    
                    # If 0-th watch is true, clause is satisfied
                    if self.lit_val[c[0]] == 1:
                        self.watches[false_lit].append(ci)
                        i += 1
                        continue
                    
                    # Look for new watch
                    found = False
                    for k in range(2, len(c)):
                        if self.lit_val[c[k]] != 0:
                            c[1], c[k] = c[k], c[1]
                            self.watches[c[1]].append(ci)
                            found = True
                            break
                    
                    if found:
                        i += 1
                        continue
                    
                    # No new watch found
                    self.watches[false_lit].append(ci)
                    i += 1
                    
                    # Unit propagation or conflict
                    if self.lit_val[c[0]] == 0:
                        # Conflict
                        # Re-add remaining watches
                        for j in range(i, len(watches_list)):
                            self.watches[false_lit].append(watches_list[j])
                        self.prop_head = prop_head
                        return ci
                    else:
                        # c[0] is unassigned, propagate
                        self.assign_lit(c[0], ci)
            
            self.prop_head = prop_head
            return None

        def analyze(self, conflict_ci):
            learnt = []
            seen = [False] * (self.n + 1)
            counter = 0
            p = None
            confl = self.clauses[conflict_ci]
            
            idx = len(self.trail) - 1
            while True:
                for lit in confl:
                    var = lit >> 1
                    if not seen[var] and self.level[var] > 0:
                        seen[var] = True
                        self.activity[var] += self.var_inc
                        if self.level[var] >= self.decision_level:
                            counter += 1
                        else:
                            learnt.append(lit)
                
                while True:
                    p = self.trail[idx]
                    idx -= 1
                    if seen[p >> 1]:
                        break
                
                seen[p >> 1] = False
                counter -= 1
                if counter == 0:
                    break
                confl = self.clauses[self.reason[p >> 1]]

            learnt.insert(0, p ^ 1)
            
            # Find backtrack level
            if len(learnt) <= 1:
                bt_level = 0
            else:
                max_i = 1
                for i in range(2, len(learnt)):
                    if self.level[learnt[i] >> 1] > self.level[learnt[max_i] >> 1]:
                        max_i = i
                learnt[1], learnt[max_i] = learnt[max_i], learnt[1]
                bt_level = self.level[learnt[1] >> 1]
                
            return learnt, bt_level

        def backtrack(self, to_level):
            while len(self.trail_lim) > to_level:
                lim = self.trail_lim.pop()
                while len(self.trail) > lim:
                    lit = self.trail.pop()
                    var = lit >> 1
                    self.assigns[var] = -1
                    self.lit_val[2 * var] = -1
                    self.lit_val[2 * var + 1] = -1
                    self.reason[var] = None
            self.decision_level = to_level
            self.prop_head = len(self.trail)

        def pick_branch_lit(self):
            max_act = -1
            best_var = 0
            for v in range(1, self.n + 1):
                if self.assigns[v] == -1:
                    if self.activity[v] > max_act:
                        max_act = self.activity[v]
                        best_var = v
            if best_var == 0:
                return None
            return 2 * best_var

        def solve(self):
            self.prop_head = 0
            
            # Check for initial unit clauses
            for ci, c in enumerate(self.clauses):
                if len(c) == 1:
                    if self.lit_val[c[0]] == 0:
                        return False
                    if self.lit_val[c[0]] == -1:
                        self.assign_lit(c[0], ci)
                elif len(c) == 0:
                    return False
            
            confl = self.propagate()
            if confl is not None:
                return False

            decay_counter = 0
            while True:
                decay_counter += 1
                if decay_counter % 50 == 0:
                    self.var_inc /= self.var_decay
                
                next_lit = self.pick_branch_lit()
                if next_lit is None:
                    return True # All variables assigned

                self.decision_level += 1
                self.trail_lim.append(len(self.trail))
                self.assign_lit(next_lit)

                while True:
                    confl = self.propagate()
                    if confl is not None:
                        if self.decision_level == 0:
                            return False
                        learnt, bt_level = self.analyze(confl)
                        self.backtrack(bt_level)
                        
                        ci = len(self.clauses)
                        self.clauses.append(learnt)
                        
                        if len(learnt) >= 2:
                            self.watches[learnt[0]].append(ci)
                            self.watches[learnt[1]].append(ci)
                        elif len(learnt) == 1:
                            self.watches[learnt[0]].append(ci)
                        
                        self.assign_lit(learnt[0], ci)
                    else:
                        break

    solver = CDCL(n, clauses)
    if solver.solve():
        print("YES")
        res = []
        for v in range(1, n + 1):
            val = solver.assigns[v]
            if val == -1:
                val = 0
            res.append(str(val))
        print(" ".join(res))
    else:
        print("NO")

if __name__ == '__main__':
    solve()