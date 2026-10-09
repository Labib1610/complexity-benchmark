import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    k = int(data[0]); t = int(data[1])
    idx = 2
    # Build adjacency: for each operator x, list of (y, z)
    adj = [[] for _ in range(k+1)]
    for _ in range(t):
        x = int(data[idx]); y = int(data[idx+1]); z = int(data[idx+2])
        idx += 3
        adj[x].append((y, z))
    
    # We need to select exactly k triples, one per operator, all y distinct, all z distinct.
    # This is a 3D matching problem. With k<=22, use DP with bitmask over y and z.
    # State: (operator index, mask_y, mask_z). But 2^22 * 2^22 is too large.
    # Instead, process operators one by one and keep a dict of reachable (mask_y, mask_z) states.
    # But that's still too many states in worst case.
    # 
    # Better: Since we need exactly k operators and k y's and k z's, and each operator must be used,
    # we can think of it as assigning to each operator a (y,z) pair such that all y distinct and all z distinct.
    # 
    # We can use meet-in-the-middle or backtracking with pruning. Given k<=22, a well-pruned
    # backtracking might work, but worst case could be hard.
    #
    # Alternative: model as bipartite matching between operators and (y,z) pairs? No, because
    # y and z both need to be distinct, so it's a 3D matching.
    #
    # Let's try DP with memoization on (operator_index, mask_y, mask_z) but using a dictionary
    # and only storing reachable states. With k=22, if the graph is dense, states explode.
    #
    # However, we can reduce: process operators in order of increasing degree (most constrained first).
    # Use recursive backtracking with bitmasks for y and z. Prune if remaining operators can't
    # be matched.
    #
    # Given time limit 5s and k<=22, let's implement backtracking with bitmasks and ordering.
    
    # Order operators by degree (ascending)
    operators = list(range(1, k+1))
    operators.sort(key=lambda x: len(adj[x]))
    
    # Precompute for pruning: for a suffix of operators, the set of available y and z
    # We can compute union of y's and z's for remaining operators and check if enough bits available.
    
    # Convert adj to lists
    # adj[x] is list of (y,z)
    
    # We'll do DFS with state (i, mask_y, mask_z) where i is index into operators list
    # mask_y and mask_z are ints with bits for used y and z (1-indexed, bit y means y used)
    
    # Pruning: for remaining operators operators[i:], compute the set of y's they can use
    # (excluding already used) and z's. If the number of available y bits < (k-i) or z bits < (k-i), prune.
    # Also, we can check Hall's condition more tightly but let's start simple.
    
    # Precompute suffix unions of y and z
    suffix_y = [0]*(k+2)
    suffix_z = [0]*(k+2)
    for i in range(k-1, -1, -1):
        op = operators[i]
        yset = 0; zset = 0
        for (y,z) in adj[op]:
            yset |= (1 << y)
            zset |= (1 << z)
        suffix_y[i] = suffix_y[i+1] | yset
        suffix_z[i] = suffix_z[i+1] | zset
    
    assignment = [0]*(k+1)  # assignment[op] = (y,z)
    
    # For fast pruning, also precompute per operator the y and z masks
    op_y_masks = [0]*(k+1)
    op_z_masks = [0]*(k+1)
    op_edges = [[] for _ in range(k+1)]
    for op in operators:
        ym = 0; zm = 0
        for (y,z) in adj[op]:
            ym |= (1 << y)
            zm |= (1 << z)
            op_edges[op].append((y,z))
        op_y_masks[op] = ym
        op_z_masks[op] = zm
    
    # Recursive DFS
    # We'll use iterative or recursive. Python recursion limit might be an issue for k=22, but depth is 22, fine.
    
    found = [False]
    result = [None]
    
    # To speed up, we can use a stack iteratively, but recursion is simpler.
    # Let's implement recursive with pruning.
    
    def dfs(i, mask_y, mask_z):
        if found[0]:
            return
        if i == k:
            found[0] = True
            result[0] = assignment[:]
            return
        op = operators[i]
        # Prune: check if remaining can possibly be satisfied
        # Available y for remaining: suffix_y[i] & ~mask_y
        avail_y = suffix_y[i] & ~mask_y
        avail_z = suffix_z[i] & ~mask_z
        # Need (k - i) more y's and z's
        if bin(avail_y).count('1') < (k - i):
            return
        if bin(avail_z).count('1') < (k - i):
            return
        # Also, for this operator, if it has no available edges, prune
        # We can iterate edges and try
        for (y,z) in op_edges[op]:
            yb = 1 << y
            zb = 1 << z
            if (mask_y & yb) == 0 and (mask_z & zb) == 0:
                assignment[op] = (y,z)
                dfs(i+1, mask_y | yb, mask_z | zb)
                if found[0]:
                    return
                assignment[op] = 0
        return
    
    dfs(0, 0, 0)
    
    if found[0]:
        out = ["YES"]
        for op in range(1, k+1):
            y,z = result[0][op]
            out.append(f"{op} {y} {z}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

solve()