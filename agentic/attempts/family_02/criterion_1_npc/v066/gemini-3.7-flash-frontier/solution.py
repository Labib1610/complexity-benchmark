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
        # Simplify clause: remove duplicate literals
        c = list(set(c))
        # If clause contains both x and -x, it's always true, can ignore
        has_tautology = False
        for lit in c:
            if -lit in c:
                has_tautology = True
                break
        if not has_tautology:
            clauses.append(c)

    # Simple DPLL / CDCL solver
    # State:
    # assignments: lit -> True (if assigned)
    # var_val: var (1..n) -> 1, 0, or -1 (unassigned)
    
    # Let's implement CDCL
    # Variables: 1 to n
    # Literals: positive 1..n, negative -1..-n
    
    # Pre-check for empty clause
    for c in clauses:
        if len(c) == 0:
            print("NO")
            return

    # CDCL Solver Implementation
    class CDCL:
        def __init__(self, n, clauses):
            self.n = n
            self.clauses = [list(c) for c in clauses]
            self.assignment = {} # var -> bool
            self.decision_level = {} # var -> int
            self.reason = {} # var -> clause_idx
            self.trail = []
            self.trail_lim = [] # decision level starts
            self.vsids = {i: 0.0 for i in range(1, n + 1)}
            for c in self.clauses:
                for lit in c:
                    self.vsids[abs(lit)] += 1.0
            self.decay = 0.95
            self.inc = 1.0

            # Watched literals: lit -> list of clause indices
            # Clause is watched by clause[0] and clause[1] (if len >= 2)
            self.watches = {i: [] for i in range(-n, n + 1) if i != 0}
            for ci, c in enumerate(self.clauses):
                if len(c) >= 2:
                    self.watches[c[0]].append(ci)
                    self.watches[c[1]].append(ci)

        def value(self, lit):
            var = abs(lit)
            if var not in self.assignment:
                return None
            val = self.assignment[var]
            return val if lit > 0 else (not val)

        def assign(self, lit, reason_idx):
            var = abs(lit)
            val = (lit > 0)
            self.assignment[var] = val
            self.decision_level[var] = len(self.trail_lim)
            self.reason[var] = reason_idx
            self.trail.append(var)

        def propagate(self):
            # Unit propagation using 2-watched literals
            # Also handle unit clauses at start
            q_idx = 0
            while q_idx < len(self.trail):
                v = self.trail[q_idx]
                q_idx += 1
                val = self.assignment[v]
                false_lit = -v if val else v

                i = 0
                watch_list = self.watches[false_lit]
                while i < len(watch_list):
                    ci = watch_list[i]
                    c = self.clauses[ci]

                    # Ensure false_lit is at c[1]
                    if c[0] == false_lit:
                        c[0], c[1] = c[1], c[0]

                    # If c[0] is already True, clause is satisfied
                    if self.value(c[0]) is True:
                        i += 1
                        continue

                    # Look for a new watched literal
                    found = False
                    for k in range(2, len(c)):
                        if self.value(c[k]) is not False:
                            c[1], c[k] = c[k], c[1]
                            self.watches[c[1]].append(ci)
                            watch_list[i] = watch_list[-1]
                            watch_list.pop()
                            found = True
                            break

                    if found:
                        continue

                    # No new literal to watch: c[0] is unit or conflict
                    if self.value(c[0]) is False:
                        # Conflict!
                        return ci
                    else:
                        # Unit propagate c[0]
                        if self.value(c[0]) is None:
                            self.assign(c[0], ci)
                    i += 1
            return None

        def analyze(self, conflict_ci):
            # 1-UIP conflict analysis
            curr_level = len(self.trail_lim)
            if curr_level == 0:
                return None, 0

            learned = []
            seen = set()
            counter = 0
            confl = self.clauses[conflict_ci]
            p = None
            trail_idx = len(self.trail) - 1

            while True:
                for lit in confl:
                    var = abs(lit)
                    if var != p and var not in seen:
                        seen.add(var)
                        if self.decision_level[var] == curr_level:
                            counter += 1
                        else:
                            learned.append(lit)
                
                # Find the next variable from trail that is in seen
                while trail_idx >= 0:
                    v = self.trail[trail_idx]
                    trail_idx -= 1
                    if v in seen:
                        p = v
                        break
                
                counter -= 1
                if counter == 0:
                    # 1-UIP reached
                    p_val = self.assignment[p]
                    learned_lit = -p if p_val else p
                    learned.append(learned_lit)
                    break
                
                confl = self.clauses[self.reason[p]]

            # Learned clause is constructed. Put 1-UIP at index 0.
            # Put literal with highest decision level < curr_level at index 1.
            # Find backtrack level
            learned[0], learned[-1] = learned[-1], learned[0]
            bt_level = 0
            if len(learned) > 1:
                max_i = 1
                max_lvl = self.decision_level[abs(learned[1])]
                for k in range(2, len(learned)):
                    lvl = self.decision_level[abs(learned[k])]
                    if lvl > max_lvl:
                        max_lvl = lvl
                        max_i = k
                learned[1], learned[max_i] = learned[max_i], learned[1]
                bt_level = max_lvl

            return learned, bt_level

        def backtrack(self, level):
            while len(self.trail_lim) > level:
                start_idx = self.trail_lim.pop()
                while len(self.trail) > start_idx:
                    v = self.trail.pop()
                    del self.assignment[v]
                    del self.decision_level[v]
                    del self.reason[v]

        def pick_var(self):
            best_var = None
            best_score = -1.0
            for v in range(1, self.n + 1):
                if v not in self.assignment:
                    if self.vsids[v] > best_score:
                        best_score = self.vsids[v]
                        best_var = v
            return best_var

        def solve(self):
            # Initial propagation for 1-literal clauses
            for ci, c in enumerate(self.clauses):
                if len(c) == 1:
                    lit = c[0]
                    if self.value(lit) is False:
                        return False
                    if self.value(lit) is None:
                        self.assign(lit, ci)

            conflict = self.propagate()
            if conflict is not None:
                return False

            while True:
                var = self.pick_var()
                if var is None:
                    return True # All variables assigned

                # Make decision
                self.trail_lim.append(len(self.trail))
                # Heuristic: try True first (or based on occurrences)
                self.assign(var, None)

                while True:
                    conflict = self.propagate()
                    if conflict is None:
                        break

                    learned, bt_level = self.analyze(conflict)
                    if learned is None:
                        return False

                    self.backtrack(bt_level)

                    ci = len(self.clauses)
                    self.clauses.append(learned)
                    for lit in learned:
                        self.vsids[abs(lit)] += self.inc
                    self.inc /= self.decay

                    if len(learned) >= 2:
                        self.watches[learned[0]].append(ci)
                        self.watches[learned[1]].append(ci)
                    elif len(learned) == 1:
                        self.watches[learned[0]].append(ci)

                    # Propagate the 1-UIP literal
                    self.assign(learned[0], ci)

    solver = CDCL(n, clauses)
    if solver.solve():
        print("YES")
        ans = []
        for i in range(1, n + 1):
            val = solver.assignment.get(i, True) # if unassigned, default True
            ans.append(1 if val else 0)
        print(*(ans))
    else:
        print("NO")

if __name__ == '__main__':
    solve()