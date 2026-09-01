import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    adj = [0] * n
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # Precompute valid masks for each subset of vertices
    # valid_mask[S] = 1 if S is an independent set, 0 otherwise
    size = 1 << n
    valid_mask = [1] * size
    
    # Using SOS DP to check independence:
    # If S is valid, then S without its lowest bit is valid.
    # If S is invalid, it remains invalid.
    # We iterate bits from 0 to n-1.
    for i in range(n):
        step = 1 << i
        for mask in range(size):
            if mask & step:
                # If the set including bit i is currently marked valid,
                # check if adding vertex i creates a conflict with the rest of the set.
                # The rest of the set is mask ^ step.
                # If valid_mask[mask ^ step] is 0, the subset was already invalid.
                # If adj[i] has intersection with (mask ^ step), then i is connected to someone in the set.
                if valid_mask[mask ^ step] and (adj[i] & (mask ^ step)):
                    valid_mask[mask] = 0

    # Iterate over all partitions of vertices into 3 sets (S1, S2, S3)
    # S1 is the set of workers assigned to shift 1.
    # S2 is the set of workers assigned to shift 2.
    # S3 is the remaining workers (shift 3).
    # We iterate S1 from 0 to 2^n - 1.
    # For each valid S1, we iterate S2 from 0 to remaining.
    
    best_assignment = None
    
    for s1 in range(size):
        if not valid_mask[s1]:
            continue
        
        rem1 = size - 1 - s1
        s2 = rem1
        while True:
            # Check if s1 and s2 are disjoint (s2 is a subset of rem1, so yes)
            # Check if s2 is valid
            if valid_mask[s2]:
                s3 = rem1 - s2
                # Check if s3 is valid
                if valid_mask[s3]:
                    # Found a valid partition
                    # Construct the assignment array
                    assignment = [0] * n
                    for i in range(n):
                        if (s1 >> i) & 1:
                            assignment[i] = 1
                        elif (s2 >> i) & 1:
                            assignment[i] = 2
                        else:
                            assignment[i] = 3
                    
                    # Since we iterate s1 from 0..2^n-1 and s2 from rem1 downwards,
                    # the first found assignment corresponds to the lexicographically smallest sequence.
                    # s1=0 means no 1s, s1=1 means worker 0 is 1 (lexicographically large start).
                    # Wait, standard integer iteration:
                    # s1=0 -> all 3s
                    # s1=1 -> worker 0 is 1, rest 3s -> 1 3 3 3...
                    # s1=2 -> worker 1 is 1, rest 3s -> 3 1 3 3...
                    # 1 3 3... is lexicographically smaller than 3 1 3...
                    # So iterating s1 by integer value finds the lex-smallest assignment.
                    
                    print("YES")
                    print(*(assignment[i] for i in range(n)))
                    return
            
            if s2 == 0:
                break
            s2 = (s2 - 1) & rem1

    print("NO")

if __name__ == '__main__':
    solve()