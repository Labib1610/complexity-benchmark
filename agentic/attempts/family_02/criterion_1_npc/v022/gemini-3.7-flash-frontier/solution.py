import sys
import random

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    clauses = []
    idx = 2
    for _ in range(m):
        c = [int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])]
        idx += 3
        # Remove duplicate literals in the same clause
        c = list(set(c))
        # If clause contains both x and -x, it's always true, skip it
        has_tautology = False
        seen = set()
        for lit in c:
            if -lit in seen:
                has_tautology = True
                break
            seen.add(lit)
        if not has_tautology:
            clauses.append(c)

    # WalkSAT for quick SAT check
    def walksat(max_flips=100000, p=0.4):
        if not clauses:
            return [0] * n
        
        # Initial random assignment: 1..n -> {True, False}
        assign = {i: random.choice([True, False]) for i in range(1, n + 1)}
        
        # Precompute clause satisfaction
        sat_count = []
        var_to_clauses = {i: [] for i in range(1, n + 1)}
        for ci, cl in enumerate(clauses):
            count = 0
            for lit in cl:
                var = abs(lit)
                val = assign[var]
                if (lit > 0 and val) or (lit < 0 and not val):
                    count += 1
                var_to_clauses[var].append((ci, lit))
            sat_count.append(count)
            
        unsat_clauses = [ci for ci, cnt in enumerate(sat_count) if cnt == 0]
        unsat_pos = {ci: i for i, ci in enumerate(unsat_clauses)}
        
        def make_sat(ci):
            pass # handled by sat_count update
            
        for _ in range(max_flips):
            if not unsat_clauses:
                return [1 if assign[i] else 0 for i in range(1, n + 1)]
            
            # Pick a random unsatisfied clause
            ci = random.choice(unsat_clauses)
            cl = clauses[ci]
            
            # Find a variable to flip
            best_var = None
            min_break = float('inf')
            
            # With probability p, pick a random var from the clause
            if random.random() < p:
                best_var = abs(random.choice(cl))
            else:
                for lit in cl:
                    var = abs(lit)
                    # Count how many clauses become unsat if we flip var
                    # A clause becomes unsat if it is currently satisfied by ONLY this var
                    break_count = 0
                    for c_idx, c_lit in var_to_clauses[var]:
                        val = assign[var]
                        is_sat = (c_lit > 0 and val) or (c_lit < 0 and not val)
                        if is_sat and sat_count[c_idx] == 1:
                            break_count += 1
                    if break_count < min_break:
                        min_break = break_count
                        best_var = var
            
            # Flip best_var
            val = assign[best_var]
            assign[best_var] = not val
            for c_idx, c_lit in var_to_clauses[best_var]:
                was_sat = (c_lit > 0 and val) or (c_lit < 0 and not val)
                if was_sat:
                    sat_count[c_idx] -= 1
                    if sat_count[c_idx] == 0:
                        unsat_pos[c_idx] = len(unsat_clauses)
                        unsat_clauses.append(c_idx)
                else:
                    sat_count[c_idx] += 1
                    if sat_count[c_idx] == 1:
                        # Remove from unsat_clauses
                        pos = unsat_pos[c_idx]
                        last_c = unsat_clauses[-1]
                        unsat_clauses[pos] = last_c
                        unsat_pos[last_c] = pos
                        unsat_clauses.pop()
                        del unsat_pos[c_idx]

        return None

    # Try WalkSAT with multiple restarts
    for _ in range(10):
        res = walksat(max_flips=15000)
        if res is not None:
            print("YES")
            print(*(res))
            return

    # If WalkSAT didn't find a solution, run CDCL
    class CDCL:
        def __init__(self, n, clauses):
            self.n = n
            self.clauses = [list(c) for c in clauses]
            self.watches = {}
            for l in range(-n, n + 1):
                if l != 0:
                    self.watches[l] = []
            
            # Add initial clauses to watches
            for ci, c in enumerate(self.clauses):
                if len(c) == 0:
                    self.ok = False
                    return
                if len(c) == 1:
                    continue
                self.watches[c[0]].append(ci)
                self.watches[c[1]].append(ci)
                
            self.assignment = {}  # var -> bool
            self.decision_level = {}  # var -> int
            self.reason = {}  # var -> clause index or None
            self.trail = []
            self.trail_lim = []
            self.activity = {i: 0.0 for i in range(1, n + 1)}
            for c in self.clauses:
                for lit in c:
                    self.activity[abs(lit)] += 1.0
            self.var_inc = 1.0
            self.decay = 0.95
            self.ok = True

        def value(self, lit):
            var = abs(lit)
            if var not in self.assignment:
                return None
            val = self.assignment[var]
            return val if lit > 0 else not val

        def assign(self, lit, reason_ci):
            var = abs(lit)
            self.assignment[var] = (lit > 0)
            self.decision_level[var] = len(self.trail_lim)
            self.reason[var] = reason_ci
            self.trail.append(var)

        def propagate(self):
            q_idx = len(self.trail) - 1
            # Propagate from the first unpropagated
            if not hasattr(self, 'prop_idx'):
                self.prop_idx = 0
            
            while self.prop_idx < len(self.trail):
                var = self.trail[self.prop_idx]
                self.prop_idx += 1
                val = self.assignment[var]
                false_lit = -var if val else var
                
                # Check clauses watching false_lit
                watch_list = self.watches[false_lit]
                new_watch_list = []
                self.watches[false_lit] = new_watch_list
                
                for i, ci in enumerate(watch_list):
                    c = self.clauses[ci]
                    if c[0] == false_lit:
                        c[0], c[1] = c[1], c[0]
                    
                    # c[1] is false_lit
                    first_lit = c[0]
                    if self.value(first_lit) is True:
                        new_watch_list.append(ci)
                        continue
                    
                    # Look for replacement
                    found = False
                    for k in range(2, len(c)):
                        if self.value(c[k]) is not False:
                            c[1], c[k] = c[k], c[1]
                            self.watches[c[1]].append(ci)
                            found = True
                            break
                    if found:
                        continue
                    
                    new_watch_list.append(ci)
                    # c[0] is unit or conflict
                    if self.value(first_lit) is False:
                        # Conflict
                        # Re-add remaining watches
                        for j in range(i + 1, len(watch_list)):
                            new_watch_list.append(watch_list[j])
                        return ci
                    elif self.value(first_lit) is None:
                        self.assign(first_lit, ci)
            return None

        def analyze(self, confl):
            learnt = [0]  # will put asserting literal at learnt[0]
            seen = set()
            counter = 0
            p = None
            cur_level = len(self.trail_lim)
            
            c = self.clauses[confl]
            trail_idx = len(self.trail) - 1
            
            while True:
                for lit in (c if p is None else c[1:] if c[0] == p or c[0] == -p else [lit for lit in c if abs(lit) != abs(p)]):
                    var = abs(lit)
                    if var not in seen and self.decision_level[var] > 0:
                        seen.add(var)
                        self.activity[var] += self.var_inc
                        if self.decision_level[var] >= cur_level:
                            counter += 1
                        else:
                            learnt.append(lit)
                
                while trail_idx >= 0:
                    p_var = self.trail[trail_idx]
                    trail_idx -= 1
                    if p_var in seen:
                        break
                p = p_var if self.assignment[p_var] else -p_var
                seen.remove(p_var)
                counter -= 1
                if counter == 0:
                    learnt[0] = -p
                    break
                c = self.clauses[self.reason[p_var]]
                
            bt_level = 0
            if len(learnt) > 1:
                max_i = 1
                for i in range(2, len(learnt)):
                    if self.decision_level[abs(learnt[i])] > self.decision_level[abs(learnt[max_i])]:
                        max_i = i
                learnt[1], learnt[max_i] = learnt[max_i], learnt[1]
                bt_level = self.decision_level[abs(learnt[1])]
                
            return learnt, bt_level

        def backtrack(self, level):
            while len(self.trail_lim) > level:
                target = self.trail_lim.pop()
                while len(self.trail) > target:
                    var = self.trail.pop()
                    del self.assignment[var]
                    del self.decision_level[var]
                    del self.reason[var]
            self.prop_idx = len(self.trail)

        def pick_branch_lit(self):
            best_var = None
            best_act = -1
            for var in range(1, self.n + 1):
                if var not in self.assignment:
                    if self.activity[var] > best_act:
                        best_act = self.activity[var]
                        best_var = var
            return best_var

        def solve(self):
            if not self.ok:
                return None
            
            # Unit propagation at level 0
            for ci, c in enumerate(self.clauses):
                if len(c) == 1:
                    lit = c[0]
                    val = self.value(lit)
                    if val is False:
                        return None
                    elif val is None:
                        self.assign(lit, None)
                        
            confl = self.propagate()
            if confl is not None:
                return None

            restart_limit = 100
            restart_inc = 1.5
            confl_count = 0
            
            while True:
                confl = self.propagate()
                if confl is not None:
                    confl_count += 1
                    if len(self.trail_lim) == 0:
                        return None
                    
                    learnt, bt_level = self.analyze(confl)
                    self.backtrack(bt_level)
                    
                    ci = len(self.clauses)
                    self.clauses.append(learnt)
                    if len(learnt) > 1:
                        self.watches[learnt[0]].append(ci)
                        self.watches[learnt[1]].append(ci)
                    self.assign(learnt[0], ci)
                    
                    self.var_inc /= self.decay
                    
                    if confl_count >= restart_limit:
                        restart_limit = int(restart_limit * restart_inc)
                        confl_count = 0
                        self.backtrack(0)
                else:
                    var = self.pick_branch_lit()
                    if var is None:
                        # All assigned
                        return [1 if self.assignment.get(i, False) else 0 for i in range(1, self.n + 1)]
                    self.trail_lim.append(len(self.trail))
                    self.assign(var, None)

    solver = CDCL(n, clauses)
    res = solver.solve()
    if res is not None:
        print("YES")
        print(*(res))
    else:
        print("NO")

if __name__ == '__main__':
    solve()