import sys

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
    
    if n > M * T:
        print("NO")
        return

    adj = [[] for _ in range(n + 1)]
    radj = [[] for _ in range(n + 1)]
    in_deg = [0] * (n + 1)
    
    idx = 4
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        adj[u].append(v)
        radj[v].append(u)
        in_deg[v] += 1
        
    # Check for cycles and get topological order
    from collections import deque
    q = deque([i for i in range(1, n + 1) if in_deg[i] == 0])
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                q.append(v)
                
    if len(topo) < n:
        print("NO")
        return
        
    # Compute Earliest (E) and Latest (L) times
    E = [1] * (n + 1)
    for u in topo:
        for v in adj[u]:
            if E[u] + 1 > E[v]:
                E[v] = E[u] + 1
                
    L = [T] * (n + 1)
    for u in reversed(topo):
        for v in radj[u]:
            if L[u] - 1 < L[v]:
                L[v] = L[u] - 1
                
    for i in range(1, n + 1):
        if E[i] > L[i]:
            print("NO")
            return

    # Compute descendant count / max depth to break ties
    depth = [1] * (n + 1)
    desc_count = [1] * (n + 1)
    for u in reversed(topo):
        d = 1
        cnt = 1
        for v in adj[u]:
            if depth[v] + 1 > d:
                d = depth[v] + 1
            cnt += desc_count[v]
        depth[u] = d
        desc_count[u] = cnt

    # Check energetic condition initially
    for t_a in range(1, T + 1):
        for t_b in range(t_a, T + 1):
            cap = (t_b - t_a + 1) * M
            cnt = sum(1 for i in range(1, n + 1) if E[i] >= t_a and L[i] <= t_b)
            if cnt > cap:
                print("NO")
                return

    # Backtracking search slot by slot
    # State:
    # current_in_deg: current remaining in-degrees
    # assignment: ans[i]
    ans = [0] * (n + 1)
    cur_in_deg = [len(radj[i]) for i in range(n + 1)]
    
    # Priority key for candidates: (L[x], -depth[x], -desc_count[x], x)
    def get_key(x):
        return (L[x], -depth[x], -desc_count[x], x)

    import itertools

    def search(t, available):
        if t > T:
            return all(ans[i] > 0 for i in range(1, n + 1))
        
        # Check mandatory jobs that must be scheduled at or before t
        # (Since they are available now, if L[x] == t, they must be scheduled at t)
        mandatory = []
        optional = []
        for x in available:
            if L[x] < t:
                # Impossible, missed deadline
                return False
            elif L[x] == t:
                mandatory.append(x)
            else:
                optional.append(x)
                
        if len(mandatory) > M:
            return False
            
        needed = M - len(mandatory)
        optional.sort(key=get_key)
        
        # If total remaining jobs can all fit in this and future slots
        # We try to take greedy combinations of optional jobs
        # To avoid combinatorial explosion, limit the number of subsets explored
        max_take = min(needed, len(optional))
        
        # Try larger takes first
        # Usually greedy (taking top by priority) is best
        options_to_try = []
        
        # Greedy choice: take top `k` from optional
        for k in range(max_take, -1, -1):
            options_to_try.append(optional[:k])
            
        # Also try single alternative combinations if small
        if len(optional) <= 8:
            for k in range(max_take, -1, -1):
                for comb in itertools.combinations(optional, k):
                    comb_list = list(comb)
                    if comb_list not in options_to_try:
                        options_to_try.append(comb_list)
        
        for chosen_opt in options_to_try:
            chosen = mandatory + chosen_opt
            # Assign
            for x in chosen:
                ans[x] = t
            
            new_available = [x for x in available if x not in chosen]
            # Unlocked jobs
            unlocked = []
            for x in chosen:
                for v in adj[x]:
                    cur_in_deg[v] -= 1
                    if cur_in_deg[v] == 0:
                        unlocked.append(v)
            
            next_available = new_available + unlocked
            
            # Recurse
            if search(t + 1, next_available):
                return True
                
            # Backtrack
            for v in unlocked:
                cur_in_deg[v] += 1
            for x in chosen:
                for v in adj[x]:
                    if v not in unlocked:
                        cur_in_deg[v] += 1
            for x in chosen:
                ans[x] = 0
                
        return False

    initial_available = [i for i in range(1, n + 1) if cur_in_deg[i] == 0]
    if search(1, initial_available):
        print("YES")
        print(*(ans[i] for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()