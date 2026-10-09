def solve():
    import sys
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    constraints = []
    for _ in range(m):
        l1 = int(input_data[idx]); idx += 1
        l2 = int(input_data[idx]); idx += 1
        l3 = int(input_data[idx]); idx += 1
        # For each criterion, the "bad" position is:
        # +k means requires 1, fails when toggle=0, so bad position is 0
        # -k means requires 0, fails when toggle=1, so bad position is 1
        crits = []
        for l in [l1, l2, l3]:
            toggle = abs(l)
            bad_pos = 0 if l > 0 else 1  # position that makes this criterion fail
            crits.append((toggle, bad_pos))
        constraints.append(crits)
    
    # assignment[i] = -1 (unassigned), 0, or 1
    assignment = [-1] * (n + 1)
    
    # For each constraint, count how many criteria are already satisfied (i.e., toggle is at non-bad position)
    # A constraint is violated when all criteria have toggle at bad position
    # A constraint is "satisfied" (safe) when at least one criterion has toggle at non-bad position
    
    # For each constraint, track: number of criteria that could still all be bad
    # If any criterion is already non-bad (toggle assigned to non-bad position), constraint is safe
    # If all criteria are assigned to bad positions, constraint is violated
    # If some are bad and rest unassigned, still potentially dangerous
    
    constraint_safe = [False] * m  # True if at least one criterion is definitely non-bad
    constraint_violated = [False] * m  # True if all criteria are bad
    
    # For each constraint, count assigned-bad and assigned-nonbad
    bad_count = [0] * m  # criteria assigned to bad position
    nonbad_count = [0] * m  # criteria assigned to non-bad position
    unassigned_count = [3] * m  # criteria not yet assigned
    
    # For each toggle, which constraints involve it
    toggle_constraints = [[] for _ in range(n + 1)]
    for ci, crits in enumerate(constraints):
        for toggle, _ in crits:
            toggle_constraints[toggle].append(ci)
    
    def assign(toggle, pos):
        """Assign toggle to pos. Returns list of (constraint_index, change) for undo."""
        changes = []
        assignment[toggle] = pos
        for ci in toggle_constraints[toggle]:
            # Find criteria in this constraint involving this toggle
            for t, bad_pos in constraints[ci]:
                if t == toggle:
                    if pos == bad_pos:
                        bad_count[ci] += 1
                        unassigned_count[ci] -= 1
                        changes.append((ci, 'bad'))
                    else:
                        nonbad_count[ci] += 1
                        unassigned_count[ci] -= 1
                        changes.append((ci, 'nonbad'))
                        constraint_safe[ci] = True
                    break  # only first criterion with this toggle? No, there could be multiple
            # Actually, a toggle can appear multiple times in same check
            # Let me handle all occurrences
        return changes
    
    # Wait, the problem says "A single toggle index may appear multiple times within the same check."
    # So I need to handle all occurrences, not just the first.
    
    # Let me redo this
    pass

solve()