import sys
from itertools import combinations

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    M = int(input_data[1])
    T = int(input_data[2])
    m = int(input_data[3])

    adj = [[] for _ in range(n + 1)]
    rev_adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    out_degree = [0] * (n + 1)

    idx = 4
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u].append(v)
        rev_adj[v].append(u)
        out_degree[u] += 1
        in_degree[v] += 1

    # Check for cycles and compute ASAP (earliest possible shift for each component)
    asap = [1] * (n + 1)
    # Topological sort for ASAP
    q = [i for i in range(1, n + 1) if in_degree[i] == 0]
    head = 0
    in_deg_copy = list(in_degree)
    top_order = []
    while head < len(q):
        u = q[head]
        head += 1
        top_order.append(u)
        for v in adj[u]:
            if asap[u] + 1 > asap[v]:
                asap[v] = asap[u] + 1
            in_deg_copy[v] -= 1
            if in_deg_copy[v] == 0:
                q.append(v)

    if len(top_order) < n:
        print("NO")
        return

    for i in range(1, n + 1):
        if asap[i] > T:
            print("NO")
            return

    # Compute depth from source (longest path from any ancestor)
    depth = list(asap)

    # Compute number of ancestors for tie-breaking
    # Transitive closure or simple reachability count if needed, but depth & asap are strong
    ans_shift = [0] * (n + 1)
    current_out_deg = list(out_degree)
    
    # Ready set for backward scheduling: unscheduled jobs with current_out_deg == 0
    ready = [i for i in range(1, n + 1) if current_out_deg[i] == 0]
    unscheduled = set(range(1, n + 1))

    # Priority key for ready jobs (higher is more critical to schedule first)
    def priority_key(u):
        return (asap[u], depth[u], len(rev_adj[u]))

    # Necessary Hall-like condition check
    def is_feasible(t):
        if not unscheduled:
            return True
        # Check if any unscheduled node has asap > t
        # Also check count of nodes with asap >= s does not exceed (t - s + 1) * M
        counts = [0] * (t + 2)
        for u in unscheduled:
            if asap[u] > t:
                return False
            counts[asap[u]] += 1
        
        # Suffix sums
        suff = 0
        for s in range(t, 0, -1):
            suff += counts[s]
            if suff > (t - s + 1) * M:
                return False
        return True

    found = False

    def backtrack(t, current_ready):
        nonlocal found
        if not unscheduled:
            found = True
            return True
        if t < 1:
            return False
        if not is_feasible(t):
            return False

        current_ready_sorted = sorted(current_ready, key=priority_key, reverse=True)

        k = min(M, len(current_ready_sorted))
        if k == 0:
            return False

        if len(current_ready_sorted) <= M:
            chosen_subsets = [current_ready_sorted]
        else:
            # Generate subsets, prioritizing the top elements
            # Taking the top k is the primary greedy choice
            # Also try other combinations if greedy fails
            best = current_ready_sorted[:k]
            chosen_subsets = [best]
            # Add other combinations of size k from the first few candidates to avoid explosion
            pool = current_ready_sorted[:min(len(current_ready_sorted), k + 4)]
            for combo in combinations(pool, k):
                c_list = list(combo)
                if c_list != best:
                    chosen_subsets.append(c_list)

        for chosen in chosen_subsets:
            # Apply choice
            new_ready = [x for x in current_ready if x not in chosen]
            for u in chosen:
                ans_shift[u] = t
                unscheduled.remove(u)
                for p in rev_adj[u]:
                    current_out_deg[p] -= 1
                    if current_out_deg[p] == 0:
                        new_ready.append(p)

            if backtrack(t - 1, new_ready):
                return True

            # Revert choice
            for u in chosen:
                for p in rev_adj[u]:
                    current_out_deg[p] += 1
                unscheduled.add(u)
                ans_shift[u] = 0

        return False

    if backtrack(T, ready):
        print("YES")
        print(*(ans_shift[i] for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()