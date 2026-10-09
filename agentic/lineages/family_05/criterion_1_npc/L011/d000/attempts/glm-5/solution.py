import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    k = int(data[0]); t = int(data[1])
    idx = 2
    # profiles[x] = list of (y, z)
    profiles = [[] for _ in range(k+1)]
    for _ in range(t):
        x = int(data[idx]); y = int(data[idx+1]); z = int(data[idx+2])
        idx += 3
        profiles[x].append((y, z))
    
    # For each operator x, we need to pick a (y, z) pair.
    # y's must be a permutation of 1..k, z's must be a permutation of 1..k.
    # We do backtracking over operators 1..k.
    
    used_y = [False] * (k+1)
    used_z = [False] * (k+1)
    assignment = [None] * (k+1)  # assignment[x] = (y, z)
    
    # Sort operators by number of available profiles (heuristic)
    order = sorted(range(1, k+1), key=lambda x: len(profiles[x]))
    
    # Also sort each operator's profiles for deterministic / faster pruning
    for x in range(1, k+1):
        profiles[x].sort()
    
    def backtrack(i):
        if i == k:
            return True
        x = order[i]
        for (y, z) in profiles[x]:
            if not used_y[y] and not used_z[z]:
                used_y[y] = True
                used_z[z] = True
                assignment[x] = (y, z)
                if backtrack(i+1):
                    return True
                used_y[y] = False
                used_z[z] = False
                assignment[x] = None
        return False
    
    if backtrack(0):
        out = ["YES"]
        for x in range(1, k+1):
            y, z = assignment[x]
            out.append(f"{x} {y} {z}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

solve()