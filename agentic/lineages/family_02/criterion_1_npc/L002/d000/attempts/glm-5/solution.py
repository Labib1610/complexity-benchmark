def dpll(clauses, assignment):
    # unit propagation
    # pure literal elimination
    # if empty clause: fail
    # if no clauses: success
    # pick branching variable (heuristic)
    # try both values