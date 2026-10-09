import sys
sys.setrecursionlimit(1000000)

def solve():
    n, m, B = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    # Root the tree at 0
    parent = [-1]*n
    order = [0]
    for u in order:
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                order.append(v)

    # DP: dp[u][k][pos] = minimal cost for subtree of u with size k,
    # where u is at position pos (0-indexed) within that block.
    # We'll store as dict for sparse states.
    INF = 10**18
    dp = [None]*n
    size = [0]*n

    for u in reversed(order):
        children = [v for v in adj[u] if v != parent[u]]
        # Start with just u
        dp[u] = {(1, 0): 0}
        size[u] = 1
        for c in children:
            new_dp = {}
            # Merge child c into u
            for (k1, pos1), cost1 in dp[u].items():
                for (k2, pos2), cost2 in dp[c].items():
                    # Place child block either to left or right of u's block
                    # We'll try both: child block left of u's block, and right.
                    # Left: child occupies positions 0..k2-1, u's block shifted right by k2
                    new_k = k1 + k2
                    # child left
                    new_pos_u = pos1 + k2
                    # cost: cost1 + cost2 + edge cost between u and c
                    # edge cost = distance between u and c in final arrangement
                    # u at new_pos_u, c at pos2 (since child block starts at 0)
                    edge_cost = abs(new_pos_u - pos2)
                    new_cost = cost1 + cost2 + edge_cost
                    key = (new_k, new_pos_u)
                    if key not in new_dp or new_cost < new_dp[key]:
                        new_dp[key] = new_cost
                    # child right: u's block first, child block after
                    new_pos_u2 = pos1
                    new_pos_c = k1 + pos2
                    edge_cost2 = abs(new_pos_u2 - new_pos_c)
                    new_cost2 = cost1 + cost2 + edge_cost2
                    key2 = (new_k, new_pos_u2)
                    if key2 not in new_dp or new_cost2 < new_dp[key2]:
                        new_dp[key2] = new_cost2
            dp[u] = new_dp
            size[u] += size[c]

    # Check if any arrangement with total cost <= B exists
    best = INF
    best_pos = -1
    for (k, pos), cost in dp[0].items():
        if k == n and cost < best:
            best = cost
            best_pos = pos

    if best > B:
        print("NO")
        return

    # Reconstruct the arrangement
    # We need to store parent choices for reconstruction.
    # We'll re-run DP storing decisions.
    # For simplicity, we'll do a second pass storing the chosen child order and positions.
    # We'll store for each node the chosen arrangement of its subtree.
    # We'll do a recursive reconstruction using the DP tables.

    # Store DP tables for reconstruction
    dp_tables = [None]*n
    size = [0]*n
    for u in reversed(order):
        children = [v for v in adj[u] if v != parent[u]]
        dp_tables[u] = {(1, 0): (0, None)}  # cost, list of (child, offset) info
        size[u] = 1
        for c in children:
            new_dp = {}
            for (k1, pos1), (cost1, _) in dp_tables[u].items():
                for (k2, pos2), (cost2, _) in dp_tables[c].items():
                    # child left
                    new_k = k1 + k2
                    new_pos_u = pos1 + k2
                    edge_cost = abs(new_pos_u - pos2)
                    new_cost = cost1 + cost2 + edge_cost
                    key = (new_k, new_pos_u)
                    if key not in new_dp or new_cost < new_dp[key][0]:
                        new_dp[key] = (new_cost, (c, k2, pos2, 'L'))
                    # child right
                    new_pos_u2 = pos1
                    new_pos_c = k1 + pos2
                    edge_cost2 = abs(new_pos_u2 - new_pos_c)
                    new_cost2 = cost1 + cost2 + edge_cost2
                    key2 = (new_k, new_pos_u2)
                    if key2 not in new_dp or new_cost2 < new_dp[key2][0]:
                        new_dp[key2] = (new_cost2, (c, k2, pos2, 'R'))
            dp_tables[u] = new_dp
            size[u] += size[c]

    # Reconstruct
    arrangement = [0]*n
    def place(u, block_start, block_size, pos_u):
        # place subtree u in block [block_start, block_start+block_size-1]
        # with u at position block_start+pos_u
        arrangement[u] = block_start + pos_u
        # get children info from dp_tables[u] for this state
        # We need to find the state (block_size, pos_u) in dp_tables[u]
        # But we stored only cost and last merge info. We'll reconstruct recursively.
        # We'll do a separate reconstruction using stored decisions.
        pass

    # Instead, we'll store full placement during DP.
    # Let's do a simpler approach: store for each node the final positions directly.
    # We'll do a recursive function that uses the DP tables to decide child placements.

    # We'll store the chosen child order and offsets.
    # We'll do a second DP pass storing decisions.

    # Let's store decisions in a dict: for each node, for each (k,pos), store list of (child, child_k, child_pos, side)
    decisions = [None]*n
    size = [0]*n
    for u in reversed(order):
        children = [v for v in adj[u] if v != parent[u]]
        decisions[u] = {(1, 0): []}
        size[u] = 1
        for c in children:
            new_dec = {}
            for (k1, pos1), dec1 in decisions[u].items():
                for (k2, pos2), dec2 in decisions[c].items():
                    # child left
                    new_k = k1 + k2
                    new_pos_u = pos1 + k2
                    key = (new_k, new_pos_u)
                    if key not in new_dec:
                        new_dec[key] = dec1 + [(c, k2, pos2, 'L')]
                    # child right
                    new_pos_u2 = pos1
                    key2 = (new_k, new_pos_u2)
                    if key2 not in new_dec:
                        new_dec[key2] = dec1 + [(c, k2, pos2, 'R')]
            decisions[u] = new_dec
            size[u] += size[c]

    # Now reconstruct positions
    pos_arr = [0]*n
    def build(u, block_start, block_size, pos_u):
        pos_arr[u] = block_start + pos_u
        # get decisions for this state
        dec = decisions[u].get((block_size, pos_u))
        if dec is None:
            return
        # We need to know which child is placed where.
        # We'll process children in order they were merged.
        # But we need to know the relative positions.
        # We'll reconstruct by simulating the merges.
        # We'll do a recursive approach: for each child in dec, we know its block size and its position within its block.
        # We also know side (L or R).
        # We'll compute child's block start.
        cur_start = block_start
        cur_pos_u = pos_u
        # We'll place children one by one.
        # But dec is in merge order, not necessarily left-to-right.
        # We'll instead compute final positions by placing children blocks.
        # We'll do: for each child in dec, we know its block size and its pos within its block.
        # We also know side relative to u's block at the time of merge.
        # This is complex; easier: we can store the final arrangement directly during DP.
        pass

    # Given complexity, we'll instead store the final arrangement during DP by keeping the actual permutation.
    # We'll do a DP that stores the actual list of positions for each state.
    # This is memory heavy but n is small enough.

    # Let's do that: dp[u][(k,pos)] = (cost, list_of_positions)
    dp_final = [None]*n
    size = [0]*n
    for u in reversed(order):
        children = [v for v in adj[u] if v != parent[u]]
        dp_final[u] = {(1, 0): (0, [0])}  # position of u within its block
        size[u] = 1
        for c in children:
            new_dp = {}
            for (k1, pos1), (cost1, arr1) in dp_final[u].items():
                for (k2, pos2), (cost2, arr2) in dp_final[c].items():
                    # child left
                    new_k = k1 + k2
                    new_pos_u = pos1 + k2
                    edge_cost = abs(new_pos_u - pos2)
                    new_cost = cost1 + cost2 + edge_cost
                    # build new arrangement: child block first, then u's block shifted
                    new_arr = [x + k2 for x in arr1] + arr2
                    key = (new_k, new_pos_u)
                    if key not in new_dp or new_cost < new_dp[key][0]:
                        new_dp[key] = (new_cost, new_arr)
                    # child right
                    new_pos_u2 = pos1
                    new_pos_c = k1 + pos2
                    edge_cost2 = abs(new_pos_u2 - new_pos_c)
                    new_cost2 = cost1 + cost2 + edge_cost2
                    new_arr2 = arr1 + [x + k1 for x in arr2]
                    key2 = (new_k, new_pos_u2)
                    if key2 not in new_dp or new_cost2 < new_dp[key2][0]:
                        new_dp[key2] = (new_cost2, new_arr2)
            dp_final[u] = new_dp
            size[u] += size[c]

    # Find best
    best_cost = INF
    best_arr = None
    for (k, pos), (cost, arr) in dp_final[0].items():
        if k == n and cost < best_cost:
            best_cost = cost
            best_arr = arr

    if best_cost > B:
        print("NO")
    else:
        print("YES")
        # best_arr contains positions of nodes in order of subtree traversal, not unit numbers.
        # We need to map to unit numbers.
        # The arr is the positions of nodes in the subtree order (preorder).
        # We need to know which node is which.
        # We'll store node order during DP.
        # Let's redo with node labels.

    # Actually, we need to output positions for each unit 1..n.
    # We'll store node labels in the arrangement.
    # Let's modify to store node indices.

    dp_final = [None]*n
    size = [0]*n
    for u in reversed(order):
        children = [v for v in adj[u] if v != parent[u]]
        dp_final[u] = {(1, 0): (0, [u])}
        size[u] = 1
        for c in children:
            new_dp = {}
            for (k1, pos1), (cost1, arr1) in dp_final[u].items():
                for (k2, pos2), (cost2, arr2) in dp_final[c].items():
                    # child left
                    new_k = k1 + k2
                    new_pos_u = pos1 + k2
                    edge_cost = abs(new_pos_u - pos2)
                    new_cost = cost1 + cost2 + edge_cost
                    new_arr = arr2 + arr1  # child block first, then u's block
                    key = (new_k, new_pos_u)
                    if key not in new_dp or new_cost < new_dp[key][0]:
                        new_dp[key] = (new_cost, new_arr)
                    # child right
                    new_pos_u2 = pos1
                    new_pos_c = k1 + pos2
                    edge_cost2 = abs(new_pos_u2 - new_pos_c)
                    new_cost2 = cost1 + cost2 + edge_cost2
                    new_arr2 = arr1 + arr2
                    key2 = (new_k, new_pos_u2)
                    if key2 not in new_dp or new_cost2 < new_dp[key2][0]:
                        new_dp[key2] = (new_cost2, new_arr2)
            dp_final[u] = new_dp
            size[u] += size[c]

    best_cost = INF
    best_arr = None
    for (k, pos), (cost, arr) in dp_final[0].items():
        if k == n and cost < best_cost:
            best_cost = cost
            best_arr = arr

    if best_cost > B:
        print("NO")
    else:
        print("YES")
        # best_arr is list of node indices in order of positions 0..n-1
        pos_of = [0]*n
        for slot, node in enumerate(best_arr):
            pos_of[node] = slot + 1
        print(' '.join(map(str, pos_of)))

if __name__ == "__main__":
    solve()