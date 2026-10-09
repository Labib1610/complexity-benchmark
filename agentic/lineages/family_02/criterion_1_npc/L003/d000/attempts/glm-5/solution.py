def search(lo, hi, sat, assigned, val):
    # propagate units; returns status and updated state
    while True:
        unsat = ~sat & clause_full_mask  # need to mask to m bits: use SAT_ALL trick
        ...