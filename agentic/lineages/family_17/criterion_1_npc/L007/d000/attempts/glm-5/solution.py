def solve(covered, chosen):
    if covered == full: return chosen
    # choose element: MRV or lowest
    ...
    for each triple containing chosen element:
        if mask & covered == 0:
            recurse