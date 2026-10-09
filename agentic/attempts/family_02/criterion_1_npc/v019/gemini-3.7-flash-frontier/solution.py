import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])

    clauses = []
    idx = 2
    for _ in range(m):
        c = [int(input_data[idx]), int(input_data[idx + 1]), int(input_data[idx + 2])]
        idx += 3
        c_set = set(c)
        valid = True
        for lit in c_set:
            if -lit in c_set:
                valid = False
                break
        if valid:
            clauses.append(list(c_set))

    assignment = [None] * (n + 1)

    def dpll(curr_assignment, curr_clauses):
        # Unit propagation loop
        unit_clauses = [c for c in curr_clauses if len(c) == 1]
        while unit_clauses:
            unit = unit_clauses[0]
            lit = unit[0]
            var = abs(lit)
            val = lit > 0
            if curr_assignment[var] is not None:
                if curr_assignment[var] != val:
                    return None
            else:
                curr_assignment[var] = val

            new_clauses = []
            for c in curr_clauses:
                if lit in c:
                    continue
                if -lit in c:
                    new_c = [x for x in c if x != -lit]
                    if not new_c:
                        return None
                    new_clauses.append(new_c)
                else:
                    new_clauses.append(c)
            curr_clauses = new_clauses
            unit_clauses = [c for c in curr_clauses if len(c) == 1]

        if not curr_clauses:
            for i in range(1, n + 1):
                if curr_assignment[i] is None:
                    curr_assignment[i] = True
            return curr_assignment

        # Choose a literal with highest frequency in shortest clauses
        min_len = min(len(c) for c in curr_clauses)
        counts = {}
        for c in curr_clauses:
            if len(c) == min_len:
                for lit in c:
                    counts[lit] = counts.get(lit, 0) + 1

        best_lit = max(counts.keys(), key=lambda l: counts[l])

        for branch_lit in [best_lit, -best_lit]:
            ass_copy = list(curr_assignment)
            res = dpll(ass_copy, curr_clauses + [[branch_lit]])
            if res is not None:
                return res

        return None

    res = dpll(assignment, clauses)
    if res is None:
        print("NO")
    else:
        print("YES")
        out = [1 if res[i] else 0 for i in range(1, n + 1)]
        print(*(out))


if __name__ == "__main__":
    solve()