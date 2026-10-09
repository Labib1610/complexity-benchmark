import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # Build adjacency: for each processor x, list of (y, z) pairs
    adj = [[] for _ in range(k + 1)]
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        adj[x].append((y, z))
    
    # We need a perfect matching in a 3-partite 3-uniform hypergraph.
    # Use backtracking with bitmask for sensors and transmitters.
    # Assign processors 1..k in order.
    
    used_sensors = 0
    used_transmitters = 0
    assignment = [None] * (k + 1)  # assignment[x] = (y, z)
    
    # Precompute for each processor the list of valid (y,z) pairs
    # Filter: y and z must be in 1..k (guaranteed by input)
    
    def backtrack(x, used_s, used_t):
        if x > k:
            return True
        for (y, z) in adj[x]:
            bit_y = 1 << y
            bit_z = 1 << z
            if (used_s & bit_y) == 0 and (used_t & bit_z) == 0:
                assignment[x] = (y, z)
                if backtrack(x + 1, used_s | bit_y, used_t | bit_z):
                    return True
        assignment[x] = None
        return False
    
    if backtrack(1, 0, 0):
        out = ["YES"]
        for x in range(1, k + 1):
            y, z = assignment[x]
            out.append(f"{x} {y} {z}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

solve()